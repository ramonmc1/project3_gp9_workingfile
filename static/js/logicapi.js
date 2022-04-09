function campMapx(xxxx){

  var = xxxxx
 
 const url = "/campdata/api2/var";
 
 d3.json(url).then(function(data) {
       
console.log(data);


for (var i = 0; i < data[0].Name.length; i++) {
     L.marker([data[0].lat[i], data[0].lon[i]]).bindPopup("<b>Name: </b>" + data[0].Name[i] + "<br><b>City: </b>"+ data[0].City[i]+
     "<br>"+ "<a href=campdata/"+ data[0].PCode[i]+"><b>Get More Details</b></a>").addTo(myMap);
}
  
 });

var myMap = L.map("map", {
  center: [40, -98],
  zoom: 12
});


// the tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

};

campMapx();
