# Virtual Environmental Station IoT System

This system simulates a virtual environmental station that generates and publishes sensor data to ThingSpeak using MQTT. Here's a brief rundown of the steps involved in developing this IoT system:

## System Components
- **Virtual Sensors**: Simulate environmental data.
- **MQTT Protocol**: Facilitates communication between the virtual station and the cloud.
- **ThingSpeak Platform**: Cloud service for data aggregation and visualization.

## Development Steps

1. **Configure Virtual Environment**:
   - Use Python to simulate an environmental station with virtual sensors for temperature, humidity, and CO2 levels.

2. **Generate Sensor Data**:
   - Randomly generate data within specified ranges for each sensor.

3. **Setup MQTT Communication**:
   - Initialize an MQTT client in Python with the Paho MQTT library.
   - Configure the client with the MQTT broker's details (ThingSpeak).

4. **Publish Sensor Data**:
   - Create a payload with the generated sensor values.
   - Publish the payload to a specific Topic on ThingSpeak.

5. **Continuous Operation**:
   - Loop the data generation and publishing process, with a pause between iterations to simulate real-time data collection.

## Running the System
- Execute the Python script to start the simulation.
- Data is periodically generated and sent to ThingSpeak.
- Visualize the data on the ThingSpeak channel.

## Dependencies
- Python 3
- Paho MQTT Library

## Installation
Ensure Python and Paho MQTT are installed:
```bash
pip install paho-mqtt
