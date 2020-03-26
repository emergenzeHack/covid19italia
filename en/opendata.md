---
lang: en
layout: page
title: Open Data Covid19 | Open Data Coronavirus
subtitle:  Open data of Covid19Italia.Help with reports coronavirus emergency
permalink: en/opendata/
---

Here in table you'll find all reference of contents and to data reported by this project with their licence to reuse it.
If you use our data don't forget to respect the licence and write to us [with a mail](mailto:covid19ita@gmail.com) so we can give you the rigth credits!

{: .table .table-striped #opendata}
Name            |Dataset         |Licence         |Link Licence    |Source           |Format         |Remarks
:---------------|:---------------|:---------------|:---------------|:---------------|:---------------|:---------------
{% for member in site.data.opendata %} {{member.Nome}} | [Dataset]({{member.Dataset}}) | {{member.Licenza}} | [Link Licenza]({{member.Linklicenza}}) | [Fonte]({{member.Fonte}}) | {{member.Formato}} | {{member.Note}}
{% endfor %}

If you have a service that can use the FEED RSS you can use also [this feed rss](http://feeds.feedburner.com/covid19ita_segnalazioni) or [this feed of most important news](https://script.google.com/macros/s/AKfycbxTuPFn9ePZOhI7et2f8nSPjkjlhd9zqHth9sOVYRZ6Va09zmE/exec).
