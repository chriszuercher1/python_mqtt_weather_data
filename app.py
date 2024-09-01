from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import paho.mqtt.client as mqtt

# Ignore warnings
import warnings
warnings.filterwarnings("ignore")

# Create a Flask web app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'geheim'
socketio = SocketIO(app)

# IP-Address of broker
MQTT_SERVER = "localhost"

# Topics
MQTT_TEMP = "sensor/temp"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(MQTT_TEMP)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode('utf-8')
    try:
        # Attempt to convert the payload to a float
        data = float(payload)
        print(f"Received data: {data}")
        socketio.emit('mqtt_message', {'topic': topic, 'data': data})
        print(f"Emitted data: {data}")
    except ValueError:
        # Handle non-numeric payloads (e.g., LWT message)
        print(f"Received non-numeric payload: {payload}")

# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)

# Define the index route
@app.route('/')
def index():
    return render_template('chart.html')

# Start the web server
if __name__ == '__main__':
    client.loop_start()
    socketio.run(app, host='0.0.0.0', port=5000)