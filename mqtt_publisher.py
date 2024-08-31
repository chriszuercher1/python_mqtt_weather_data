import time
import random
import paho.mqtt.client as mqtt

# MQTT broker settings
broker = "localhost"
port = 1883
topic = "sensor/temperature"

# Initialize the MQTT client
client = mqtt.Client("TemperaturePublisher", clean_session=False)

# Set the Last Will and Testament (LWT)
client.will_set(topic, "Client disconnected", qos=1, retain=True)

# Enable logging
client.on_log = lambda client, userdata, level, buf: print(f"Log: {buf}")

# Connect to the MQTT broker
client.connect(broker, port)

# Function to simulate and publish temperature data
def publish_temperature_data():
    for i in range(100):
        # Simulate temperature
        temperature = round(random.uniform(24.0, 25.0), 2)
        message = f"Temperature: {temperature}°C"
        client.publish(topic, message, qos=1, retain=True)
        time.sleep(0.5)

# Publish temperature data
publish_temperature_data()

# Disconnect from the broker
client.disconnect()