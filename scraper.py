import requests
import pandas as pd
from datetime import datetime, timedelta

def fetch_flight_data():
    url = "https://opensky-network.org/api/states/all"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        columns = ["icao24", "callsign", "origin_country", "time_position", "last_contact",
                   "longitude", "latitude", "baro_altitude", "on_ground", "velocity",
                   "true_track", "vertical_rate", "sensors", "geo_altitude", "squawk",
                   "spi", "position_source"]
        df = pd.DataFrame(data["states"], columns=columns)
        df["time_fetched"] = datetime.utcnow()
        return df
    else:
        return pd.DataFrame()  # Return empty DataFrame if request fails
