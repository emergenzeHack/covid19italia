---
lang: it
layout: page
title: Segnala dati
permalink: /dataset/
---

<script type="application/ld+json">
    [{
      "@context": "http://schema.org",
      "@type":"Dataset",
	  "name": "covid19italia.help dataset",
	  "url" : "https://www.covid19italia.help/opendata/",
	  "distribution" :    [
	    { "@type": "DataDownload",
		  "contentUrl" : "https://raw.githubusercontent.com/emergenzeHack/covid19italia_data/master/issues.csv",
		  "encodingFormat" : "text/csv",
		  "requiresSubscription" :"false"
		},
		{ "@type": "DataDownload",
		  "contentUrl" : "https://raw.githubusercontent.com/emergenzeHack/covid19italia_data/master/issuesjson.json",
		  "encodingFormat" : "application/json",
		  "requiresSubscription" :"false"
		},
		{ "@type": "DataDownload",
		  "contentUrl" : "https://raw.githubusercontent.com/emergenzeHack/covid19italia_data/master/issues.geojson",
		  "encodingFormat" : "application/geo+json",
		  "requiresSubscription" :"false"
		}
	  ],
	  "about" : "Questo Dataset contiene tutti i riferimenti ai contenuti e ai dati prodotti o raccolti dal progetto covid19italia.help . Se usi i nostri dati non scordare di citarci come fonte",
	  "abstract" : "Il dataset contiene tutte le notizie di eventi, fake news, iniziative e servizi, raccolte fondi che siamo riusciti a raccogliere riguardo al fenomeno del coronavirus in Italia",
	  "description" : "Il dataset contiene tutte le notizie di eventi, fake news, iniziative e servizi, raccolte fondi che siamo riusciti a raccogliere riguardo al fenomeno del coronavirus in Italia",	  
	  "license" : "https://creativecommons.org/licenses/by/4.0/",
	  "producer" : "https://www.covid19italia.help/",
	  "contentLocation" : {
	      "@type" : "Place",
		  "name" : "Italy"
	  },
	  "exampleOfWork" : "https://www.covid19italia.help/issues/"
	}]
</script>

<div class="text-center">
	<a href="#dataset-ricercati" class="btn btn-warning btn-lg" role="button">Dataset ricercati</a>
	<a href="#dataset-segnalati" class="btn btn-success btn-lg" role="button">Dataset segnalati</a>
	<a href="#tci-opendata" class="btn btn-success btn-lg" role="button">TCI opendata</a>
</div>

<iframe src="https://terremotocentroitalia.herokuapp.com/dataset/" width="100%" height="600rem" frameborder="0">
<a href="https://terremotocentroitalia.herokuapp.com/dataset/">Segnala dati</a></iframe>

## Dataset ricercati

<div class="panel-group">
{% assign filteredissues = site.data.issuesjson | where: "state","open" | where_exp: "member","member.issue.labels contains 'Cerco un dataset'"%}
{% for member in filteredissues %}
<div class="panel-body">
<a href="/issues/{{ member.number }}" class="list-group-item">
	<h4 class="list-group-item-heading">{{member.title}}</h4>
	<p class="list-group-item-text">{{member.issue.data.Testo|markdownify}}</p>
	<p class="list-group-item-text">{{member.issue.data.data}}</p>
</a>

{% include social-share-issue.html %}
</div>
{% endfor %}
</div>

## Dataset segnalati

{% assign filteredissues = site.data.issuesjson | where: "state","open" | where_exp: "member","member.issue.labels contains 'Segnalo un dataset'" %}
{% if filteredissues.size > 0 %}
<div class="panel-group">
{% for member in filteredissues %}
<div class="panel-body">
<a href="/issues/{{ member.number }}" class="list-group-item">
	<h4 class="list-group-item-heading">{{member.title}}</h4>
	<p class="list-group-item-text">{{member.issue.data.Testo|markdownify}}</p>
	<p class="list-group-item-text">{{member.issue.data.data}}</p>
</a>

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
</div>
{% else %}
<div>Non ci sono dataset segnalati</div>
{% endif %}

## TCI opendata

I dati prodotti e gestiti da TCI sono disponibili come _open data_ con varie licenze e sono catalogati [nell'apposita pagina](/opendata).
