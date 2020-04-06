---
lang: pt
layout: page
title: Canais de comunicação e redes sociais
subtitle: Contacte Covid19Portugal Help e siga-nos nas nossas redes sociais
permalink: /canais/
---

<div class="segnala">
<p>Aqui estão os canais através dos quais pode contactar-nos, receber actualizações, reportar informações úteis ou necessidades: </p>
     <ul>
         {% if site.author.facebook %}
          <li>
            <a href="https://www.facebook.com/{{ site.author.facebook }}" title="Facebook">
              <span class="fa-stack fa-lg" aria-label="Logo riferito al sito facebook, il carattere f dentro un quadrato blu." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-facebook fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Página do Facebook
            </a><span>para se manter em contacto connosco no Facebook</span>
          </li>
         {% endif %}
         {% if site.author.facebook_group %}
          <li>
            <a href="https://www.facebook.com/groups/{{ site.author.facebook_group}}" title="Facebook">
              <span class="fa-stack fa-lg" aria-label="Logo riferito al sito facebook, il carattere f dentro un quadrato blu." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-facebook fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Grupo do Facebook
            </a><span>para discutir connosco no Facebook</span>
          </li>
         {% endif %}
         {% if site.author.github %}
          <li>
            <a href="https://github.com/{{ site.author.github }}" title="GitHub">
              <span class="fa-stack fa-lg" aria-label="Logo riferito al sito github, raffigura un gatto con i tentacoli." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-github fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Repository GitHub
            </a><span>para colaborar nos desenvolvimentos</span>
          </li>
          {% endif %}
          {% if site.author.twitter %}
          <li>
            <a href="https://twitter.com/{{ site.author.twitter }}" title="Twitter">
              <span class="fa-stack fa-lg" aria-label="Logo riferito al sito twitter, un uccello di colore celeste." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-twitter fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Página Twitter
            </a><span>para comunicar connosco no Twitter</span>
          </li>
          {% endif %}
           {% if site.author.messenger %}
          <li>
            <a href="https://m.me/{{ site.author.messenger }}" title="Messenger una chat">
              <span class="fa-stack fa-lg" aria-label="Logo riferito a Messanger, raffigura una nuvola come quella dei fumetti." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-bullhorn fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Canal Messenger do Facebook
            </a><span>para se manter actualizado directamente do Messenger.</span>
          </li>
          {% endif %}
          <li>
            <a itemprop="sameAs" href="{{ site.author.email }}" title="Email">
              <span class="fa-stack fa-lg" aria-label="Logo raffigurante una busta, email.">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-envelope fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Email
            </a>para comunicar conteúdos que necessitem de ser retirados ou para nos escrever
          </li>
          {% if site.author.archiveorg %}
          <li>
            <a itemprop="sameAs" href="{{ site.author.archiveorg }}" title="archive.org archivio di internet.">
              <span class="fa-stack fa-lg" aria-label="Logo riferito al sito archive.org, raffigura un tempio." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-archive fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Archive.org
            </a>archivio dati
          </li>
          {% endif %}
          {% if site.author.slack %}
	         <li>
            <a href="{{ site.author.slack }}" title="Slack">
              <span class="fa-stack fa-lg" aria-label="Logo Slack" role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-paper-plane fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Gruppo Slack
            </a><span>para coordenar o nosso grupo</span>
          </li>
          {% endif %}
     </ul>
          <p>Tudo o que nos enviar será tratado pela nossa equipa, que poderá colocar as informações no site o mais rapidamente possível. Lembre-se que, ao utilizar os nossos canais, aceita automaticamente assinar as<a href="{{ site.url }}/legal-comunicacao/">notas legais</a> para as informações sobre este projecto.</p>
</div>
