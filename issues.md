---
layout: issuelist
title: "Όλες οι Αναρτήσεις"
subtitle: Δες εδώ όλες τις αναφορές που έγιναν στην πλατφόρμα Covid19Greece.Help
permalink: /issues/
categorieMapAll: true
justLatestIssues: true
---

{%- if page.issuecategory -%}
{% assign issuecategories = "" | split: "," %}
{% assign tmpcategory = "" | split: "," %}
{%- assign tmpcategory = tmpcategory | push: page.issuecategory -%}
{%- assign tmpcategory = tmpcategory | push: site.data.cfg.issuecategories[page.issuecategory] -%}
{%- assign issuecategories = issuecategories |  push: tmpcategory -%}
{%- else -%}
{%- assign issuecategories = site.data.cfg.issuecategories -%}
{%- endif -%}

<div class="row mx-auto">
{% for categorytuple in issuecategories %}
{% assign category = categorytuple[1] %}
  <div class="col-12 col-sm-6 mb-15">
	  <a href="{{category["permalink"]}}" class="btn btn-primary btn-block text-left h-100">
              <span class="fa-stack text-left" role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true" style="color:{{category['markercolor']}};"></i>
                <i class="fa fa-{{category['markericon']}} fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>
<span class="text-center">{{category["displayname"]}}</span></a>
	</div>
{% endfor %}
</div>


