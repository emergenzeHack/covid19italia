---
layout: page
title: Issues
permalink: /issues/
---

<div class="text-center">
	<a href="#raccolte-fondi" class="btn btn-warning btn-lg" role="button">Raccolte fondi</a>
	<a href="#servizi-e-iniziative-solidali" class="btn btn-success btn-lg" role="button">Servizi e iniziative solidali</a>
	<a href="#consegne-e-commissioni" class="btn btn-success btn-lg" role="button">Consegne e commissioni</a>
	<a href="#supporto-psicologico" class="btn btn-success btn-lg" role="button">Supporto psicologico</a>
</div>

---

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.0.0/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.0.0/dist/leaflet.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css" />
<script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.min.js"></script>
<style>
#map{ height: 400px }
</style>


<link rel="stylesheet" href="{{ site.url }}/css/Control.Geocoder.css" />
<script src="{{ site.url }}/js/Control.Geocoder.js"></script>

#<div class="row"><div class="col-md-12"> <div id="map"></div> </div> </div>
#<div class="row"><div class="col-md-4">Latitudine</div><div class="col-md-4" id="lat"></div></div>
#<div class="row"><div class="col-md-4">Longitudine</div><div class="col-md-4" id="lng"></div></div>

---
# Raccolte fondi
<div class="panel-group">
{% assign filteredissues = site.data.issuesjson | where: "state","open" | where_exp: "member","member.issue.labels contains 'Raccolte fondi'"%}
{% for member in filteredissues %}
<div class="panel-body">
<a href="{{site.url}}/issues/{{member.number}}" class="list-group-item">
	<h4 class="list-group-item-heading">{{member.title}}</h4>
	<p class="list-group-item-text">{{member.issue.data.descrizione|markdownify}}</p>
                <dl class="row">
                    {% for item in member.issue.data %}
  {% if item[1] != blank %}
  <dt class="col-sm-3">{{item[0]}}</dt>
  <dd class="col-sm-9">{{item[1]}}</dd>
  {% endif %}
  {% endfor %}
                </dl>
</a>
<div class="panel-footer">
<ul class="share-buttons">
  <li>Condividi:</li>
  <li><a href="https://www.covid19italia.help/issues/{{ member.number | datapage_url: '.' }}" title="Copia link"><img alt="Copia link" src="/img/icone/link.png"></a></li>
  <li><a href="https://www.facebook.com/sharer/sharer.php?u=https://www.covid19italia.help/issues/{{ member.number | datapage_url: '.' }}&title={{member.title|truncate:70|uri_escape}} | {{ site.title }}" title="Condividi su Facebook" target="_blank"><img alt="Condividi su Facebook" src="/img/icone/Facebook.png"></a></li>
  <li><a href="https://twitter.com/intent/tweet?url=https://www.covid19italia.help/issues/{{ member.number | datapage_url: '.' }}&text={{member.title|truncate:50|uri_escape}}&via=terremotocentro&hashtags=terremotocentroitalia" target="_blank" title="Tweet"><img alt="Tweet" src="/img/icone/Twitter.png"></a></li>
 <li><a href="https://plus.google.com/share?url=https://www.covid19italia.help/issues/{{ member.number | datapage_url: '.' }}" target="_blank" title="Condividi su Google+"><img alt="Condividi su Google+" src="/img/icone/Google+.png"></a></li>
 <li><a data-proofer-ignore href="mailto:?subject={{member.title|truncate:70|uri_escape}} | {{site.title}}&body={{member.title|truncate:70|uri_escape}}%20Clicca qui:%20https://www.covid19italia.help/issues/{{ member.number | datapage_url: '.' }}" title="Invia email"><img alt="Invia email" src="/img/icone/Email.png"></a></li>
</ul>
</div>
</div>
{% endfor %}
</div>

---
# Servizi e iniziative solidali
<div class="panel-group">
{% assign filteredissues = site.data.issuesjson | where: "state","open" | where_exp: "member","member.issue.labels contains 'Servizi e iniziative solidali private' or member.issue.labels contains 'Servizi e iniziative solidali pubbliche'"%}
{% for member in filteredissues %}
<div class="panel-body">
<a href="{{site.url}}/issues/{{member.number}}" class="list-group-item">
	<h4 class="list-group-item-heading">{{member.title}}</h4>
	<p class="list-group-item-text">{{member.issue.data.descrizione|markdownify}}</p>
                <dl class="row">
                    {% for item in member.issue.data %}
  {% if item[1] != blank %}
  <dt class="col-sm-3">{{item[0]}}</dt>
  <dd class="col-sm-9">{{item[1]}}</dd>
  {% endif %}
  {% endfor %}
                </dl>
</a>
<div class="panel-footer">
<ul class="share-buttons">
  <li>Condividi:</li>
  <li><a href="https://www.covid19italia.help/issues/{{ member.number | datapage_url: '.' }}" title="Copia link"><img alt="Copia link" src="/img/icone/link.png"></a></li>
  <li><a href="https://www.facebook.com/sharer/sharer.php?u=https://www.covid19italia.help/issues/{{ member.number | datapage_url: '.' }}&title={{member.title|truncate:70|uri_escape}} | {{ site.title }}" title="Condividi su Facebook" target="_blank"><img alt="Condividi su Facebook" src="/img/icone/Facebook.png"></a></li>
  <li><a href="https://twitter.com/intent/tweet?url=https://www.covid19italia.help/issues/{{ member.number | datapage_url: '.' }}&text={{member.title|truncate:50|uri_escape}}&via=terremotocentro&hashtags=terremotocentroitalia" target="_blank" title="Tweet"><img alt="Tweet" src="/img/icone/Twitter.png"></a></li>
 <li><a href="https://plus.google.com/share?url=https://www.covid19italia.help/issues/{{ member.number | datapage_url: '.' }}" target="_blank" title="Condividi su Google+"><img alt="Condividi su Google+" src="/img/icone/Google+.png"></a></li>
 <li><a data-proofer-ignore href="mailto:?subject={{member.title|truncate:70|uri_escape}} | {{site.title}}&body={{member.title|truncate:70|uri_escape}}%20Clicca qui:%20https://www.covid19italia.help/issues/{{ member.number | datapage_url: '.' }}" title="Invia email"><img alt="Invia email" src="/img/icone/Email.png"></a></li>
</ul>
</div>
</div>
{% endfor %}
</div>

---
# Consegne e commissioni
<div class="panel-group">
{% assign filteredissues = site.data.issuesjson | where: "state","open" | where_exp: "member","member.issue.labels contains 'Consegne e commissioni'"%}
{% for member in filteredissues %}
<div class="panel-body">
<a href="{{site.url}}/issues/{{member.number}}" class="list-group-item">
	<h4 class="list-group-item-heading">{{member.title}}</h4>
	<p class="list-group-item-text">{{member.issue.data.descrizione|markdownify}}</p>
                <dl class="row">
                    {% for item in member.issue.data %}
  {% if item[1] != blank %}
  <dt class="col-sm-3">{{item[0]}}</dt>
  <dd class="col-sm-9">{{item[1]}}</dd>
  {% endif %}
  {% endfor %}
                </dl>
</a>
<div class="panel-footer">
<ul class="share-buttons">
  <li>Condividi:</li>
  <li><a href="https://www.covid19italia.help/issues/{{ member.number | datapage_url: '.' }}" title="Copia link"><img alt="Copia link" src="/img/icone/link.png"></a></li>
  <li><a href="https://www.facebook.com/sharer/sharer.php?u=https://www.covid19italia.help/issues/{{ member.number | datapage_url: '.' }}&title={{member.title|truncate:70|uri_escape}} | {{ site.title }}" title="Condividi su Facebook" target="_blank"><img alt="Condividi su Facebook" src="/img/icone/Facebook.png"></a></li>
  <li><a href="https://twitter.com/intent/tweet?url=https://www.covid19italia.help/issues/{{ member.number | datapage_url: '.' }}&text={{member.title|truncate:50|uri_escape}}&via=terremotocentro&hashtags=terremotocentroitalia" target="_blank" title="Tweet"><img alt="Tweet" src="/img/icone/Twitter.png"></a></li>
 <li><a href="https://plus.google.com/share?url=https://www.covid19italia.help/issues/{{ member.number | datapage_url: '.' }}" target="_blank" title="Condividi su Google+"><img alt="Condividi su Google+" src="/img/icone/Google+.png"></a></li>
 <li><a data-proofer-ignore href="mailto:?subject={{member.title|truncate:70|uri_escape}} | {{site.title}}&body={{member.title|truncate:70|uri_escape}}%20Clicca qui:%20https://www.covid19italia.help/issues/{{ member.number | datapage_url: '.' }}" title="Invia email"><img alt="Invia email" src="/img/icone/Email.png"></a></li>
</ul>
</div>
</div>
{% endfor %}
</div>

---
# Supporto psicologico
<div class="panel-group">
{% assign filteredissues = site.data.issuesjson | where: "state","open" | where_exp: "member","member.issue.labels contains 'Supporto psicologico'"%}
{% for member in filteredissues %}
<div class="panel-body">
<a href="{{site.url}}/issues/{{member.number}}" class="list-group-item">
	<h4 class="list-group-item-heading">{{member.title}}</h4>
	<p class="list-group-item-text">{{member.issue.data.descrizione|markdownify}}</p>
                <dl class="row">
                    {% for item in member.issue.data %}
  {% if item[1] != blank %}
  <dt class="col-sm-3">{{item[0]}}</dt>
  <dd class="col-sm-9">{{item[1]}}</dd>
  {% endif %}
  {% endfor %}
                </dl>
</a>
<div class="panel-footer">
<ul class="share-buttons">
  <li>Condividi:</li>
  <li><a href="https://www.covid19italia.help/issues/{{ member.number | datapage_url: '.' }}" title="Copia link"><img alt="Copia link" src="/img/icone/link.png"></a></li>
  <li><a href="https://www.facebook.com/sharer/sharer.php?u=https://www.covid19italia.help/issues/{{ member.number | datapage_url: '.' }}&title={{member.title|truncate:70|uri_escape}} | {{ site.title }}" title="Condividi su Facebook" target="_blank"><img alt="Condividi su Facebook" src="/img/icone/Facebook.png"></a></li>
  <li><a href="https://twitter.com/intent/tweet?url=https://www.covid19italia.help/issues/{{ member.number | datapage_url: '.' }}&text={{member.title|truncate:50|uri_escape}}&via=terremotocentro&hashtags=terremotocentroitalia" target="_blank" title="Tweet"><img alt="Tweet" src="/img/icone/Twitter.png"></a></li>
 <li><a href="https://plus.google.com/share?url=https://www.covid19italia.help/issues/{{ member.number | datapage_url: '.' }}" target="_blank" title="Condividi su Google+"><img alt="Condividi su Google+" src="/img/icone/Google+.png"></a></li>
 <li><a data-proofer-ignore href="mailto:?subject={{member.title|truncate:70|uri_escape}} | {{site.title}}&body={{member.title|truncate:70|uri_escape}}%20Clicca qui:%20https://www.covid19italia.help/issues/{{ member.number | datapage_url: '.' }}" title="Invia email"><img alt="Invia email" src="/img/icone/Email.png"></a></li>
</ul>
</div>
</div>
{% endfor %}
</div>