
// function getinfo (data) {
var latlong = [48.7, -99];
// let info = data.Name
// var element = $('[data-size = "link"]'),
//     size = element.data("size");

// function getData (data){

// data.forEach(element => {
//   let li = document.createElement ('li')
//     li.innerHTML = `${element.nickname} (${element.species})
//   <button class="release" data-pokemon-id+"${element.id}">Release</button>
//   `
//   let trainerDiv = document.querySelector(`[data-id="${element.trainer_id}"]`)
//   trainerDiv.append(li)

//   })
// }

let findLat = document.querySelector(`[data-info1]`);
let findLon = document.querySelector(`[data-info2]`);
lat = findLat.innerText;
lon = findLon.innerText;

// console.log(findInfo);
console.log(lon)
// let findOther = document.querySelector(`data.Name`);

// console.log(findOther);

var latlong = [lat, lon];



function campMapx(){

const url = 'http://127.0.0.1:5000/campdata/api2';
 
console.log(url);

d3.json(url).then(function(data) {
     

L.marker([data[0].lat, data[0].lon]).bindPopup("<b>Name: </b>" + data[0].Name + "<br><b>City: </b>"+ data[0].City+
     "<br>"+ "<a href="+data[0].URL+"><b>Webpage</b></a>").addTo(myMap);
  let newlatlon = [parseFloat(data[0].lat),parseFloat(data[0].lon)]
    console.log(newlatlon)
//  this.map.setView(newlatlon);
});


console.log(latlong)

let myMap = L.map("map", {
  center: latlong,
  zoom: 7
});

// the tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

};

campMapx();
// }
// getinfo();