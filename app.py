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
      # print(destination_data)
    return render_template("index.html", camp=destination_data)
    

# Route that will trigger the scrape function
@app.route("/upload")
def scrape():

    # Run the scrape function
    datacamp_dict = camp_scrape.scrape_info()

    # Insert the record
    mongo.db.parks_small.update_one({}, {"$set": datacamp_dict}, upsert=True)

    # Redirect back to home page
    return redirect("/")

@app.route("/api/camps")
def pals():
    
    results = mongo.db.parks_small.find_one()
    Name = [result for result in results["Name"]]
    lat = [result for result in results["Latitude"]]
    lon = [result for result in results["Longitude"]]
    URL = [result for result in results["URL"]]
    City = [result for result in results["City"]]
    Desc = [result for result in results["Description"]]

    camp_data = [{

        "lat": lat,
        "lon": lon,
        "Name": Name,
        "URL": URL,
        "City": City,
        "Description": Desc,
        "marker": {
            "size": 50,
            "line": {
                "color": "rgb(8,8,8)",
                "width": 1
            },
        }
    }]

    return jsonify(camp_data)


if __name__ == "__main__":
    app.run(debug=True)

