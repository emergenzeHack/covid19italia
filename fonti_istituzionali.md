---
lang: it
layout: page
title: Fonti istituzionali emergenza coronavirus | Fonti ufficiali
subtitle: Tutte le fonti istituzionali da consultare per avere informazioni di prima mano sull'emergenza coronavirus 
permalink: /fonti-istituzionali/
---
<div class="panel-group">
{% assign filteredissues = site.data.machgen.issuesjson | where: "state","open" | where_exp: "member","member.issue.labels contains 'Fonti istituzionali'"%}

{% assign filteredissuesbycategoria = filteredissues | group_by:"issue.data.Categoria" %}

<div class="text-center">
{% for membergroup in filteredissuesbycategoria %}
<span class="col-xs-12 col-sm-6">
  <a href="#{{membergroup.name}}" class="btn btn-success btn-lg col-xs-12 mb-15" role="button">Categoria: {{membergroup.name}}</a>
</span>
{% endfor %}
</div>

{% for membergroup in filteredissuesbycategoria %}
<h2 id="{{membergroup.name}}">Categoria: {{membergroup.name}}</h2>
{% for member in membergroup.items %}

<div class="panel-body">
<div class="list-group-item">
<a href="/issues/{{ member.number | datapage_url: '.' }}">
		<h4 class="list-group-item-heading">{{member.title}}</h4>
</a>
                <dl class="row">
                    {% for item in member.issue.data %}
  {% if item[1] != blank %}
{% assign itemname = item[0]|downcase %}
  <dt class="col-sm-3">{{item[0]}}</dt>
{% if itemname  contains 'link' %}
  <dd class="col-sm-9"><small><a href="{{item[1]}}">{{item[1]}}</a></small></dd>
{% else %}
  <dd class="col-sm-9">{{item[1]}}</dd>
  {% endif %}
  {% endif %}
  {% endfor %}
                </dl>
                <p class="list-group-item-text">{{member.issue.data.descrizione|markdownify}}</p>
                <p class="list-group-item-text">{{member.issue.data.data}}</p>
                </div>
{% include social-share-issue.html %}
</div>
{% endfor %}
{% endfor %}
</div>
