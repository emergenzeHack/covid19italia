---
layout: page
title: About
permalink: /about/
---
  
## Il Progetto

**covid19italia.help** è un progetto no profit, organizzato e diretto interamente da volontari e volontarie. È nato per condividere informazioni utili e verificate sull'evento di Coronavirus diffusosi in Italia nel 2020.

Lo scopo è quello di verificare, aggregare ed etichettare segnalazioni di varia natura, al fine di mettere in contatto richieste di aiuto e offerte di beni e servizi.

Vengono inoltre raccolte e pubblicate iniziative solidali, culturali e dirette a promuovere ed implementare telelavoro e didattica a distanza.

Infine, raccogliamo normative, direttive istituzionali e dati.

Non si intende in alcun modo sostituirsi a fonti istituzionali di informazione a cui rimandiamo caldamente per l'attendibilità.

## Riuso

Ogni componente software che sviluppiamo è rilasciato con una licenza Open Source che ne permette il riuso e ne promuove lo sviluppo pubblicamente.

I dati che raccogliamo e produciamo vengono pubblicati e tenuti aggiornati come [Open Data]({{ site.url }}/opendata/).

Laddove lo si ritenga utile, tutta l'infrastruttura è ri-usabile da organizzazioni, associazioni, gruppi informali ed anche pubbliche amministrazioni che avessero bisogno di un servizio per informare e attivarsi per rispondere all’emergenza covid19.

Il progetto è descritto tramite il nostro [wiki](https://github.com/emergenzeHack/covid19italia/wiki).

L'idea ed anche buona parte del progetto è dello stesso team che ha sviluppato il progetto [TerremotoCentroItalia](https://www.terremotocentroitalia.info).

## Chi siamo

Ecco la squadra di volontari che lavora a questo progetto:

### Sviluppo

<div class="row contributorRow">
	{% for contributore in site.data.contributorsCore %}
		<div class="col-md-2 col-sm-2 col-xs-3" style="text-align: center">
			<img src="{{ contributore.avatarUrl }}" alt="Avatar" class="contributorImage img-circle">
			<br>
			<p class="contributorName">{{ contributore.name }}</p>
		</div>
	{% endfor %}
</div>

### Editors

<div class="row contributorRow">
	{% for contributore in site.data.contributorsEditors %}
		<div class="col-md-2 col-sm-2 col-xs-3" style="text-align: center">
			<img src="{{ contributore.avatarUrl }}" alt="Avatar" class="contributorImage img-circle">
			<br>
			<p class="contributorName">{{ contributore.name }}</p>
		</div>
	{% endfor %}
</div>

### Contatti

- [Email](mailto:covid19ita@gmail.com)
- [Twitter](https://twitter.com/ItaliaCovid19)
- [Instagram](https://www.instagram.com/covid19italia.help/)
- [Pagina Facebook](https://www.facebook.com/covid19italia.help/)
- [Gruppo Facebook](https://www.facebook.com/groups/2921275147894653/)
- [Gruppo Telegram ](https://t.me/COVID19I)
- [Canale Telegram](https://t.me/COVID19I)
- [Repository Github](https://github.com/emergenzeHack/covid19italia)

### Tecnologie e Progetti Riusati

- [Beautiful Jekyll](https://deanattali.com/beautiful-jekyll/)
- [Maptune](https://github.com/gjrichter/maptune)
- [Mapstraction](http://mapstraction.com)
- [Leaflet](http://leafletjs.com)
- [Mapicons](http://mapicons.nicolasmollet.com)
- [Bootstrap](http://getbootstrap.com/)
- [Glyphicons](http://glyphicons.com)
- [Jekyll](https://jekyllrb.com/)
- [Github](http://www.github.com)
- [Kobotoolbox](https://www.kobotoolbox.org/)
- [TerremotoCentroItalia](http://www.terremotocentroitalia.info)

