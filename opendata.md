---
lang: pt
layout: page
title: Open Data Covid19 | Open Data Coronavirus
subtitle: Gli open data di Covid19Italia.Help con le segnalazioni in emergenza coronavirus da riutilizzare
permalink: /opendata/
---


In tabella trovi tutti i riferimenti ai contenuti e ai dati prodotti o raccolti da questo progetto assieme alla loro licenza di riuso.
Se usi i nostri dati non scordare di citarci come fonte (grazie!) ma segnalacelo [scrivendoci una mail](mailto:covid19ita@gmail.com) in modo che potremmo citarti tra
gli utilizzatori di questo progetto!

{: .table .table-striped #opendata}
Nome            |Dataset         |Licenza         |Link Licenza    |Fonte           |Formato         |Note
:---------------|:---------------|:---------------|:---------------|:---------------|:---------------|:---------------
{% for member in site.data.opendata %} {{member.Nome}} | [Dataset]({{member.Dataset}}) | {{member.Licenza}} | [Link Licenza]({{member.Linklicenza}}) | [Fonte]({{member.Fonte}}) | {{member.Formato}} | {{member.Note}}
{% endfor %}


Se hai un servizio che può usare il formato Feed RSS puoi anche usare [questo feed rss delle segnalazioni](http://feeds.feedburner.com/covid19ita_segnalazioni) oppure [questo feed delle notizie nel bollettino](https://script.google.com/macros/s/AKfycbxTuPFn9ePZOhI7et2f8nSPjkjlhd9zqHth9sOVYRZ6Va09zmE/exec).
