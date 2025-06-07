import time

last_received = {}

timeout_threshold = 2.0
rpm_upper_limit = 8000
rpm_lower_limit = 500
temp_upper_limit = 120
temp_lower_limit = -40

def check_anomalies(msg,decoded_signal,decoded_value):
	alerts=[]
	current_time=time.time()
	can_id=msg.arbitration_id

	last_received[can_id] = current_time
	if decoded_signal == "Engine RPM":
		try:
			rpm = int(decoded_value.split()[0])
			if rpm >rpm_upper_limit or rpm < rpm_lower_limit:
				alerts.append(f" RPM out of bounds: {rpm} RPM")
		except:
			pass
	elif decoded_signal == "Temperature Sensor":
		try:
			temperature = int(decoded_value.split()[0])
			if temperature > temp_upper_limit or temperature < temp_lower_limit:
				alerts.append(f" Temperature out of bounds: {temperature} C")
		except:
			pass
	return alerts

def check_message_timeouts():
	alerts=[]
	current_time = time.time()
	
	for can_id, last_time in last_received.items():
		if(current_time - last_time) > timeout_threshold:
			alerts.append(f" Timeout detected for CAN ID {hex(can_id)} (No message for {timeout_threshold} seconds)")
	return alerts

