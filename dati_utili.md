---
lang: it
layout: page
title: Dati utili
permalink: /dati_utili/
---

<div class="panel-group">
{% assign filteredissues = site.data.machgen.issuesjson | where: "state","open" | where_exp: "member","member.issue.labels contains 'Dati utili'" %}
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
