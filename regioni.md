---
layout: page
title: Emergenza coronavirus: segnalazioni per regione
subtitle: Regione per regione le segnalazioni fatte sulla piattaforma Covid19Italia.Help
permalink: /issues/regione/
---


<div class="row">
<div class="text-center">
{% for regione in site.data.regioni %}
  <span class="col-xs-12 col-sm-6">
	  <a href="/issues/regione/{{regione.nome_regione | replace: "'", "" | slugify}}/" class="btn btn-success btn-lg col-xs-12 mb-15" role="button">{{regione.nome_regione}}</a>
	</span>
{% endfor %}
</div>
</div>

