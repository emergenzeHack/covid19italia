---
layout: issuelist
title: Iniziative Solidali
permalink: /issues/
categorieissue:
 - Raccolte fondi;Raccolte fondi
 - Bambini;Bambini
 - Servizi e iniziative solidali;Servizi e iniziative solidali
 - Iniziative culturali e ricreative;Attivita culturali e ricreative
 - Consegne e commissioni;Consegne e commissioni
 - Supporto psicologico;Supporto psicologico
 - Sostegno lavoro e imprese;Sostegno lavoro e imprese
 - Donazioni beni/strumenti;Donazioni beni/strumenti
 - Didattica a distanza e-learning;Didattica a distanza e-learning
categorieMapAll: true
---

<div class="row">
<div class="text-center">
{% for categoriatuple in page.categorieissue %}
{% assign categoria = categoriatuple | split: ";" %}
  <span class="col-xs-12 col-sm-6">
	  <a href="/{{categoria[0] | slugify}}" class="btn btn-success btn-lg col-xs-12 mb-15" role="button">{{categoria[0]}}</a>
	</span>
{% endfor %}
</div>
</div>


