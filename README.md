# Can Bus Anomaly detection
A multithreaded, real time CAN bus analyzer built in Python using SocketCAN, designed for vehicle diagnostics and embedded systems simulations.

# Project Overview
This tool listens to a virtual CAN interface ('vcan0') , decode messages for vehicle signals like Engine RPM, temperature and detects anomalies such as out of range values and missing messages. All data is displayed in real time on a web dashboard and logged for post-analysis.

# Features
Live CAN bus monitoring via python-can
CAN frame decoding (RPM,temperature,Brake Pressure)
Anomaly Detection (value thresholds & timeout detection)
Real Time Dashboard using StreamLit
Multithreaded CAN listener with Background processing
Persistent Logging of messages and anomalies to CSV

# Project Structure

can_listener.py  → Listens to CAN messages on vcan0
can_decoder.py   → Decodes specific CAN IDs into signals
can_anomaly.py   → Detects value/time-based anomalies
can_logger.py    → Logs all messages to can_log.csv
can_dashboard.py → Real-time dashboard UI using Streamlit
anomaly_log.csv  → Output: Anomaly logs
can_log.csv      → Output: Full CAN message log

# Technologies and Libraries

[python-can](https://python-can.readthedocs.io/en/master/)
[SocketCAN](https://www.kernel.org/doc/Documentation/networking/can.txt)
[Streamlit](https://streamlit.io/)

# Setup and Run Instructions

### Prerequistes
- Python 3.7+
- Linux system with **SocketCAN**
- Virtual CAN interface (`vcan0`) setup

### Setup Virtual CAN interface in Linux

sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0

### Run the dashboard

streamlit run can_dashboard.py




