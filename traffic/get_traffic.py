import requests
import json
import os
from config.config_loader import get_config

def get_traffic_data():
    config = get_config()
    api_key = config["mapmyindia_api_key"]
    lat = config["latitude"]
    lng = config["longitude"]
    
    url = f"https://apis.mapmyindia.com/advancedmaps/v1/{api_key}/traffic?lat={lat}&lng={lng}"
    try:
        response = requests.get(url)
        data = response.json()
        
        with open("traffic/dummy_data.json", "w") as f:
            json.dump(data, f, indent=2)
        
        congestion = data.get("results", [{}])[0].get("congestion", "Moderate")
        message = f"Current traffic congestion near your location is {congestion}."
        return message
    except Exception as e:
        return "Failed to retrieve traffic data."
