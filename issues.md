---
lang: gr
layout: issuelist
title: "Όλες οι Πληροφορίες"
subtitle: Ανακαλύψτε όλες τις αναφορές που έγιναν στην πλατφόρμα Covid19Greece.Help
permalink: /issues/
categorieMapAll: true
---

{% if page.issuecategories %}
{% assign issuecategories = page.issuecategories[page.lang] %}
{% else %}
{% assign issuecategories = site.data.cfg.issuecategories[page.lang] %}
{% endif %}

<div class="row mx-auto">
{% for category in issuecategories %}
  <div class="col-xs-12 col-sm-6 mb-15">
	  <a href="/{{category[0] | slugify}}" class="btn btn-success btn-block">{{category[0]}}</a>
	</div>
{% endfor %}
</div>


