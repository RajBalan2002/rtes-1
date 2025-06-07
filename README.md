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




