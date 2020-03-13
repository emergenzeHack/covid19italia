---
layout: page
title: Segnalazioni
permalink: /issues/
---
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
   integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
   crossorigin=""/>

   <!-- Make sure you put this AFTER Leaflet's CSS -->
 <script src="https://unpkg.com/leaflet@1.6.0/dist/leaflet.js"
   integrity="sha512-gZwIG9x3wUXg2hdXF6+rVkLF/0Vi9U8D2Ntg4Ga5I5BZpVkVxlJWbSQtXPSiUTtC0TjtGOmxa1AJPuV0CPthew=="
   crossorigin=""></script>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css" />
<script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.min.js"></script>

<link rel="stylesheet" href="https://unpkg.com/leaflet.markercluster@1.4.1/dist/MarkerCluster.css"
   crossorigin=""/>

<link rel="stylesheet" href="https://unpkg.com/leaflet.markercluster@1.4.1/dist/MarkerCluster.Default.css"
   crossorigin=""/>

 <script src="https://unpkg.com/leaflet.markercluster@1.4.1/dist/leaflet.markercluster.js"
   crossorigin=""></script>

<style>
#map{ height: 600px }
</style>

{% assign categorieissue = "Raccolte fondi;Raccolte fondi,Notizie;Notizie,Servizi e iniziative solidali;Servizi e iniziative solidali,Iniziative culturali e ricreative;Attivita culturali e ricreative,Consegne e commissioni;Consegne e commissioni,Supporto psicologico;Supporto psicologico" | split: "," %}


<div class="row">
<div class="text-center">
{% for categoriatuple in categorieissue %}
{% assign categoria = categoriatuple | split: ";" %}
  <span class="col-xs-12 col-sm-6">
	  <a href="#{{categoria[0] | slugify}}" class="btn btn-success btn-lg col-xs-12 mb-15" role="button">{{categoria[0]}}</a>
	</span>
{% endfor %}
</div>
</div>



<div class="row"><div class="col-md-12 col-sm-12 col-xs-12"> <div id="map" style="height: 600px;"></div> </div> </div>

{% for categoriatuple in categorieissue %}
{% assign categoria = categoriatuple | split: ";" %}
---
# {{categoria[0]}}
<div class="panel-group">
{% assign filteredissues = site.data.issuesjson | where: "state","open" | where_exp: "member","member.issue.labels contains categoria[1]" %}
{% for member in filteredissues %}
<div class="panel-body issuepanel" id="issue{{member.number}}">
<div class="list-group-item">
<a href="{{site.url}}/issues/{{member.number}}"><h4 class="list-group-item-heading">{{member.title}}</h4></a>
<dl class="row">
{% for item in member.issue.data %}
{% if item[1] != blank %}
<dt class="col-sm-3">{{item[0] | replace: "_", " " | capitalize_all}}</dt>
<dd class="col-sm-9">{{item[1] | newline_to_br | auto_link}}</dd>
{% endif %}
{% endfor %}
</dl>
</div>
{% include social-share-issue.html %}
</div>
{% endfor %}
</div>
{% endfor %}


{% assign filteredissues = site.data.issuesjson | where: "state","open" "%}
<script>
var markerList=[];
{% for member in filteredissues %}
{% if member.issue.data.Posizione != blank %}
{% assign coordinate = member.issue.data.Posizione | split: ' ' %}
markerList.push([{{coordinate[0]}}, {{coordinate[1]}}, "{{member.title|uri_escape}}", "{{ member.number }}", ""]);
{% endif %}
{% endfor %}

var alloggiMarker = L.AwesomeMarkers.icon({
icon: 'home',
prefix: 'fa',
markerColor: 'green'
});
var fabbisogniMarker = L.AwesomeMarkers.icon({
icon: 'child',
prefix: 'fa',
markerColor: 'blue'
});
var notizieutiliMarker = L.AwesomeMarkers.icon({
icon: 'newspaper-o',
prefix: 'fa',
markerColor: 'orange'
});
var donazioniMarker = L.AwesomeMarkers.icon({
icon: 'handshake-o',
prefix: 'fa',
markerColor: 'red'
});
var raccoltefondiMarker = L.AwesomeMarkers.icon({
icon: 'money',
prefix: 'fa',
markerColor: 'blue'
});

// initialize the map
var map = L.map('map')

// create the tile layer with correct attribution
var osmUrl='{{site.tile_map}}';
var osmAttrib='&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, Tiles courtesy of <a href="http://hot.openstreetmap.org/" target="_blank">Humanitarian OpenStreetMap Team</a>';
var osm = new L.TileLayer(osmUrl, {minZoom: 5, maxZoom: 19, attribution: osmAttrib});


var sumLat = 0.;
var sumLon = 0.;

markers = L.markerClusterGroup();

for (var i=0; i<markerList.length; i++) {
    var lat = markerList[i][0];
    var lon = markerList[i][1];
    var popupText = markerList[i][2];
    var popupURL = markerList[i][3];
    var type = markerList[i][4]

        if (!isNaN(lat) && !isNaN(lon)) {
            var markerLocation = new L.LatLng(lat, lon);
            var marker = new L.Marker(markerLocation);

            markers.addLayer(marker);

            marker.bindPopup("<a href=\"" + popupURL + "\">" + decodeURI(popupText) + "</a>");

            sumLat += lat;
            sumLon += lon;
        }
}

map.addLayer(markers);

map.addLayer(osm).setView([42.629381, 13.288372], 5);

function getFeaturesInView() {
    var features = [];
    for (var i=0; i<markerList.length; i++) {
            if(map.getBounds().contains(L.latLng(markerList[i][0],markerList[i][1]))) {
            features.push(markerList[i]);
            }
            }
    return features;
}

function setVisible(element) {
    $("#issue"+element[3]).show();
}

function onMoveEnd(evt) {
    $(".issuepanel").hide()
    inView=getFeaturesInView();
    inView.forEach(setVisible); 
}

map.on('moveend', onMoveEnd);
console.log("moveend");

//var geocoder = L.Control.geocoder({collapsed:false,placeholder:"Cerca...",
//        defaultMarkGeocode: false, geocodingQueryParams: { countrycodes: "it" },
//        })
//.on('markgeocode', function(e) {
//        var latlon=e.geocode.center;
//        $("#lat").html(latlon.lat);
//        $("#lng").html(latlon.lng);
//        var marker = new L.Marker(markerLocation);
//        map.addLayer(marker);
//        })
//.addTo(map);


</script>
