# Dependencies
import pandas as pd
import requests
from splinter import Browser
import html5lib
import time
import pymongo
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
    
    
    for camp in datacamp["data"]:
        Name.append(camp["fullName"])
        URL.append(camp["url"])
        Desc.append(camp["description"])
        Lat.append(camp["latitude"])
        Long.append(camp["longitude"])
        City.append(camp["addresses"][0]["city"])
        zipcode.append(camp["addresses"][0]["postalCode"])
        parkCode.append(camp["parkCode"])
    # Loop through the list of cities and perform a request for data on each


    camp_dict = {
    "PCode": parkCode,
    "Name": Name,
    "Latitude": Lat,
    "Longitude":Long,
    "URL": URL,
    "Description":Desc,
    "City":City,
    "ZipCode": zipcode
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








