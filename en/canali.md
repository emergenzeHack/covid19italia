---
lang: en
layout: page
title: Contacts
subtitle: Contact Covid19Italia.help and follow our social media
permalink: en/canali/
---

<div class="segnala">
<p>Here channels to conctact, be informed, report info or needs: </p>
     <ul>
         {% if site.author.facebook %}
          <li>
            <a href="https://www.facebook.com/{{ site.author.facebook }}" title="Facebook">
              <span class="fa-stack fa-lg" aria-label="Logo riferito al sito facebook, il carattere f dentro un quadrato blu." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-facebook fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Facebook Page
            </a><span>to follow us on Facebook</span>
          </li>
         {% endif %}
         {% if site.author.facebook_group %}
          <li>
            <a href="https://www.facebook.com/groups/{{ site.author.facebook_group}}" title="Facebook">
              <span class="fa-stack fa-lg" aria-label="Logo riferito al sito facebook, il carattere f dentro un quadrato blu." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-facebook fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Facebook Group
            </a><span>to discuss on Facebook</span>
          </li>
         {% endif %}
         {% if site.author.androidapp %}
          <li>
            <a href="https://play.google.com/store/apps/details?id={{ site.author.androidapp }}&hl=it_it" title="Android App">
              <span class="fa-stack fa-lg" aria-label="Logo raffigurante il market di applicazioni android." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-android fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;App Android
            </a><span>to see contents with app android</span>
          </li>
         {% endif %}
         {% if site.author.github %}
          <li>
            <a href="https://github.com/{{ site.author.github }}" title="GitHub">
              <span class="fa-stack fa-lg" aria-label="Logo riferito al sito github, raffigura un gatto con i tentacoli." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-github fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Repo GitHub
            </a><span>to collaborate for developments</span>
          </li>
          {% endif %}
          {% if site.author.twitter %}
          <li>
            <a href="https://twitter.com/{{ site.author.twitter }}" title="Twitter">
              <span class="fa-stack fa-lg" aria-label="Logo riferito al sito twitter, un uccello di colore celeste." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-twitter fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Twitter
            </a><span>to follow on Twitter</span>
          </li>
          {% endif %}
           {% if site.author.instagram %}
          <li>
            <a href="https://www.instagram.com/{{ site.author.instagram }}" title="Instagram un social network pieno di fotografie.">
              <span class="fa-stack fa-lg" aria-label="Logo riferito a instagram, raffigura una macchina fotografica stilizzata." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-instagram fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Instagram
            </a><span>to see our pics and Instagram stories</span>
          </li>
          {% endif %}
           {% if site.author.messenger %}
          <li>
            <a href="https://m.me/{{ site.author.messenger }}" title="Messenger una chat">
              <span class="fa-stack fa-lg" aria-label="Logo riferito a Messanger, raffigura una nuvola come quella dei fumetti." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-bullhorn fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Facebook Messenger
            </a><span>to be updated on Messenger.</span>
          </li>
          {% endif %}
          {% if site.author.telegram %}
          <li>
            <a href="{{ site.author.telegram }}" title="Telegram una chat.">
              <span class="fa-stack fa-lg" aria-label="Logo riferito a telegram, raffigura un aereoplano di carta stilizzato." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-paper-plane fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Telegram Channel
            </a><span>to receive our news on Telegram</span>
          </li>
          {% endif %}
          {% if site.author.telegram_bot %}
          <li>
            <a href="http://telegram.me/{{ site.author.telegram_bot }}" title="Bot Telegram">
              <span class="fa-stack fa-lg" aria-label="Logo riferito al RoBot testuale su Telegram." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-paper-plane fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;BOT Telegram
            </a><span>per inviare segnalazioni con smartphone dal "campo"</span>
          </li>
          {% endif %}
          {% if site.author.medium %}
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
          </a><span>to be updated with our reports</span>
          </li>
          {% endif %}
          {% if site.author.flickr %}
           <li>
            <a href="https://www.flickr.com/photos/{{ site.author.flickr }}" title="Flickr un sito pieno di fotografie di viaggiatori e appassionati di fotografie.">
              <span class="fa-stack fa-lg" aria-label="Logo riferito a flickr" role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-flickr fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Gruppo Flickr
            </a><span>to load photos</span>
          </li>
          {% endif %}
          {% if site.author.telegram_group %}
	         <li>
            <a href="{{ site.author.telegram_group }}" title="Bot Telegram un robot testuale che risponde automaticamente.">
              <span class="fa-stack fa-lg" aria-label="Logo riferito al RoBot testuale su Telegram." role="img">
                <i class="fa fa-circle fa-stack-2x" aria-hidden="true"></i>
                <i class="fa fa-paper-plane fa-stack-1x fa-inverse" aria-hidden="true"></i>
              </span>&nbsp;&nbsp;Telegram Group
            </a><span>to coordinate on Telegram</span>
          </li>
          {% endif %}
     </ul>
          <p>Tutto ciò che ci invii sarà gestito dal nostro team, che potrà provvedere alla pubblicazione delle informazioni sul sito appena possibile. Ricordati che usando i nostri canali accetti automaticamente di sottoscrivere l'<a href="{{ site.url }}/legal_segnalazioni/">informativa legale</a> per le informazioni di questo progetto.</p>
</div>
