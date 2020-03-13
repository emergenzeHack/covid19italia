---
layout: page
title: Canali di comunicazione
permalink: /canali/
---

<div class="segnala">
<p>Ecco i canali attraverso cui puoi contattarci, ricevere aggiornamenti, segnalare info utili o necessità: </p>
         {% if site.author.facebook and site.share-links-active.facebook %}
          <li>
            <a href="https://www.facebook.com/{{ site.author.facebook }}" title="Facebook">
              <span class="fa-stack fa-lg" aria-label="Logo riferito al sito facebook, il carattere f dentro un quadrato blu." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-facebook fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Pagina Facebook
            </a><span>da usare per restare in contatto con noi su Facebook</span>
          </li>
         {% endif %}
         {% if site.author.facebook_group and site.share-links-active.facebook %}
          <li>
            <a href="https://www.facebook.com/groups/{{ site.author.facebook_group}}" title="Facebook">
              <span class="fa-stack fa-lg" aria-label="Logo riferito al sito facebook, il carattere f dentro un quadrato blu." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-facebook fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Gruppo Facebook
            </a><span>da usare per discutere con noi su Facebook</span>
          </li>
         {% endif %}
         {% if site.author.androidapp and site.share-links-active.androidapp %}
          <li>
            <a href="https://play.google.com/store/apps/details?id={{ site.author.androidapp }}&hl=it_it" title="Android App">
              <span class="fa-stack fa-lg" aria-label="Logo raffigurante il market di applicazioni android." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-android fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;App Android
            </a><span>consulta i contenuti da app android</span>
          </li>
         {% endif %}
         {% if site.author.github and site.share-links-active.github %}
          <li>
            <a href="https://github.com/{{ site.author.github }}" title="GitHub">
              <span class="fa-stack fa-lg" aria-label="Logo riferito al sito github, raffigura un gatto con i tentacoli." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-github fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Repository GitHub
            </a><span>per collaborare agli sviluppi</span>
          </li>
          {% endif %}
          {% if site.author.twitter and site.share-links-active.twitter %}
          <li>
            <a href="https://twitter.com/{{ site.author.twitter }}" title="Twitter">
              <span class="fa-stack fa-lg" aria-label="Logo riferito al sito twitter, un uccello di colore celeste." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-twitter fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Pagina Twitter
            </a><span>da usare per comunicare con noi su Twitter</span>
          </li>
          {% endif %}
           {% if site.author.instagram and site.share-links-active.instagram %}
          <li>
            <a href="https://www.instagram.com/{{ site.author.instagram }}" title="Instagram un social network pieno di fotografie.">
              <span class="fa-stack fa-lg" aria-label="Logo riferito a instagram, raffigura una macchina fotografica stilizzata." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-instagram fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Pagina Instagram
            </a><span>per vedere le foto su Instagram</span>
          </li>
          {% endif %}
           {% if site.author.messenger and site.share-links-active.messenger %}
          <li>
            <a href="https://m.me/{{ site.author.messenger }}" title="Messenger una chat">
              <span class="fa-stack fa-lg" aria-label="Logo riferito a Messanger, raffigura una nuvola come quella dei fumetti." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-bullhorn fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Canale Facebook Messenger
            </a><span>per restare aggiornato direttamente da Messenger.</span>
          </li>
          {% endif %}
          {% if site.author.telegram and site.share-links-active.telegram %}
          <li>
            <a href="{{ site.author.telegram }}" title="Telegram una chat.">
              <span class="fa-stack fa-lg" aria-label="Logo riferito a telegram, raffigura un aereoplano di carta stilizzato." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-paper-plane fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Canale Telegram
            </a><span>per restare aggiornato con le nostre notizie</span>
          </li>
          {% endif %}
          {% if site.author.telegram_bot and site.share-links-active.telegram_bot %}
          <li>
            <a href="http://telegram.me/{{ site.author.telegram_bot }}" title="Bot Telegram">
              <span class="fa-stack fa-lg" aria-label="Logo riferito al RoBot testuale su Telegram." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-paper-plane fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;BOT Telegram
            </a><span>per inviare segnalazioni con smartphone dal "campo"</span>
          </li>
          {% endif %}
          {% if site.author.medium and site.share-links-active.medium %}
          <li>
            <a itemprop="sameAs" href="{{ site.author.medium }}" title="medium">
              <span class="fa-stack fa-lg" aria-label="Logo riferito al sito medium, raffigura una M maiuscola bianca su sfondo nero." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-medium fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Canale Medium
            </a><span>per leggere le nostre storie</span>
          </li>
          {% endif %}
          {% if site.share-links-active.rss %}
          <li>
          <a href="http://feeds.feedburner.com/covid19ita_segnalazioni" title="RSS">
              <span class="fa-stack fa-lg" aria-label="Logo riferito a RSS, raffigura un cercio e due cerchi semi concentrici paralleli come a rappresentare un antenna che trasmette messaggi." role="img">
              <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
              <i class="fa fa-rss fa-stack-1x fa-inverse" aria-hidden="true"></i>
            </span>&nbsp;&nbsp;Feed RSS
          </a><span>per rimanere aggiornato sulle nostre segnalazioni</span>
          </li>
          {% endif %}
          {% if site.author.flickr and site.share-links-active.flickr %}
           <li>
            <a href="https://www.flickr.com/photos/{{ site.author.flickr }}" title="Flickr un sito pieno di fotografie di viaggiatori e appassionati di fotografie.">
              <span class="fa-stack fa-lg" aria-label="Logo riferito a flickr" role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-flickr fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Gruppo Flickr
            </a><span>per caricare foto e media</span>
          </li>
          {% endif %}
          {% if site.author.waze and site.share-links-active.waze %}
              <li>
            <a href="{{ site.author.waze }}" title="Waze">
              <span class="fa-stack fa-lg" aria-label="Logo riferito a Waze ottimo per controllare il traffico automobilistico" role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-car fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Waze
            </a>per informazioni su tutto ciò che riguarda la viabilità
          </li>
          {% endif %}
                 <li>
            <a itemprop="sameAs" href="{{ site.author.email }}" title="Email">
              <span class="fa-stack fa-lg" aria-label="Logo raffigurante una busta, email.">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-envelope fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Email
            </a>per segnalare contenuti da rimuovere o scriverci
          </li>
          {% if site.author.archiveorg and site.share-links-active.archiveorg %}
          <li>
            <a itemprop="sameAs" href="{{ site.author.archiveorg }}" title="archive.org archivio di internet.">
              <span class="fa-stack fa-lg" aria-label="Logo riferito al sito archive.org, raffigura un tempio." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-archive fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Archive.org
            </a>archivio dati
          </li>
          {% endif %}
          {% if site.author.telegram_group and site.share-links-active.telegram_group %}
	         <li>
            <a href="{{ site.author.telegram_group }}" title="Bot Telegram un robot testuale che risponde automaticamente.">
              <span class="fa-stack fa-lg" aria-label="Logo riferito al RoBot testuale su Telegram." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-paper-plane fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Gruppo Telegram
            </a><span>per coordinarci internamente</span>
          </li>
          {% endif %}
          <p>Tutto ciò che ci invii sarà gestito dal nostro team, che potrà provvedere alla pubblicazione delle informazioni sul sito appena possibile. Ricordati che usando i nostri canali accetti automaticamente di sottoscrivere l'<a href="{{ site.url }}/legal_segnalazioni/">informativa legale</a> per le informazioni di questo progetto.</p>
</div>
