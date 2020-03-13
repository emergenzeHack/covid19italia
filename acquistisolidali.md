---
layout: page
title: Acquisti Solidali
permalink: /acquistisolidali/
---
<div class="panel-group">
{% assign filteredissues = site.data.issuesjson | where: "state","open" | where_exp: "member","member.issue.labels contains 'acquisto solidale'"%}
{% for member in filteredissues %}

<div class="panel panel-default">
<div class="panel-heading">
<a href="/issues/{{ member.number | datapage_url: '.' }}">
<h4 class="panel-title">
{{member.title}} <small>({{member.issue.data.data}})</small>
</h4>
</a>
</div>
<div class="panel-body">
<small>
<div class="row"><div class="col-xs-12">{{member.issue.data.descrizione|markdownify}}</div></div>
<div class="row">
<div class="col-xs-6"><div class="col-xs-1"><i class="fa fa-phone" aria-hidden="true"></i></div><div class="col-xs-11">{% if member.issue.data.tel != blank %}<a href="tel:{{member.issue.data.tel}}">{{member.issue.data.tel}}</a>{% endif %}</div></div>
<div class="col-xs-6"><div class="col-xs-1"><i class="fa fa-envelope" aria-hidden="true"></i></div><div class="col-xs-11">{% if member.issue.data.email != blank %}<a href="mailto:{{member.issue.data.email}}">{{member.issue.data.email}}</a>{% endif %}</div></div>
</div>
<div class="row"><div class="col-xs-6"><div class="col-xs-1"><i class="fa fa-home"></i></div><div class="col-xs-11">{{member.issue.data.indirizzo}}</div></div><div class="col-xs-6"></div></div>

</small>
</div>
{% include social-share-issue.html %}
</div>
{% endfor %}
</div>
