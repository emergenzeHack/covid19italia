---
lang: pt
layout: page
title: Notícias falsas sobre o Coronavirus
subtitle: Cuidado com as notícias falsas sobre o Coronavirus. Denuncie em pt.Covid19Italia.help
permalink: /fake-news/
---
<div class="panel-group">
{% assign filteredissues = site.data.issuesjson | where: "state","open" | where_exp: "member","member.issue.labels contains 'Fake News'" %}
{% for member in filteredissues %}
<div class="panel-body issuepanel" id="issue{{member.number}}">
<div class="list-group-item">
<a href="{{site.url}}/issues/{{member.number}}"><h4 class="list-group-item-heading">{{member.title}}</h4></a>
<dl class="row">
{% for item in member.issue.data %}
{% if item[1] != blank %}
<dt class="col-sm-3">{{item[0] | replace: "_", " " | capitalize_all}}</dt>
<dd class="col-sm-9">{{item[1] | newline_to_br | auto_link}}</dd>
{% endif %}
{% endfor %}
</dl>
</div>
{% include social-share-issue.html %}
</div>
{% endfor %}
</div>
