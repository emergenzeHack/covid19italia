---
layout: issuelist
title: "Όλες οι Πληροφορίες"
subtitle: Ανακαλύψτε όλες τις αναφορές που έγιναν στην πλατφόρμα Covid19Greece.Help
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
  <div class="col-xs-12 col-sm-6 mb-15">
	  <a href="{{category["permalink"]}}" class="btn btn-primary btn-block">{{category["displayname"]}}</a>
	</div>
{% endfor %}
</div>


