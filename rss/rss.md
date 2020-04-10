---
layout: page
title: Feed RSS
permalink: /rss/
---

<h2>Feed delle singole regioni</h2>
<div class="list-group">
{% for regione in site.data.geo.regioni %}
{% assign regionelink = regione.nome_regione | remove: "'" | slugify %}

<a class="list-group-item" href="/rss/regione/{{regionelink}}.xml">
<img src="/img/icone/rss.png" class="img-fluid" width="50px" alt="Icona FEED RSS">
</img>
{{regione.nome_regione}}
</a>

{% endfor %}
</div>

<h2>Feed per categoria</h2>
<div class="list-group">
{% for categoriatuple in site.data.cfg.issuecategories %}
{% assign categorialink = categoriatuple[1]['permalink'] | remove_first: '/' | reverse | remove_first: '/' | reverse %}
<a class="list-group-item" href="/rss/categoria/{{categorialink}}.xml">
<img src="/img/icone/rss.png" class="img-fluid" width="50px" alt="Icona FEED RSS">
</img> 
{{categoriatuple[1]["displayname"]}}</a>
{% endfor %}
</div>
