---
lang: pt
layout: page
title: Open Data Covid19 | Open Data Coronavirus
subtitle: Os dados abertos do Covid19Portugal Help com relatórios de emergência do coronavírus para reutilização
permalink: /opendata/
---


Na tabela encontrará todas as referências aos conteúdos e dados produzidos ou recolhidos por este projecto, juntamente com a respectiva licença de reutilização.
Se utilizar os nossos dados não se esqueça de nos citar como a fonte (obrigado!) e informe-nos [enviando-nos um e-mail](mailto:covid19pt.help@gmail.com) para que possamos citá-lo entre
os utilizadores deste projecto!

{: .table .table-striped #opendata}
Nome            |Dataset         |Licença         |Link Licença    |Fonte           |Formato         |Notas
:---------------|:---------------|:---------------|:---------------|:---------------|:---------------|:---------------
{% for member in site.data.opendata %} {{member.Nome}} | [Dataset]({{member.Dataset}}) | {{member.Licença}} | [Link Licença]({{member.Linklicença}}) | [Fonte]({{member.Fonte}}) | {{member.Formato}} | {{member.Notas}}
{% endfor %}


