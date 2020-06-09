---
lang: it
layout: issuelist_embed
title: Emergenza coronavirus - CSV Lecco
nome_regione: Lombardia
nome_provincia: Lecco
mapcenter:
        - 45.90111
        - 9.39242
mapzoom: 9
issuecategories: 
    - games and activities for children
    - cultural activities and leisure
    - solidarity services and initiatives
    - deliveries and services
    - psychological support
    - goods donations and services offering
    - e-learning
    - migrants and refugees
---

{%- if page.issuecategory != blank -%}

    {% assign issuecategories = "" | split: "," %}
    {% assign tmpcategory = "" | split: "," %}
    {%- assign tmpcategory = tmpcategory | push: page.issuecategory -%}
    {%- assign tmpcategory = tmpcategory | push: site.data.cfg.issuecategories[page.issuecategory] -%}
    {%- assign issuecategories = issuecategories |  push: tmpcategory -%}

{%- elsif page.issuecategories != blank -%}

    {% assign issuecategories = "" | split: "," %}
    {% for category in page.issuecategories %}
    {% assign tmpcategory = "" | split: "," %}
    {%- assign tmpcategory = tmpcategory | push: category -%}
    {%- assign tmpcategory = tmpcategory | push: site.data.cfg.issuecategories[category] -%}
    {%- assign issuecategories = issuecategories |  push: tmpcategory -%}
    {% endfor %}

{%- elsif page.displayname != blank and page.markericon != blank -%}

    {% assign issuecategories = "" | split: "," %}
    {% assign tmpcategory = "" | split: "," %}
    {%- assign tmpcategory = tmpcategory | push: "page" -%}
    {%- assign tmpcategory = tmpcategory | push: page -%}
    {%- assign issuecategories = issuecategories |  push: tmpcategory -%}

{%- else -%}

    {%- assign issuecategories = site.data.cfg.issuecategories -%}

{%- endif -%}

<div class="row mx-auto">
{% for categorytuple in issuecategories %}
{% assign category = categorytuple[1] %}
  <div class="col-12 col-sm-6 mb-15">
	  <a href="#{{category["permalink"]}}" class="btn btn-primary btn-block text-left h-100" title="Vedi tutte le segnalazioni della categoria {{category['displayname']}}">
              <span class="fa-stack text-left" aria-label="logo del marker della segnalazione" role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true" style="color:{{category['markercolor']}};"></i>
                <i class="fa fa-{{category['markericon']}} fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>
<span class="text-center">{{category["displayname"]}}</span></a>
	</div>
{% endfor %}
</div>
