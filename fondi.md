---
layout: page
title: Raccolte Fondi
permalink: /fondi/
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
<style>
#map{ height: 600px }
</style>

<link rel="stylesheet" href="{{ site.url }}/css/Control.Geocoder.css" />
<script src="{{ site.url }}/js/Control.Geocoder.js"></script>

<div class="row"><div class="col-md-12"> <div id="map"></div> </div> </div>
<div class="row"><div class="col-md-4">Latitudine</div><div class="col-md-4" id="lat"></div></div>
<div class="row"><div class="col-md-4">Longitudine</div><div class="col-md-4" id="lng"></div></div>

<div class="panel-group">
{% assign filteredissues = site.data.issuesjson | where: "state","open" | where_exp: "member","member.issue.labels contains 'Raccolte fondi'"%}

{% assign filteredissuesbyregione = filteredissues | group_by:"issue.data.regione" %}

<ul>
{% for membergroup in filteredissuesbyregione %}
<li><a href="#{{membergroup.name}}">Regione: {{membergroup.name}}</a></li>
{% endfor %}
</ul>

{% for membergroup in filteredissuesbyregione %}
<h2 id="{{membergroup.name}}">Regione: {{membergroup.name}}</h2>
{% for member in membergroup.items %}
<div class="panel-body">
<div class="list-group-item">
<a href="/issues/{{ member.number | datapage_url: '.' }}">
		<h4 class="list-group-item-heading">{{member.title}}</h4>
</a>
                <dl class="row">
                <dt class="col-sm-3">Chi</dt>
                <dd class="col-sm-9">{{member.issue.data.chi}}</dd>
                <dt class="col-sm-3">Destinatari</dt>
                <dd class="col-sm-9">{{member.issue.data.destinatari}}</dd>
                {% if member.issue.data.contatti != blank %}
                <dt class="col-sm-3">Contatti</dt>
                <dd class="col-sm-9">{{member.issue.data.contatti}}</dd>
                {% endif %}
                {% if member.issue.data.fonte != blank %}
                <dt class="col-sm-3">Fonte</dt>
                <dd class="col-sm-9"><small><a href="{{member.issue.data.fonte}}">{{member.issue.data.fonte}}</a></small></dd>
                {% endif %}
                {% if member.issue.data.regione != blank %}
                <dt class="col-sm-3">Regione</dt>
                <dd class="col-sm-9">{{member.issue.data.regione}}</dd>
                {% endif %}
                {% if member.issue.data.provincia != blank %}
                <dt class="col-sm-3">Provincia</dt>
                <dd class="col-sm-9">{{member.issue.data.provincia}}</dd>
                {% endif %}
                {% if member.issue.data.comune != blank %}
                <dt class="col-sm-3">Comune</dt>
                <dd class="col-sm-9">{{member.issue.data.comune}}</dd>
                {% endif %}
                </dl>
                <p class="list-group-item-text">{{member.issue.data.descrizione|markdownify}}</p>
                <p class="list-group-item-text">{{member.issue.data.data}}</p>
                </div>
<div class="panel-footer">
<ul class="share-buttons">
  <li>Condividi:</li>
  <li><a href="https://www.covid19italia.info/issues/{{ member.number | datapage_url: '.' }}" title="Copia link"><img alt="Copia link" src="/img/icone/link.png"></a></li>
  <li><a href="https://www.facebook.com/sharer/sharer.php?u=https://www.covid19italia.info/issues/{{ member.number | datapage_url: '.' }}&title={{member.title|truncate:70|uri_escape}} | {{ site.title }}" title="Condividi su Facebook" target="_blank"><img alt="Condividi su Facebook" src="/img/icone/Facebook.png"></a></li>
  <li><a href="https://twitter.com/intent/tweet?url=https://www.covid19italia.info/issues/{{ member.number | datapage_url: '.' }}&text={{member.title|truncate:50|uri_escape}}&via=terremotocentro&hashtags=terremotocentroitalia" target="_blank" title="Tweet"><img alt="Tweet" src="/img/icone/Twitter.png"></a></li>
 <li><a href="https://plus.google.com/share?url=https://www.covid19italia.info/issues/{{ member.number | datapage_url: '.' }}" target="_blank" title="Condividi su Google+"><img alt="Condividi su Google+" src="/img/icone/Google+.png"></a></li>
 <li><a data-proofer-ignore href="mailto:?subject={{member.title|truncate:70|uri_escape}} | {{site.title}}&body={{member.title|truncate:70|uri_escape}}%20Clicca qui:%20https://www.covid19italia.info/issues/{{ member.number | datapage_url: '.' }}" title="Invia email"><img alt="Invia email" src="/img/icone/Email.png"></a></li>
</ul>
</div>
</div>
{% endfor %}
{% endfor %}
</div>


<script>
var markerList=[];
{% for member in filteredissues %}
console.log("{{member.issue.data.Posizione}}");
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
var osmAttrib='&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, Tiles courtesy of <a href="http://leafletjs.com/" target="_blank">Leaflet</a>';
var osm = new L.TileLayer(osmUrl, {minZoom: 5, maxZoom: 19, attribution: osmAttrib});


var sumLat = 0.;
var sumLon = 0.;

for (var i=0; i<markerList.length; i++) {
    var lat = markerList[i][0];
    var lon = markerList[i][1];
    var popupText = markerList[i][2];
    var popupURL = markerList[i][3];
    var type = markerList[i][4]

        if (!isNaN(lat) && !isNaN(lon)) {
            var markerLocation = new L.LatLng(lat, lon);
            var marker = new L.Marker(markerLocation);

            map.addLayer(marker);

            marker.bindPopup("<a href=\"" + popupURL + "\">" + decodeURI(popupText) + "</a>");

            sumLat += lat;
            sumLon += lon;
        }
}

map.addLayer(osm).setView([42.629381, 13.288372], 5);
var geocoder = L.Control.geocoder({collapsed:false,placeholder:"Cerca...",
        defaultMarkGeocode: false, geocodingQueryParams: { countrycodes: "it" },
        })
.on('markgeocode', function(e) {
        var latlon=e.geocode.center;
        $("#lat").html(latlon.lat);
        $("#lng").html(latlon.lng);
        var marker = new L.Marker(markerLocation);
        map.addLayer(marker);
        })
.addTo(map);

</script>
