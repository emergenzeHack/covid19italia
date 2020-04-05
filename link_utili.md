---
lang: pt
layout: page
title: Link e Contatti Utili
permalink: /link_utili/
---

Di seguito la lista dei contatti e dei link registrati da questo progetto.

# Contatti

{% assign filteredissues = site.data.machgen.issuesjson | where: "state","open" | where_exp: "member","member.issue.labels contains 'Contatti'"%}
{% for member in filteredissues %}
* <a href="/issues/{{ member.number | datapage_url: '.' }}">{{member.title}}</a>
{% endfor %}

# Link

{: .table .table-striped #links}
Nome            |Link
:---------------|:-----------------------
{% for member in site.data.links %} {{member.Nome}} | [Link]({{member.Link}})
{% endfor %}
