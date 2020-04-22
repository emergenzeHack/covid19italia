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
Se hai un servizio che può usare il formato Feed RSS puoi anche usare [questo feed delle notizie nel bollettino](https://script.google.com/macros/s/AKfycbxTuPFn9ePZOhI7et2f8nSPjkjlhd9zqHth9sOVYRZ6Va09zmE/exec), 

Vuoi abbonarti alle nostre FAKE NEWS? Iscriviti a [questo feed](https://script.googleusercontent.com/macros/echo?user_content_key=-1pBZ5FSSHLKu9ITbEvoauID8dWwF321PgcKMIiUAh4JxLRANyjyIl0H58m-rzCwaJ7nA_a5_baHSztwZFQNyUlMAmjLK_zsm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnMpwm1G-nXDvxsGuhE_BPNBdZvO-e2L8rmrctOWUXYpo9_Bx7cv4i1OqPzsuuyxeTcpYAgK7DOSm&lib=MNwjxxHPb0n3pOMRizSkov0wBSA0_FGxs)

Se invece cerchi un feed particolare tra tutte le nostre categorie puoi visualizzare tutti i nostri Feed RSS [in questa pagina](/rss)


## API
Se invece vuoi accedere ai nostri dati in modo programmatico puoi fare uso delle nostre API documentate [qui](https://github.com/emergenzeHack/covid19italia_api/wiki)
