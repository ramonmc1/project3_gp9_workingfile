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
    i=0
    
    for camp in datacamp["data"]:
        try:
            i=i+1
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
            OperHours.append(camp["operatingHours"][0]["description"])
            Weather_info.append(camp["weatherInfo"])
        except:
            print (i)
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

    url = "http://api.openweathermap.org/data/2.5/weather?"
    units = "imperial"

    weath_url = f"{url}appid={weath_key}&units={units}&q={zip}"

    response = requests.get(weath_url).json() 

    weath_dict = {
    "Max_temp":response['main']['temp_max'],
    "Min_temp":response['main']['temp_min'],
    "Humidity":response['main']['humidity'],
    "Cloudiness":response['clouds']['all'],
    "Wind_Speed":response['wind']['speed'],
    "Date":response['dt'],
    "City":response['name']
    }
    
   
    return weath_dict








