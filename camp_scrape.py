# Dependencies
import pandas as pd
import requests
from splinter import Browser
from config import api_key
from config import weath_key
import urllib.request, json

def scrape_info():

    
    camp_url = "https://developer.nps.gov/api/v1/parks?limit=600&stateCode=&"
    query_url = f"{camp_url}api_key={api_key}"

    response = urllib.request.urlopen(query_url).read()
    datacamp = json.loads(response.decode('utf-8'))
    Name = []
    URL = []
    Desc =[]
    Lat = []
    Long = []
    City = []
    zipcode = []
    parkCode = []
    Images = []
    Images_title = []
    Images_cap = []
    Weather_info = []
    Cost = []
    Cost_symbol = []
    OperHours = []
    directions = []
    
    for camp in datacamp["data"]:
        Name.append(camp["fullName"])
        URL.append(camp["url"])
        Desc.append(camp["description"])
        Lat.append(camp["latitude"])
        Long.append(camp["longitude"])
        City.append(camp["addresses"][0]["city"])
        directions.append(camp["directionsInfo"])
        zipcode.append(camp["addresses"][0]["postalCode"])
        parkCode.append(camp["parkCode"])
        Images.append(camp["images"][0]["url"])
        Images_title.append(camp["images"][0]["title"])
        Images_cap.append(camp["images"][0]["caption"])
        Weather_info.append(camp["weatherInfo"])
          
    for camp in datacamp["data"]:
        try:   
            fee = (camp ["entranceFees"][0]["cost"])
            
            if float(fee)> 30:
                Cost.append(fee)
                Cost_symbol.append("$$$")
            elif float(fee) >= 5:
                Cost.append(fee)
                Cost_symbol.append("$$")
            elif float(fee) < 5:
                Cost.append(fee)
                Cost_symbol.append("$")
        except:
           Cost.append('0')
           Cost_symbol.append("$")  
    
    for camp in datacamp["data"]:
        try:   
            OperHours.append(camp["operatingHours"][0]["description"])
        except:   
            OperHours.append("no information available")

    camp_dict = {
    "PCode": parkCode,
    "Name": Name,
    "Latitude": Lat,
    "Longitude":Long,
    "URL": URL,
    "Description":Desc,
    "City":City,
    "ZipCode": zipcode,
    "Images": Images,
    "Image_title": Images_title,
    "Caption":Images_cap,
    "Weather_info":Weather_info,
    "Cost":Cost,
    "Cost_range": Cost_symbol,
    "Hours": OperHours,
    "Directions": directions

    }
    
    return camp_dict


def weather_info(zip):

    Temp = [] 
    Humidity = []
    Cloudiness = [] 
    Wind_Speed = []
    Date = []
    City = []
     
    url = "http://api.openweathermap.org/data/2.5/weather?"
    units = "imperial"

    weath_url = f"{url}appid={weath_key}&units={units}&q={zip}"
    response = requests.get(weath_url).json() 
    try:
        Temp.append(response['main']['temp'])
        Humidity.append(response['main']['humidity'])
        Cloudiness.append(response['clouds']['all'])
        Wind_Speed.append(response['wind']['speed'])
        Date.append(response['dt'])
        City.append(response['name'])
    except:
        Temp.append("-")
        Humidity.append("-")
        Cloudiness.append("-")
        Wind_Speed.append("-")
        Date.append("-")
        City.append("-")
    
    weath_dict = { 
        "Temp" : Temp,
        "Humidity" : Humidity,
        "Cloudiness" : Cloudiness,
        "Wind_Speed" : Wind_Speed,
        "Date" : Date,
        "City": City
    }
    return weath_dict








