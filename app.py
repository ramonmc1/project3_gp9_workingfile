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
    

# @app.route("/page2")
# def home():
#     destination_data = mongo.db.parks_small.find_one()
      
#     return render_template("index2.html", campx=destination_data)

# /////////in html
#    {% for name in campx %}
#           <li>{{ name }}</li>
#           {% endfor %}
# ////////


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
    
    camp_datai = [{
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
    }]
    print(camp_datai)
    return render_template("index2.html", campi=camp_datai)


@app.route("/campdata/api2/<code>")
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
    
    camp_datax = [{
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
    }]
 
    return jsonify(camp_datax)





@app.route("/test")
def test():
    lat = [40, 50]
    lon = [-90, -110]
    Name = ["test1", "test2"]
    PCode = ["abcd", "dcba"]
    
    test_data = [{
        "lat": lat,
        "lon": lon,
        "Name": Name,
        "PCode": PCode,      
    }]

    return jsonify(test_data)

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

# @app.route("/api/camps")
# def pals():
    
#     results = mongo.db.parks_small.find_one()
#     Name = [result for result in results["Name"]]
#     lat = [result for result in results["Latitude"]]
#     lon = [result for result in results["Longitude"]]
#     URL = [result for result in results["URL"]]
#     City = [result for result in results["City"]]
#     ZipCode = [result for result in results["ZipCode"]]
#     PCode = [result for result in results["PCode"]]
#     Desc = [result for result in results["Description"]]
    
#     camp_data = [{
#         "lat": lat,
#         "lon": lon,
#         "Name": Name,
#         "PCode": PCode,
#         "ZipCode":ZipCode,
#         "URL": URL,
#         "City": City,
#         "Description": Desc,
#         ""
#         "marker": {
#             "size": 50,
#             "line": {
#                 "color": "rgb(8,8,8)",
#                 "width": 1
#             },
#         }
#     }]

#     return jsonify(camp_data)


if __name__ == "__main__":
    app.run(debug=True)

