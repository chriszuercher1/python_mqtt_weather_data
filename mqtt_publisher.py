import time
import requests
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

# Function to fetch the most recent air temperature data from the API
def get_most_recent_air_temperature():
    url = "https://tecdottir.herokuapp.com/measurements/tiefenbrunnen?startDate=2024-09-01&sort=timestamp_cet%20desc&limit=500&offset=0"
    response = requests.get(url)
    data = response.json()

    if data["ok"] and len(data["result"]) > 0:
        # Assuming the most recent entry is the first in the sorted list
        most_recent_entry = data["result"][0]
        air_temperature = most_recent_entry["values"]["air_temperature"]["value"]
        return air_temperature
    else:
        return None

# Function to fetch and publish air temperature data
def publish_temperature_data():
    try:
        while True:
            air_temperature = get_most_recent_air_temperature()
            if air_temperature is not None:
                message = str(air_temperature)
                print(f"Publishing: {message}°C")
                client.publish(topic, message)
            else:
                print("No data available.")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Disconnecting from broker...")
        client.disconnect()

if __name__ == "__main__":
    # Publish temperature data
    publish_temperature_data()
