---
layout: page
title: Normativa nazionale
permalink: /normativa-nazionale/
---
<div class="panel-group">
{% assign filteredissues = site.data.issuesjson | where: "state","open" | where_exp: "member","member.issue.labels contains 'Normativa nazionale'"%}
{% for member in filteredissues %}
<div class="panel-body">
<div class="list-group-item">
<a href="/issues/{{ member.number | datapage_url: '.' }}">
		<h4 class="list-group-item-heading">{{member.title}}</h4>
</a>
                <dl class="row">
                    {% for item in member.issue.data %}
  {% if item[1] != blank %}
  <dt class="col-sm-3">{{item[0]}}</dt>
  <dd class="col-sm-9">{{item[1]}}</dd>
  {% endif %}
  {% endfor %}
                </dl>
                <p class="list-group-item-text">{{member.issue.data.descrizione|markdownify}}</p>
                <p class="list-group-item-text">{{member.issue.data.data}}</p>
                </div>
<div class="panel-footer">
<ul class="share-buttons">
  <li>Condividi:</li>
  <li><a href="https://www.covid19italia.info/issues/{{ member.number | datapage_url: '.' }}" title="Copia link"><img alt="Copia link" src="/img/icone/link.png"></a></li>
  <li><a href="https://www.facebook.com/sharer/sharer.php?u=https://www.covid19italia.info/issues/{{ member.number | datapage_url: '.' }}&title={{member.title|truncate:70|uri_escape}} | {{ site.title }}" title="Condividi su Facebook" target="_blank"><img alt="Condividi su Facebook" src="/img/icone/Facebook.png"></a></li>
  <li><a href="https://twitter.com/intent/tweet?url=https://www.covid19italia.info/issues/{{ member.number | datapage_url: '.' }}&text={{member.title|truncate:50|uri_escape}}&via=terremotocentro&hashtags=terremotocentroitalia" target="_blank" title="Tweet"><img alt="Tweet" src="/img/icone/Twitter.png"></a></li>
 <li><a href="https://plus.google.com/share?url=https://www.covid19italia.info/issues/{{ member.number | datapage_url: '.' }}" target="_blank" title="Condividi su Google+"><img alt="Condividi su Google+" src="/img/icone/Google+.png"></a></li>
 <li><a data-proofer-ignore href="mailto:?subject={{member.title|truncate:70|uri_escape}} | {{site.title}}&body={{member.title|truncate:70|uri_escape}}%20Clicca qui:%20https://www.covid19italia.info/issues/{{ member.number | datapage_url: '.' }}" title="Invia email"><img alt="Invia email" src="/img/icone/Email.png"></a></li>
</ul>
</div>
</div>
{% endfor %}
</div>
