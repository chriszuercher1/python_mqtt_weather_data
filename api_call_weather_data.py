import time
import requests
from datetime import datetime

def get_most_recent_air_temperature():
    current_date = datetime.now().strftime("%Y-%m-%d")
    url = f"https://tecdottir.herokuapp.com/measurements/tiefenbrunnen?startDate={current_date}&sort=timestamp_cet%20desc&limit=500&offset=0"
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
