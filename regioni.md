---
lang: pt
layout: page
title: "Emergenza coronavirus: segnalazioni per regione"
subtitle: Regione per regione le segnalazioni fatte sulla piattaforma Covid19Italia.Help
permalink: /issues/regione/
---


<div class="row">
{%- for regione in site.data.regioni -%}
<div class="col-md-6 col-sm-12 col-xs-12 mb-15">
	  <a href="/issues/regione/{{regione.nome_regione | replace: "'", "" | slugify}}/" class="btn btn-success btn-block" >{{regione.nome_regione}}</a>
</div>
{%- endfor -%}
</div>

