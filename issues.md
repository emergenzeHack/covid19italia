---
lang: pt
layout: issuelist
title: Emergência do coronavírus peça ajuda, partilhe iniciativas, notícias, dados
subtitle: Descubra todos os relatórios feitos sobre a plataforma pt.Covid19people.Help
permalink: /iniciativas/
categorieMapAll: true
---

{% if page.categorieissue %}
{% assign categorieissue = page.categorieissue %}
{% else %}
{% assign categorieissue = site.categorieissue %}
{% endif %}

<div class="row mx-auto">
{% for categoriatuple in categorieissue %}
{% assign categoria = categoriatuple | split: ";" %}
  <div class="col-xs-12 col-sm-6 mb-15">
	  <a href="/{{categoria[0] | slugify}}" class="btn btn-success btn-block">{{categoria[0]}}</a>
	</div>
{% endfor %}
</div>


