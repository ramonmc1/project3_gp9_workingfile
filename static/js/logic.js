function campMap() {

  const url = "/api/camps";

  d3.json(url).then(function (data) {

    var campMarkers = [];
    var lowCost = [];
    var medCost = [];
    var highCost = [];

    for (var i = 0; i < data[0].Name.length; i++) {
      // var x = data[0].parkCode   

      // if (x ==glac) {
      campMarkers.push(L.marker([data[0].lat[i], data[0].lon[i]]).bindPopup("<b>Name: </b>" + data[0].Name[i] + "<br><b>City: </b>" + data[0].City[i] +
        "<br>" + "<a href=campdata/" + data[0].PCode[i] + "><b>Get More Details</b></a>"));
    console.log(data[0].PCode[i])
      }

    for (var i = 0; i < data[0].Name.length; i++) {
      var x = data[0].Cost_range[i];
      // console.log(x);

      if (x == '$') {
        lowCost.push(L.marker([data[0].lat[i], data[0].lon[i]]).bindPopup("<b>Name: </b>" + data[0].Name[i] + "<br><b>City: </b>" + data[0].City[i] +
          "<br>" + "<a href=campdata/" + data[0].PCode[i] + "><b>Get More Details</b></a>"));
      }
      else if (x == '$$') {
        medCost.push(L.marker([data[0].lat[i], data[0].lon[i]]).bindPopup("<b>Name: </b>" + data[0].Name[i] + "<br><b>City: </b>" + data[0].City[i] +
          "<br>" + "<a href=campdata/" + data[0].PCode[i] + "><b>Get More Details</b></a>"));
      }

      else if (x =='$$$') {
        highCost.push(L.marker([data[0].lat[i], data[0].lon[i]]).bindPopup("<b>Name: </b>" + data[0].Name[i] + "<br><b>City: </b>" + data[0].City[i] +
          "<br>" + "<a href=campdata/" + data[0].PCode[i] + "><b>Get More Details</b></a>"));
      }

    }

      var campLayer = L.layerGroup(campMarkers);
      var lowCampLayer = L.layerGroup(lowCost);
      var medCampLayer = L.layerGroup(medCost);
      var highCampLayer = L.layerGroup(highCost);

      // the tile layer
      var street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      });


      var topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
      });

      var baseMaps = {
        "Street Map": street,
        "Topographic Map": topo
      };

      var overlayMaps = {
        "All Camps": campLayer,
        "$": lowCampLayer,
        "$$": medCampLayer,
        "$$$": highCampLayer
      };


      var myMap = L.map("map", {
        center: [40, -98],
        zoom: 4,
        layers: [street, campLayer]
      });

      L.control.layers(baseMaps, overlayMaps, {
        collapsed: false
      }).addTo(myMap);



    });

};

campMap();
