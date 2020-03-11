---
layout: page
title: About
permalink: /about/
---

<div class="text-center">
	<a href="#il-progetto" class="btn btn-primary btn-lg" role="button">Il Progetto</a>
	<a href="#credits" class="btn btn-primary btn-lg" role="button">Credits</a>
	<a href="#contatti" class="btn btn-primary btn-lg" role="button">Contatti</a>
	<a href="#press" class="btn btn-primary btn-lg" role="button">Press</a>
</div>

### Il Progetto


Questo è un progetto non profit, organizzato interamente da volontari e volontarie. È nato per condividere informazioni utili e
verificate sull'evento di CoronaVirus diffusosi in Italia nel 2020.

Il progetto si pone come scopo quello di aggregare e non disperdere contenuti utili a tutti provenienti da fonti di varia natura (ufficiali e non) al fine creare valore in un momento di crisi per il paese.

Il progetto non vuole in alcun modo sostituirsi a fonti istituzionali di informazione a cui rimandiamo caldamente per l'attendibilità.

Il progetto, laddove lo si ritenga utile, è usabile da organizzazioni, associazioni, gruppi informali ed anche pubbliche amministrazioni che avessero bisogno di un servizio per informare e attivarsi per rispondere all’emergenza covid19.

Il progetto è descritto tramite il nostro [wiki](https://github.com/emergenzeHack/covid19italia/wiki).

L'idea (ed anche buona parte del progetto) è dello stesso team che ha sviluppato il progetto [TerremotoCentroItalia](https://www.terremotocentroitalia.info).

### Credits

Un grazie sentito a :

.....
(i ringraziamenti sono in progress ogni giorno....Non avertene a male se non compari ancora, grazie lo stesso!)

### Contatti

- [Email](mailto:covid19ita@gmail.com)
- [Twitter](https://twitter.com/ItaliaCovid19)
- [Instagram](https://www.instagram.com/covid19italia.info/)
- [Facebook](https://www.facebook.com/covid19italia.info)
- [Gruppo Telegram ](http://t.me/covid19italia)
- [Canale Telegram](https://t.me/COVID19I)
- [Repository Github](https://github.com/emergenzeHack/covid19italia)

### Altri crediti

- [Maptune](https://github.com/gjrichter/maptune)
- [Mapstraction](http://mapstraction.com)
- [Leaflet](http://leafletjs.com)
- [Mapicons](http://mapicons.nicolasmollet.com)
- [Bootstrap](http://getbootstrap.com/)
- [Glyphicons](http://glyphicons.com)
- [Jekyll](https://jekyllrb.com/)
- [Github](http://www.github.com)

### Press

|Data         | Dove    | Titolo |
|:------------|:--------|:------|
|{% for member in site.data.press %}{{member.data}} | {{member.dove}} | [{{member.titolo}}]({{member.link}})|
{% endfor %}
