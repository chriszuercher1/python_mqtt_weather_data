import time
import requests
from datetime import datetime

def get_most_recent_air_temperature():
    url = f"https://tecdottir.herokuapp.com/measurements/tiefenbrunnen?sort=timestamp_cet%20desc&limit=5"
    response = requests.get(url)
    data = response.json()

    if data["ok"] and len(data["result"]) > 0:
        # Assuming the most recent entry is the first in the sorted list
        most_recent_entry = data["result"][0]
        air_temperature = most_recent_entry["values"]["air_temperature"]["value"]
        return air_temperature
    else:
        return None

while True:
    air_temperature = get_most_recent_air_temperature()
    if air_temperature is not None:
        print(f"Publish air temperature: {air_temperature}°C")
    else:
        print("No data available.")
    
    time.sleep(1)
