import time
import requests
from datetime import datetime
import paho.mqtt.client as mqtt

# MQTT broker settings
broker = "localhost"
port = 1883
topic = "sensor/temp"

# Initialize the MQTT client
client = mqtt.Client("Publisher")

# Enable logging (optional)
# client.on_log = lambda client, userdata, level, buf: print(f"Log: {buf}")

# Connect to the MQTT broker
client.connect(broker, port)

# Function to fetch the most recent data from the weather API
def get_data():
    url = "https://tecdottir.herokuapp.com/measurements/tiefenbrunnen?sort=timestamp_cet%20desc&limit=5"
    response = requests.get(url)
    data = response.json()

    if data["ok"] and len(data["result"]) > 0:
        # Assuming the most recent entry is the first in the sorted list
        most_recent_entry = data["result"][0]
        value = most_recent_entry["values"]["air_temperature"]["value"]
        return value
    else:
        return None

# Function to fetch and publish data
def publish_data():
    try:
        while True:
            value = get_data()
            if value is not None:
                message = str(value)
                print(f"Publishing: {message}°C from {topic}")
                client.publish(topic, message)
            else:
                print("No data available.")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Disconnecting from broker...")
        client.disconnect()

if __name__ == "__main__":
    # Publish data
    publish_data()
