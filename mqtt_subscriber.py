import paho.mqtt.client as mqtt

# MQTT broker settings
broker = "localhost"
port = 1883
topic = "sensor/temp"

# Callback function for when a message is received
def on_message(client, userdata, message):
    payload = message.payload.decode()
    try:
        # Attempt to convert the payload to a float
        temperature = float(payload)
        print(f"Received temperature: {temperature}°C")
    except ValueError:
        # Ignore non-numeric payloads (e.g., LWT message)
        pass

# Initialize the MQTT client
client = mqtt.Client("TemperatureSubscriber")

# Set the callback function for message reception
client.on_message = on_message

# Enable logging (optional)
# client.on_log = lambda client, userdata, level, buf: print(f"Log: {buf}")

# Connect to the MQTT broker
client.connect(broker, port)

# Subscribe to the temperature topic
client.subscribe(topic)

# Start the MQTT client loop to process messages
client.loop_forever()