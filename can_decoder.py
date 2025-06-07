
def decode_can_message(msg):
	known_signals = {
		0x123 : "Engine RPM",
		0x124 : "temperature sensor",
		0x125 : "Brake pressure"
		}
	signal_name = known_signals.get(msg.arbitration_id, "Unknown Signal")
	
	if msg.arbitration_id == 0x123:
		rpm = int.from_bytes(msg.data[0:2], byteorder = 'big')
		decoded_value = f"{rpm} RPM"
	elif msg.arbitration_id == 0x124:
		temperature = int(msg.data[0])
		decoded_value = f"{temperature} C"
	elif msg.arbitration_id == 0x125:
		pressure = int.from_bytes(msg.data[0:2], byteorder='big') / 10
		decoded_value = f"{pressure} Bar"
	else:
		decoded_value = msg.data.hex()
	return signal_name, decoded_value
