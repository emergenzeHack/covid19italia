---
layout: page
title: Fonti istituzionali
permalink: /fonti-istituzionali/
---
<div class="panel-group">
{% assign filteredissues = site.data.issuesjson | where: "state","open" | where_exp: "member","member.issue.labels contains 'Fonti istituzionali'"%}

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
<div class="panel-footer">
<ul class="share-buttons">
  <li>Condividi:</li>
  <li><a href="{{ site.url }}/issues/{{ member.number | datapage_url: '.' }}" title="Copia link"><img alt="Copia link" src="/img/icone/link.png"></a></li>
  <li><a href="https://www.facebook.com/sharer/sharer.php?u={{ site.url }}/issues/{{ member.number | datapage_url: '.' }}&title={{member.title|truncate:70|uri_escape}} | {{ site.title }}" title="Condividi su Facebook" target="_blank"><img alt="Condividi su Facebook" src="/img/icone/Facebook.png"></a></li>
  <li><a href="https://twitter.com/intent/tweet?url={{ site.url }}/issues/{{ member.number | datapage_url: '.' }}&text={{member.title|truncate:50|uri_escape}}&via=terremotocentro&hashtags=terremotocentroitalia" target="_blank" title="Tweet"><img alt="Tweet" src="/img/icone/Twitter.png"></a></li>
 <li><a href="https://plus.google.com/share?url={{ site.url }}/issues/{{ member.number | datapage_url: '.' }}" target="_blank" title="Condividi su Google+"><img alt="Condividi su Google+" src="/img/icone/Google+.png"></a></li>
 <li><a data-proofer-ignore href="mailto:?subject={{member.title|truncate:70|uri_escape}} | {{site.title}}&body={{member.title|truncate:70|uri_escape}}%20Clicca qui:%20{{ site.url }}/issues/{{ member.number | datapage_url: '.' }}" title="Invia email"><img alt="Invia email" src="/img/icone/Email.png"></a></li>
</ul>
</div>
</div>
{% endfor %}
{% endfor %}
</div>
