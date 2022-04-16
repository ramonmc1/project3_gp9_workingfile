from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import camp_scrape

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/camp_project")

datacamp_dict = camp_scrape.scrape_info()
mongo.db.parks_nps.update_one({}, {"$set": datacamp_dict}, upsert=True)

# Route to render index.html template using data from Mongo

@app.route("/")
def home():
    destination_data = mongo.db.parks_nps.find_one()
      
    return render_template("index.html", camp=destination_data)
    
#api to get the camp data and weather condition for a single campsite
@app.route("/campdata/<code>")
def page2(code):
    destination_data2 = mongo.db.parks_nps.find_one()
    Namei = []
    Desci = []
    URLi = []
    Zipcodei = []
    Lati = []
    Loni=[]
    PCodei = []
    Imagesi = []
    Images_titlei = []
    Images_capi = []
    Weather_infoi = []
    Costi = []
    Cost_symboli = []
    OperHoursi = []
    directionsi = []

    searchid = code
    for index in range(len(destination_data2["PCode"])):
        if destination_data2["PCode"][index] ==searchid:
            Namei.append(destination_data2["Name"][index])
            PCodei.append(destination_data2["PCode"][index])
            Desci.append(destination_data2["Description"][index])
            URLi.append(destination_data2["URL"][index])
            Zipcodei.append(destination_data2["ZipCode"][index])
            Lati.append(destination_data2["Latitude"][index])
            Loni.append(destination_data2["Longitude"][index])
            Imagesi.append(destination_data2["Images"][index])
            Images_titlei.append(destination_data2["Image_title"][index])
            Images_capi.append(destination_data2["Caption"][index])
            Weather_infoi.append(destination_data2["Weather_info"][index])
            Costi.append(destination_data2["Cost"][index])
            Cost_symboli.append(destination_data2["Cost_range"][index])
            OperHoursi.append(destination_data2["Hours"][index])
            directionsi.append(destination_data2["Directions"][index])
    zip = Zipcodei[0]
    weather_dict = camp_scrape.weather_info(zip)
    mongo.db.weather_nps.update_one({}, {"$set": weather_dict}, upsert=True)
    camp_datai = {
         "lat": Lati[0],
         "lon": Loni[0],
         "Name": Namei[0],
         "PCode": PCodei[0],
         "ZipCode":Zipcodei[0],
         "URL": URLi[0],
         "Description": Desci[0],
         "Image":Imagesi[0],
         "Image_title": Images_titlei[0],
         "Caption":Images_capi[0],
         "Weather_info": Weather_infoi[0],
         "Cost":Costi[0],
         "Cost_range":Cost_symboli[0],
         "Hours":OperHoursi[0],
         "Directions":directionsi[0],
         "Temp": weather_dict["Temp"],
         "Humidity": weather_dict["Humidity"],
         "Cloudiness": weather_dict["Cloudiness"],
         "Wind_Speed": weather_dict["Wind_Speed"],
         "Date": weather_dict["Date"],
         "City": weather_dict["City"],
         "marker": {
             "size": 50,
             "line": {
                 "color": "rgb(8,8,8)",
                 "width": 1
             },
         }
    }   
    mongo.db.parks_nps_individual.update_one({}, {"$set": camp_datai}, upsert=True)
    return render_template("index2.html", data=camp_datai)
   
#This api call an 'individual campsite' from the mongodb for the marker and popup information
@app.route("/campdata/api2")
def campi():    
    
    results = mongo.db.parks_nps_individual.find_one()
    camp_dataii = [{
        "lat": results["lat"],
        "lon": results["lon"],
        "Name": results["Name"],
        "PCode": results["PCode"],
        "ZipCode":results["ZipCode"],
        "URL": results["URL"],
        "Description": results["Description"], 
        "Cost": results["Cost"],
        "Hours": results["Hours"],
        "marker": {
            "size": 50,
            "line": {
                "color": "rgb(8,8,8)",
                "width": 1
            },
        }
    }] 
    return jsonify(camp_dataii)

@app.route("/api/camps")
def camp_data():
    
    results = mongo.db.parks_nps.find_one()
    Name = [result for result in results["Name"]]
    lat = [result for result in results["Latitude"]]
    lon = [result for result in results["Longitude"]]
    URL = [result for result in results["URL"]]
    City = [result for result in results["City"]]
    ZipCode = [result for result in results["ZipCode"]]
    PCode = [result for result in results["PCode"]]
    Desc = [result for result in results["Description"]]
    Cost = [result for result in results["Cost"]]
    Cost_range = [result for result in results["Cost_range"]]

    camp_data = [{
        "lat": lat,
        "lon": lon,
        "Name": Name,
        "PCode": PCode,
        "ZipCode":ZipCode,
        "URL": URL,
        "City": City,
        "Description": Desc,
        "Cost": Cost,
        "Cost_range":Cost_range,
   
    }]

    return jsonify(camp_data)


if __name__ == "__main__":
    app.run(debug=True)
