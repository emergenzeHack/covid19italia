---
lang: it
layout: issuelist_embed
title: Emergenza coronavirus - CSV Monza
mapcenter:
    - 45.59274
    - 9.27571
mapzoom: 12
nome_regione: Lombardia
nome_provincia: Monza e della Brianza
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

<div class="row">
    <div class="col-12 w-100 mb-15">
		<form class="global-search" role="form" action="/searchissues" method="get">
			<div class="input-group">
				<input type="text" class="form-control" id="search-box" name="query" placeholder="Cosa cerchi?">
				<div class="input-group-btn">
                                    <button class="btn btn-primary" type="submit" formtarget="_blank"><span><i class="glyphicon glyphicon-search"></i> Cerca tra {{site.data.machgen.issuesjson.size}} segnalazioni</span></button>
				</div>
			</div>
		</form>
    </div>
</div>
