---
lang: it
layout: page
title: Mappa tamponi Toscana
js:
  - "/js/Autolinker.min.js"

---

(Fonti: )

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css"
  integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A=="
  crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"
  integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA=="
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

<div id="map"></div>

<script>

window.onload = function() {
var vialMarker = L.AwesomeMarkers.icon({
icon: 'vial',
prefix: 'fa',
markerColor: 'red'
});

var markerList=[];
{% for member in site.data.machgen.mappe.Toscana.tamponi %}
{% if member.LATITUDINE != blank and member.LONGITUDINE != blank %}
markerList.push([{{member.LATITUDINE}}, {{member.LONGITUDINE}}, "{{member.USL|uri_escape}}", "{{member.DOVE|uri_escape}}", "{{member.ORARI|uri_escape}}", "{{member['NOTE SUL SERVIZIO']|uri_escape}}"]);
{% endif %}
{% endfor %}

// initialize the map
var map = L.map('map');

// create the tile layer with correct attribution
var osmUrl='{{site.tile_map}}';
var osmAttrib='&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, Tiles courtesy of <a href="http://leafletjs.com/" target="_blank">Leaflet</a>';
var osm = new L.TileLayer(osmUrl, {minZoom: 6, maxZoom: 19, attribution: osmAttrib});


var sumLat = 0.;
var sumLon = 0.;
var countMarkers=0;

markers = L.markerClusterGroup();

for (var i=0; i<markerList.length; i++) {
    var lat = markerList[i][0];
    var lon = markerList[i][1];
    var popupUSL = markerList[i][2];
    var popupDOVE = markerList[i][3];
    var popupORARI = markerList[i][4];
    var popupNOTE = markerList[i][5];

    // Raccolte fondi, Supporto psicologico, Servizi e iniziative solidali pubbliche, Servizi e iniziative solidali private, Richiesta aiuto

    if (!isNaN(lat) && !isNaN(lon)) {
        var markerLocation = new L.LatLng(lat, lon);

        var marker = new L.Marker(markerLocation, { icon: vialMarker} );
        markerText="<h2>"+decodeURI(popupDOVE)+"</h2>";
        markerText+="<table>";
        if (popupUSL) {
            markerText+="<tr><td>USL</td><td>"+decodeURI(popupUSL)+"</td></tr>";
        }
        if (popupORARI) {
            markerText+="<tr><td>ORARI</td><td>"+decodeURI(popupORARI)+"</td></tr>";
        }
        if (popupNOTE) {
            markerText+="<tr><td>NOTE</td><td>"+decodeURI(popupNOTE)+"</td></tr>";
        }
        markerText+="</table>";

        marker.bindPopup(Autolinker.link(markerText, newWindow=true));

        markers.addLayer(marker);

        sumLat += lat;
        sumLon += lon;
        countMarkers++;
    }
}


map.addLayer(markers);
map.addLayer(osm).setView([sumLat / countMarkers, sumLon / countMarkers], 7);
}

</script>

