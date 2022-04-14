
//Using JQuery to get the lat/long from the html page (attributes) to establish the map position
// // let zipq = document.querySelector(`[data-info1]`);
// $(window).on("resize", function () { $("#map2").height($(window).height()-40); map.invalidateSize(); }).trigger("resize");

let Latq = document.querySelector(`[data-infolat]`);
let Lonq= document.querySelector(`[data-infolon]`);

let lat = Latq.dataset.infolat;
let lon = Lonq.dataset.infolon;


var latlong = [lat, lon];

//getting the data from the flask server api (@app.route("/campdata/api2"))
function campMapx(){
const url = 'http://127.0.0.1:5000/campdata/api2';

//creating a marker with link to external website
d3.json(url).then(function(data) {  
L.marker([data[0].lat, data[0].lon]).bindPopup("<b>Name: </b>" + data[0].Name + 
     "<br>"+ "$"+ data[0].Cost+ "<br>"+"<a href="+data[0].URL+"><b>Webpage</b></a>").addTo(myMap);
});

//This is updated based on the jQuery latlon
let myMap = L.map("map2", {
  center: latlong,
  zoom: 6
});

// the tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

};

campMapx();
