from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import camp_scrape

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/camp_small")


# Route to render index.html template using data from Mongo

@app.route("/")
def home():
    destination_data = mongo.db.parks_small.find_one()
      
    return render_template("index.html", camp=destination_data)
    


@app.route("/campdata/<code>")
def page2(code):
    destination_data2 = mongo.db.parks_small.find_one()
    Namei = []
    Desci = []
    URLi = []
    Zipcodei = []
    Lati = []
    Loni=[]
    PCodei = []
    index=0
    searchid = code
    for index in range(len(destination_data2["PCode"])):
        if destination_data2["PCode"][index] ==searchid:
            print("Victory..partial...time for workout")
            print(index)
            Namei.append(destination_data2["Name"][index])
            PCodei.append(destination_data2["PCode"][index])
            Desci.append(destination_data2["Description"][index])
            URLi.append(destination_data2["URL"][index])
            Zipcodei.append(destination_data2["ZipCode"][index])
            Lati.append(destination_data2["Latitude"][index])
            Loni.append(destination_data2["Longitude"][index])
    
    camp_datai = {
         "lat": Lati[0],
         "lon": Loni[0],
        "Name": Namei[0],
         "PCode": PCodei[0],
         "ZipCode":Zipcodei[0],
         "URL": URLi[0],
         "Description": Desci[0],
         "marker": {
             "size": 50,
             "line": {
                 "color": "rgb(8,8,8)",
                 "width": 1
             },
         }
    }
    
    mongo.db.parks_individual.update_one({}, {"$set": camp_datai}, upsert=True)
    print (camp_datai)
    return render_template("index2.html", data=camp_datai)
    # return render_template("index2.html", campi=camp_datai)

@app.route("/campdata/api2")
def campi():    
    
    results = mongo.db.parks_individual.find_one()

    Name = results["Name"]
    lat = results["lat"]
    lon = results["lon"]
    URL = results["URL"]
    ZipCode = results["ZipCode"]
    PCode = results["PCode"]
    Desc = results["Description"]
    
    camp_dataii = [{
        "lat": lat,
        "lon": lon,
        "Name": Name,
        "PCode": PCode,
        "ZipCode":ZipCode,
        "URL": URL,
        "Description": Desc,
       
        "marker": {
            "size": 50,
            "line": {
                "color": "rgb(8,8,8)",
                "width": 1
            },
        }
    }]
    print(camp_dataii)
    return jsonify(camp_dataii)


@app.route("/api/camps")
def pals():
    
    results = mongo.db.parks_small.find_one()
    Name = [result for result in results["Name"]]
    lat = [result for result in results["Latitude"]]
    lon = [result for result in results["Longitude"]]
    URL = [result for result in results["URL"]]
    City = [result for result in results["City"]]
    ZipCode = [result for result in results["ZipCode"]]
    PCode = [result for result in results["PCode"]]
    Desc = [result for result in results["Description"]]
    
    camp_data = [{
        "lat": lat,
        "lon": lon,
        "Name": Name,
        "PCode": PCode,
        "ZipCode":ZipCode,
        "URL": URL,
        "City": City,
        "Description": Desc,
        ""
        "marker": {
            "size": 50,
            "line": {
                "color": "rgb(8,8,8)",
                "width": 1
            },
        }
    }]

    return jsonify(camp_data)



# Route that will trigger the scrape function
@app.route("/upload")
def scrape():

    # Run the scrape function
    datacamp_dict = camp_scrape.scrape_info()

    # Insert the record
    mongo.db.parks_small.update_one({}, {"$set": datacamp_dict}, upsert=True)

    # Redirect back to home page
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)



            # <!-- <a data-name="link" data-size="small" data-color="green"></a>
            # <a class="test" data-name="link" data-size="small"></a>
            # <h3>Zip: {{campi[0].ZipCode}}</h3>
            # <h3 data-pcode ="1">{{campi[0].PCode}}</h3>
            # <h3 data-lat ="2">{{campi[0].lat}}</h3>
            # <p>{{campi[0].lat, campi[0].lon}} -->