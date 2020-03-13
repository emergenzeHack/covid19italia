---
layout: page
title: Servizi ed iniziative solidali private
permalink: /servizi_iniziative_private/
---
<div class="panel-group">
{% assign filteredissues = site.data.issuesjson | where: "state","open" | where_exp: "member","member.issue.labels contains 'Servizi e iniziative solidali private'"%}
{% for member in filteredissues %}
	<div class="panel-body">
	<a href="/issues/{{ member.number | datapage_url: '.' }}" class="list-group-item">
		<h4 class="list-group-item-heading">{{member.title}}</h4>
		<p class="list-group-item-text">{{member.issue.data.descrizione|markdownify}}</p>
    <p class="list-group-item-text">{{member.issue.data.data}}</p>
	</a>
{% include social-share-issue.html %}
</div>
{% endfor %}
</div>