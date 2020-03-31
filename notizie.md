---
lang: pt
layout: page
title: Notícias
permalink: /notícias/
---

{% assign filteredissues = site.data.issuesjson | where: "state","open" | where_exp: "member","member.issue.labels contains 'notícias'" %}
{% for member in filteredissues %}
<div class="card mb-15" id="issue{{member.number}}">
<div class="card-body">
<a href="{{site.url}}/issues/{{member.number}}"><h4 class="card-title">{{member.title}}</h4></a>
<dl class="row">
{% for item in member.issue.data %}
{% if item[1] != blank %}
<dt class="col-sm-3">{{item[0] | replace: "_", " " | capitalize_all}}</dt>
<dd class="col-sm-9">{{item[1] | newline_to_br | auto_link}}</dd>
{% endif %}
{% endfor %}
</dl>
{% include social-share-issue.html %}
</div>
</div>
{% endfor %}
</div>
