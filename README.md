# Smart Room Automation System with Data Logging

## Overview
This project is an Arduino-based smart lighting system that automatically controls an LED based on motion and light levels. The system also logs real-time data to Python for analysis and visualisation.

## Features
- Motion detection using PIR sensor
- Light detection using LDR
- Automatic LED control
- Manual ON/OFF modes via button
- Non-blocking timing using millis()
- Data logging using Python
- Graph visualisation of system behaviour

## System Design
The system combines inputs from a motion sensor and light sensor. When it is dark and motion is detected, the LED turns on and remains on for a fixed time.

A button allows switching between:
- AUTO mode
- MANUAL ON
- MANUAL OFF

## Data Logging
The Arduino sends data in CSV format via serial communication:


A Python script reads this data, saves it to a CSV file, and generates a graph.

## Images

### Circuit Setup
![Circuit](circuit.jpg)

### System Setup
![Setup](setup.jpg)

### Data Graph
![Graph](graph.png)

## Files
- Arduino/smart_room.ino → Arduino code
- Python/data_logger.py → Python logging script
- Data/example_data.csv → sample data output

## Conclusion
This project demonstrates a complete system integrating sensors, control logic, user interaction, and data analysis using both Arduino and Python.
