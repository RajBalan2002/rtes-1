import streamlit as st
import pandas as pd
import queue
import can
import can_listener
import can_decoder
import can_anomaly
import time
import matplotlib.pyplot as plt
import csv



msg_queue = can_listener.can_msg_queue
st.set_page_config( page_title = "CAN Bus Analyzer", layout="wide")
st.title("CAN bus Real-Time Dashboard")
start_logging = st.button("start logging")
stop_logging = st.button("stop logging")
placeholder = st.empty()
plot_placeholder = st.empty()
can_listener.start_can_listener()
data = []
time_data = []
engine_rpm_data = []
temp_data = []
log_active = False

anomaly_log_file = "anomaly_log.csv"

with open(anomaly_log_file, mode = 'w' , newline = '') as file:
	writer = csv.writer(file)
	writer.writerow(["Timestamp" , "CAN ID" , "Signal" , "Value" , "Anomaly"])

last_timeout_check = time.time()
while True:
	if start_logging:
		log_active = True
	if stop_logging:
		log_active = False
	elif msg_queue.empty():
		msg = msg_queue.get()
		signal_name, decoded_value = can_decoder.decode_can_message(msg)
		row = {
			"Timestamp" : msg.timestamp,
			"CAN ID": hex(msg.arbitration_id),
			"Signal":signal_name,
			"Value": decoded_value
			}
		data.append(row)

		if len(data) > 50:
			data = data[-50:]
			df = pd.DataFrame(data)
			placeholder.dataframe(df, use_container_width=True)
	
		value_alerts=can_anomaly.check_anomalies(msg, signal_name,decoded_value)
		for alert in value_alerts:
			st.warning(alert)
			with open(anomaly_log_file, mode='a',newline='') as file:
				writer = csv.writer(file)
				writer.writerow([msg.timestamp, hex(msg.arbitration_id), signal_name, decoded_value, alert])
			print(alert)
		if signal_name == "Engine RPM":
			engine_rpm_data.append(decoded_value)
			time_data.append(msg.timestamp)
		elif signal_name == "Temperature":
			temp_data.append(msg.timestamp)
		if engine_rpm_data:
			st.line_chart(engine_rpm_data, height=150)
		if temp_data:
			st.line_chart(temp_data, height=150)

	if (time.time() - last_timeout_check) > 2:
		timeout_alerts = can_anomaly.check_message_timeouts()
		for timeout_alert in timeout_alerts:
			st.error(timeout_alert)
			print(timeout_alert)
		last_timeout_check = time.time()
	df = pd.DataFrame(data)
	def highlight_anomalies(row):
		if row["Signal"] == "Engine RPM" and row["Value"] > 8000:
			return ['background-color: red'] * len(row)
		if row["Signal"] == "Temperature" and row["Value"] > 100:
			return ['background-color: orange'] * len(row)
		return [''] * len(row)
	style_df = df.style.apply(highlight_anomalies, axis=1)
	placeholder.dataframe(df, use_container_width=True)
	
	if len(engine_rpm_data) > 1 and len(temp_data) > 1:
		fig,ax = plt.subplots()
		ax.plot(time_data[-50:], engine_rpm_data[-50:], label="Engine RPM", color = 'blue')
		ax.plot(time_data[-50:], temp_data[-50:], label="temperature", color = 'orange')
		ax.set_xlabel("time")
		ax.set_ylabel("Value")
		ax.set_title("real time monitoring")
		ax.legend
		plot_placeholder.pyplot(fig)
	time.sleep(0.1)



