import can
import can_logger
import queue
import threading

can_msg_queue = queue.Queue()

def listen_to_can(channel="vcan0",bustype="socketcan"):
	bus=can.interface.Bus(channel=channel,bustype=bustype)
	print(f"Listening on {channel}....")
	try:
		for msg in bus:
			can_msg_queue.put(msg)
			print(f"ID: {hex(msg.arbitration_id)} | DLC: {msg.dlc} | Data: {msg.data.hex()} | Timestamp:{msg.timestamp}")
	except KeywordInterrupt:
		print("\nStopped CAN Listener")
def start_can_listener():
	listener_thread = threading.Thread(target=listen_to_can)
	listener_thread.daemon = True
	listener_thread.start()
if __name__ == "__main__":
	can_logger.initialize_log()
	start_can_listener()
	while True:
		if not can_msg_queue.empty():
			msg = can_msg_queue.get(msg)
			signal_name,decoded_value = can_decoder.decode_can_message(msg)
			print(f"Received: ID = {hex(msg.arbitration_id)}, Data = {msg.data.hex()} , Timestamp = {msg.timestamp}") 
			can_logger.log_can_message(msg)

