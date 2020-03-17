---
layout: issuelist
title: Archivio segnalazioni
permalink: /issues/
categorieMapAll: true
---

{% if page.categorieissue %}
{% assign categorieissue = page.categorieissue %}
{% else %}
{% assign categorieissue = site.categorieissue %}
{% endif %}

<div class="row">
<div class="text-center">
{% for categoriatuple in categorieissue %}
{% assign categoria = categoriatuple | split: ";" %}
  <span class="col-xs-12 col-sm-6">
	  <a href="/{{categoria[0] | slugify}}" class="btn btn-success btn-lg col-xs-12 mb-15" role="button">{{categoria[0]}}</a>
	</span>
{% endfor %}
</div>
</div>


