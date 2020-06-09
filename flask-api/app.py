import json
import requests
from flask_cors import CORS
import pandas as pd
import os
from flask import Flask, jsonify, json, request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)

def realtime_simulation():
    df = pd.read_excel('streaming_sample500.xlsx','streaming_sample500')
    #df.pop('Vehicle Present')
    df.columns = ["Area", "O_BetweenStreet1", "O_BetweenStreet2", "DewPointC", "DurationSeconds", "Hourly_Counts", "Sensor_Id", "Sensor_Name", "Side_Of_Street", "StreetId", "StreetName", "Time", "WindChillC", "WindGustKmph", "cloudcover", "humidity", "moon_illumination", "pressure", "tempC", "traffic_count", "winddirDegree", "windspeedKmph"]
    df = df.sample()
    out = df.to_json(orient='records')[1:-1].replace('},{', '} {')
    return out

@app.route("/")
def main():
    return realtime_simulation()

port = os.getenv('VCAP_APP_PORT', '8080')
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=port)
