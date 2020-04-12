---
lang: it
layout: page
title: Usa i nostri dati | Open Data Coronavirus 
subtitle: Gli open data di Covid19Italia.Help con le segnalazioni in emergenza coronavirus da riutilizzare
permalink: /opendata/
---

Se usi i nostri dati non scordare di citarci come fonte (grazie!) e segnalacelo [scrivendoci una mail](mailto:covid19ita@gmail.com) in modo che potremmo citarti tra gli utilizzatori di questo progetto!

## DATASET 
In tabella trovi tutti i riferimenti ai dati raccolti e ridistribuiti da questo progetto assieme alla loro licenza di riuso.

{: .table .table-striped #opendata}
Nome            |Dataset         |Licenza         |Link Licenza    |Fonte           |Formato         |Note
:---------------|:---------------|:---------------|:---------------|:---------------|:---------------|:---------------
{% for member in site.data.opendata %} {{member.Nome}} | [Dataset]({{member.Dataset}}) | {{member.Licenza}} | [Link Licenza]({{member.Linklicenza}}) | [Fonte]({{member.Fonte}}) | {{member.Formato}} | {{member.Note}}
{% endfor %}

## Feed RSS
Se hai un servizio che può usare il formato Feed RSS puoi anche usare [questo feed delle notizie nel bollettino](https://script.google.com/macros/s/AKfycbxTuPFn9ePZOhI7et2f8nSPjkjlhd9zqHth9sOVYRZ6Va09zmE/exec), se invece cerchi un feed particolare tra tutte le nostre categorie puoi visualizzare tutti i nostri Feed RSS [in questa pagina](/rss)


## API
Se invece vuoi accedere ai nostri dati in modo programmatico puoi fare uso delle nostre API documentate [qui](https://github.com/emergenzeHack/covid19italia_api/wiki)
