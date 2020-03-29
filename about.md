---
layout: page
title: O que é Covid19Portugal Help? Coronavirus Resposta de Emergência
subtitle: Saiba como funciona a plataforma, como colaborar e como comunicar um caso

permalink: sobre

lang: pt
---

## O Projeto

**covid19italia.help** é um projeto sem fins lucrativos, organizado e dirigido inteiramente por voluntárias e voluntários. Foi criado para compartilhar informações úteis e verificadas sobre o evento Coronavírus espalhado em Itália em 2020. Agora o projeto está a espalhar-se por muitos outros países, incluindo Portugal com Covid19Portugal Help.

O objetivo é verificar, agregar e rotular relatórios de vários tipos, a fim de combinar pedidos de ajuda e ofertas de bens e serviços.

Também recolhe e publica iniciativas culturais e de solidariedade destinadas a promover e implementar o teletrabalho e a educação à distância.

Finalmente, recolhemos leis e regras, diretivas institucionais e dados que disponibilizamos no nosso site.

Não pretendemos de forma alguma substituir as fontes institucionais de informação às quais nos referimos fortemente pela sua fiabilidade.

## Estatísticas

{% assign labels = "Serviços e iniciativas privadas de solidariedade, Serviços e iniciativas de solidariedade pública,Entregas e comissões,Notícias Falsas,Mulheres,Angariação de fundos,Apoio psicológico,e-learning educação à distância,Fontes institucionais,Informazioni utili,Notícias" | split: ',' %}

Até agora, na Itália, tratámos
{% for valore in site.data.statisticheSegnalazioni %} {% if valore.Tipo == "Segnalazioni totali" %} <b>{{valore.Valore}}</b> {% endif %} {% endfor %} relatórios, aceitando e verificando {% for valore in site.data.statisticheSegnalazioni %} {% if valore.Tipo == "Accettate" %} <b>{{valore.Valore}}</b>{% endif %}{% endfor %},  categorizados da seguinte forma:
{% for valore in site.data.statisticheSegnalazioni %} {% if labels contains valore.Tipo %}
- {{ valore.Valore }} {{ valore.Tipo }} {% endif %} {% endfor %}

## Reutilização

Cada componente de software que desenvolvemos é lançado sob uma licença Open Source que permite a sua reutilização e promove o seu desenvolvimento publicamente.

Os dados que coletamos e produzimos são publicados e mantidos atualizados como  [Dados Abertos]({{ site.url }}/opendata/).

Quando considerado útil, toda a infraestrutura é reutilizável pelas organizações, associações, grupos informais e até mesmo administrações públicas que precisam de um serviço para informar e responder à emergência covid19.

O projeto é descrito através do nosso [wiki](https://github.com/emergenzeHack/covid19italia/wiki).

A ideia e também uma grande parte do projeto é da mesma equipa que o desenvolveu [TerremotoCentroItalia](https://www.terremotocentroitalia.info).

## Sobre nós

De seguida, apresentamos a equipa de voluntários que trabalha neste projeto:

### Desenvolvimento

<div class="row contributorRow">
	{% for contributore in site.data.contributorsCore %}
		<div class="col-md-2 col-sm-2 col-xs-3" style="text-align: center">
			<img src="{{ contributore.avatarUrl }}" alt="Avatar" class="contributorImage img-circle">
			<br>
			<p class="contributorName">{{ contributore.name }}</p>
		</div>
	{% endfor %}
</div>

### Editores

<div class="row contributorRow">
	{% for contributore in site.data.contributorsEditors %}
		<div class="col-md-2 col-sm-2 col-xs-3" style="text-align: center">
			<img src="{{ contributore.avatarUrl }}" alt="Avatar" class="contributorImage img-circle">
			<br>
			<p class="contributorName">{{ contributore.name }}</p>
		</div>
	{% endfor %}
</div>

### Mídia e comunicação

<div class="row contributorRow">
	{% for contributore in site.data.contributorsMedia %}
		<div class="col-md-2 col-sm-2 col-xs-3" style="text-align: center">
			<img src="{{ contributore.avatarUrl }}" alt="Avatar" class="contributorImage img-circle">
			<br>
			<p class="contributorName">{{ contributore.name }}</p>
		</div>
	{% endfor %}
</div>

### Contactos

- [Email](mailto:covid19ita@gmail.com)
- [Twitter](https://twitter.com/ItaliaCovid19)
- [Instagram](https://www.instagram.com/covid19italia.help/)
- [Pagina Facebook](https://www.facebook.com/covid19italia.help/)
- [Gruppo Facebook](https://www.facebook.com/groups/2921275147894653/)
- [Gruppo Telegram ](https://t.me/COVID19I)
- [Canale Telegram](https://t.me/COVID19I)
- [Repository Github](https://github.com/emergenzeHack/covid19italia)

### Tecnologias e Projetos Reutilizados

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

