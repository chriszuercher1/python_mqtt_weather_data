import time
import random
import paho.mqtt.client as mqtt

# MQTT broker settings
broker = "localhost"
port = 1883
topic = "sensor/temp"

# Initialize the MQTT client
client = mqtt.Client("TemperaturePublisher")

# Enable logging (optional)
# client.on_log = lambda client, userdata, level, buf: print(f"Log: {buf}")

# Connect to the MQTT broker
client.connect(broker, port)

# Function to simulate and publish temperature data
def publish_temperature_data():
    try:
        while True:
            # Simulate temperature
            temperature = round(random.uniform(24.0, 25.0), 2)
            message = str(temperature)  # Send as string
            print(f"Publishing: {message}")
            client.publish(topic, message, qos=1, retain=False)
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Disconnecting from broker...")
        client.disconnect()

# Publish temperature data
publish_temperature_data()