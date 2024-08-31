import paho.mqtt.client as mqtt

# MQTT broker settings
broker = "localhost"
port = 1883
topic = "sensor/temperature"

# Callback function to handle incoming messages
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode('utf-8')} on topic {message.topic}")

# Initialize the MQTT client
client = mqtt.Client("TemperaturePublisher")

# Connect to the MQTT broker
client.connect(broker, port)

# Set the callback function
client.on_message = on_message

# Subscribe to the topic
client.subscribe(topic)

# Start the loop to process received messages
client.loop_start()

# Keep the script running to listen for incoming messages
input("Press Enter to stop...\n")

# Stop the loop and disconnect
client.loop_stop()
client.disconnect()
