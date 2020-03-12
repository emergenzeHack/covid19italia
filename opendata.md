---
layout: page
title: Opendata
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

