---
lang: it
layout: issuelist_embed
title: Emergenza coronavirus - Servizi e iniziative solidali per migranti e rifugiati
permalink: /migranti-rifugiati-base/
issuecategories: 
        - migrants and refugees
        - psychological support
        - deliveries and services 
---

{%- if page.issuecategory != blank -%}

    {% assign issuecategories = "" | split: "," %}
    {% assign tmpcategory = "" | split: "," %}
    {%- assign tmpcategory = tmpcategory | push: page.issuecategory -%}
    {%- assign tmpcategory = tmpcategory | push: site.data.cfg.issuecategories[page.issuecategory] -%}
    {%- assign issuecategories = issuecategories |  push: tmpcategory -%}

{%- elsif page.issuecategories != blank -%}

    {% assign issuecategories = "" | split: "," %}
    {% for category in page.issuecategories %}
    {% assign tmpcategory = "" | split: "," %}
    {%- assign tmpcategory = tmpcategory | push: category -%}
    {%- assign tmpcategory = tmpcategory | push: site.data.cfg.issuecategories[category] -%}
    {%- assign issuecategories = issuecategories |  push: tmpcategory -%}
    {% endfor %}

{%- elsif page.displayname != blank and page.markericon != blank -%}

    {% assign issuecategories = "" | split: "," %}
    {% assign tmpcategory = "" | split: "," %}
    {%- assign tmpcategory = tmpcategory | push: "page" -%}
    {%- assign tmpcategory = tmpcategory | push: page -%}
    {%- assign issuecategories = issuecategories |  push: tmpcategory -%}

{%- else -%}

    {%- assign issuecategories = site.data.cfg.issuecategories -%}

{%- endif -%}

