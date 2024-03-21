import random
import time
import paho.mqtt.client as mqtt
import uuid

MQTT_BROKER = "mqtt.thingspeak.com"
MQTT_PORT = 1883
STATION_ID = str(uuid.uuid4())
CHANNEL_ID = "2479393"
WRITE_API_KEY = "7ONCL9GXWVZZS5MU"

MQTT_TOPIC = f"channels/{CHANNEL_ID}/publish/{WRITE_API_KEY}"

def generate_sensor_values():
    temperature = random.uniform(-50, 50)
    humidity = random.uniform(0, 100)
    co2 = random.uniform(300, 2000)
    return temperature, humidity, co2

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker.")
    else:
        print(f"Failed to connect, return code {rc}\n")

def publish_sensor_data(client, temperature, humidity, co2):
    payload = f"field1={temperature}&field2={humidity}&field3={co2}"
    result = client.publish(MQTT_TOPIC, payload)
    status = result[0]
    if status == 0:
        print(f"Sent `{payload}` to topic `{MQTT_TOPIC}`")
    else:
        print(f"Failed to send message to topic {MQTT_TOPIC}")

def main():
    client = mqtt.Client(client_id=STATION_ID)
    client.on_connect = on_connect
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()

    while True:
        temperature, humidity, co2 = generate_sensor_values()
        publish_sensor_data(client, temperature, humidity, co2)
        time.sleep(10)

    client.loop_stop()
    client.disconnect()

if __name__ == "__main__":
    main()
