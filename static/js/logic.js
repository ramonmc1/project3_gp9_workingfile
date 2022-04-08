function campMap(){

const url = "/api/camps";


d3.json(url).then(function(data) {
       
  console.log(data[0].Name.length);
for (var i = 0; i < data[0].Name.length; i++) {
     L.marker([data[0].lat[i], data[0].lon[i]]).bindPopup("<h1>" + data[0].Name[i] + "</h1>").addTo(myMap);
}
  
  });

var myMap = L.map("map", {
  center: [40, -98],
  zoom: 4
});


// the tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

};

campMap();
