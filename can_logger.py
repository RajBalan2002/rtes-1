import csv
import os

log_file = "can_log.csv"

def initilize_log():
	if not os.path.exists(log_file):
		with open(log_file, mode='w' , newline='') as file:
			writer = csv.writer(file)
			writer.writerow(["Timestamp" , "CAN_ID" , "DLC" , "Data"])
def log_can_msg(msg):
	with open(log_file, mode='a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([ msg.timestamp, hex(msg.arbitration_id), msg.dlc, msg.data.hex()])

