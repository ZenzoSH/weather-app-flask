from flask import Flask, render_template, request , redirect
import requests
import time
import datetime


app = Flask(__name__)





@app.route("/", methods=["GET", "POST"])
def weather():
    if request.method == "POST":
       city = request.form["city"].upper()
    
    else:
        city ="Varanasi"
        

 
    API_KEY = "4326c3105140cc48cc2c6f9e2318ad23"
    URL_BASE = "https://api.openweathermap.org/data/2.5/weather"
    GEO_BASE_URL = "http://api.openweathermap.org/geo/1.0/direct"
    

    
    geoURL = f"{GEO_BASE_URL}?q={city}&appid={API_KEY}"   
    
            
            
    response_geo = requests.get(geoURL)


    if response_geo.status_code ==200:
                data1 =  response_geo.json()
                lat = data1[0]["lat"]
                lon = data1[0]["lon"]
    else:
        return redirect("/")   # if the search box is submitted empty then the page reloads

        

    mainURL=f"{URL_BASE}?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

    response_main = requests.get(mainURL)
    if response_main.status_code ==200:
                data1 = response_main.json()
    else:
        print("MAIN ERROR OCCURED ")
    
            
            
            
        

    data = { 
            "icon" : str(data1["weather"][0]["icon"]),
            "weather" : str(data1["weather"][0]["description"].capitalize()),   # overcast clouds
            "overall_weather"  :str(data1["weather"][0]["main"].capitalize()),   #  clouds
            "temperature" :str( data1["main"]["temp"]),  #temp
            "feels_like" :str( data1["main"]["feels_like"]),
            "sunrise"   :   datetime.datetime.fromtimestamp(data1["sys"]["sunrise"]).strftime('%Y-%m-%d %H:%M').split()[-1],
            "sunset" :   time.strftime('%Y-%m-%d %H:%M', time.localtime(data1["sys"]["sunset"])).split()[-1],
            "country" : data1["sys"]["country"],
            "humidity": str( data1["main"]["humidity"])
            }

    return  render_template("index.html" , data =data , city =city)
            

    
    




if __name__ == "__main__":
    app.run(debug=True)