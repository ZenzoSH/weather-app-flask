# Standard library imports
import os
import time
import datetime

# Third party imports
from flask import Flask, render_template, request, redirect
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def weather():
    if request.method == "POST":
        city = request.form["city"].upper()
    else:
        city = "Varanasi"
    
    # API configuration
    API_KEY = os.getenv('OPENWEATHER_API_KEY')
    if not API_KEY:
        return "Error: API key not found. Please check .env file"
    
    URL_BASE = "https://api.openweathermap.org/data/2.5/weather"
    GEO_BASE_URL = "http://api.openweathermap.org/geo/1.0/direct"
    
    # Get coordinates
    geoURL = f"{GEO_BASE_URL}?q={city}&appid={API_KEY}"
    response_geo = requests.get(geoURL)

    if response_geo.status_code == 200:
        data1 = response_geo.json()
        lat = data1[0]["lat"]
        lon = data1[0]["lon"]
    else:
        return redirect("/")
    
    # Get weather data
    mainURL = f"{URL_BASE}?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response_main = requests.get(mainURL)
    
    if response_main.status_code == 200:
        data1 = response_main.json()
    else:
        print("MAIN ERROR OCCURRED")
    
    # Format weather data
    data = {
        "icon": str(data1["weather"][0]["icon"]),
        "weather": str(data1["weather"][0]["description"].capitalize()),
        "overall_weather": str(data1["weather"][0]["main"].capitalize()),
        "temperature": str(data1["main"]["temp"]),
        "feels_like": str(data1["main"]["feels_like"]),
       "sunrise": datetime.fromtimestamp(data1["sys"].get("sunrise")).strftime('%H:%M') if data1["sys"].get("sunrise") else "N/A",
       "sunset": datetime.fromtimestamp(data1["sys"].get("sunset")).strftime('%H:%M') if data1["sys"].get("sunset") else "N/A",
        "country": data1["sys"]["country"],
        "humidity": str(data1["main"]["humidity"])
    }

    return render_template("index.html", data=data, city=city)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
