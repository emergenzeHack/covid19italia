---
lang: it
layout: page
title: Fake News e bufale sul coronavirus
subtitle: Fai attenzione a bufale e fake news sul coronavirus e segnalale a Covid19Italia.help
permalink: /fake-news/
---

Vuoi abbonarti alle nostre FAKE NEWS? Iscriviti a [questo feed](https://script.googleusercontent.com/macros/echo?user_content_key=-1pBZ5FSSHLKu9ITbEvoauID8dWwF321PgcKMIiUAh4JxLRANyjyIl0H58m-rzCwaJ7nA_a5_baHSztwZFQNyUlMAmjLK_zsm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnMpwm1G-nXDvxsGuhE_BPNBdZvO-e2L8rmrctOWUXYpo9_Bx7cv4i1OqPzsuuyxeTcpYAgK7DOSm&lib=MNwjxxHPb0n3pOMRizSkov0wBSA0_FGxs)

<div class="panel-group">
{% assign filteredissues = site.data.machgen.issuesjson | where: "state","open" | where_exp: "member","member.issue.labels contains 'Fake News'" %}
{% for member in filteredissues %}
<div class="panel-body issuepanel" id="issue{{member.number}}">
<div class="list-group-item">
<a href="{{site.url}}/issues/{{member.number}}"><h4 class="list-group-item-heading">{{member.title}}</h4></a>
<dl class="row">
{% for item in member.issue.data %}
{% if item[1] != blank %}
<dt class="col-sm-3">{{item[0] | replace: "_", " " | capitalize_all}}</dt>
<dd class="col-sm-9">{{item[1] | newline_to_br | auto_link}}</dd>
{% endif %}
{% endfor %}
</dl>
</div>
{% include social-share-issue.html %}
</div>
{% endfor %}
</div>
