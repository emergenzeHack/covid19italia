---
layout: page
title: Technical Documentation
permalink: /en/wiki/
lang: en
---


Welcome in Covid19Italia wiki. Covid19Italia is a community based on social media, born with the purpose of sharing useful and verified information on Corona virus in Italy.

The project is completely open and anyone can provide support using the following guidelines.

**The site**

Our site has been created with [Github](http://www.github.com/).

**Get involved**

In order to be added at the list of the repository developers open an issue here ([qui](https://github.com/emergenzehack/covid19italia/issues/new?title=%5Brichiesta%20iscrizione%5D)), ask to get the access sharing your [Telegram](https://web.telegram.org/) username.

**Help us in improving it**

Covid19Italia is an ongoing project. If you want to suggest improvements open an issue here ([issue qui](https://github.com/emergenzeHack/covid19italia/issues)). In the same page you will see the reports entered by other users. From there you can realize what it is still possible to implement and fix.

Github repositories we are using are the following ones :


*   [QUESTO](https://github.com/emergenzeHack/covid19italia) This one for the website development
*   [QUESTO](https://github.com/emergenzeHack/covid19italia_segnalazioni) This one for collecting and controlling the reports.
*   [QUESTO](https://github.com/emergenzeHack/covid19italia_data) This one in order to archive the open data we created
*   [QUESTO](https://github.com/emergenzeHack/covid19italia_form) This one for the development of the reporting forms
*   [QUESTO](https://github.com/emergenzeHack/covid19italia_app) This one for the development of a mobile app


# Contributing

Welcome to the wiki of Covid19Italia, a social media-based community created to share useful and verified information about the corona virus in Italy.

The project is completely open and anyone can contribute according to these guidelines.


# The site

Our site is created with [Github]([http://www.github.com/](http://www.github.com/)).


# Become a contributor

To be added to the developers list of the repository open an issue [here](https://github.com/emergenzehack/covid19italia/issues/new?title=%5Brichiesta%20iscrizione%5D), request access by leaving your [Telegram](https://web.telegram.org/) username.


# Help us to improve

Covid19Italia is a project in progress, to suggest improvements open an issue [here](https://github.com/emergenzeHack/covid19italia/issues). On the same page you can see the reports opened by other users; from there you can see what still needs to be done and fixed.

The Github repositories we use are



*   THIS for the development of the website
*   THIS for the collection and moderation of alerts
*   THIS for the storage of open data provided by us
*   THIS for the development of the alert entry form
*   THIS for the development of a mobile APP

Thank you, we're waiting for your help!


# Reuse

Covid19Italia is an opensource project composed of various integrated applications. This WIKI allows you to understand how the project is structured and how to reuse it. TerremotoCentroItalia is licensed under Creative Commons Attribution 3.0 (CC BY) whose text is available at [this address](https://creativecommons.org/licenses/by/3.0/it/). Unless otherwise specified (e.g. in the source code repositories) we ask you to comply with the criteria of this license if you reuse part of our project.


## Index of contents



*   Open an Issue
*   How to use GitHub
*   Working on Reports
*   How the TCI method works in brief
*   Convert a Google Docs document to Markdown
*   How to insert an element in Press
*   Develop locally on site


# Open an Issue

Issues can be used to keep track of bugs, improvements or other project requests.

All GitHub users can create an issue for a public project.



*   On Github navigate to the main project page.
*   Under the project name, click on the Issues tab of the project.
*   Click the green "New Issue" button.
*   Enter a title and description for your issue.

If you are a project maintainer you can assign the issue to someone, associate it with milestones or add a label.

You can attach a file by dragging it into the description field.

When you are done click on "Submit new issue".

Note: project maintainers can



*   Create a template for issues in a project. Templates include commands that the project maintainer chooses to display in the issue description.
*   Disable issues for a project.


# How do you use GitHub?

This page is a mirror of [this simple tutorial](https://guides.github.com/activities/hello-world/) and describes the first steps to start using Github as a shared design tool.


# Working on reports

Preamble:

This document is intended for the team working on Reports. Other users do not have permission to perform the operations described here, but they can freely leave a comment on any Issue contributing to it. For example, at [this link](https://github.com/emergenzeHack/covid19italia_segnalazioni/issues?q=is%3Aissue+is%3Aopen+label%3A%22Posizione+mancante%22) you can see all the Reports that are still missing a position. You can suggest coordinates in a comment. A moderator will take over and apply your suggestions as soon as possible.

To join the team of Moderators, make sure you are an active member of the community, that you have contributed previously and that you enter the group chat of contributors.


## Mechanism

Each compilation of a Covid19Italia form generates - after about 30 seconds - a new Issue [here](https://github.com/emergenzeHack/covid19italia_segnalazioni/issues).

Different labels are applied to these Issues to describe their nature and approval status (which determines their final publication on the site, on bulletins, on Twitter, on Telegram channel and bot,...).

This allows everyone to collaborate in the classification, moderation and community verification of the reports. A history of all changes, operations and moderations on each Issue is available.

All it takes is an account on GitHub and a web browser, no knowledge or IT tool is required.


## Structure

Reports must maintain this structure:

```

&lt;pre>&lt;yamldata>

Field1: Field value1

Field2: Field value2

&lt;/yamldata>&lt;/pre>

```

Pay attention to the following conventions when changing the content of an Issue:



1. Fields that go on multiple lines must be delimited by a '. Example:

```

Description: 'The content of this field

spans multiple

lines

'

Field2: This field is on one line only

```

Attention: Fields on several lines must be delimited by `'` (one at the beginning and one at the end of the field). `'` is used to delimit the content of a field so it cannot be used with the normal apostrophe function inside. To use `'` literally, and not as a delimiter, use `\`.

For example, if I wanted to write `l’altro` one once per line, in a multi-field field, I would have to do this:

```

'

L\'altro

L\'altro

'

```

`'` is used as a delimiter, while it is written `\` to use it literally. In the final report it will then be shown simply as `'`.



1. The title of the Issue becomes the title of the report on the front end.
2. Changes (including publication/de-publication) appear on the final site after a maximum of 15 minutes. Use CTRL+F5 or anonymous navigation mode if you do not see any changes. If things still don't come back to you after this, proceed to open Issue and report the problem. Issue on forms (fields, structure, missing data) should be opened on [covid19italia_forms]([https://github.com/emergenzeHack/covid19italia_form/issues](https://github.com/emergenzeHack/covid19italia_form/issues)).
3. If you need to change the Labels that are already assingned to the Issue (the ones you see already automatically assigned) please report it [here]([https://github.com/emergenzeHack/covid19italia_form/issues/new](https://github.com/emergenzeHack/covid19italia_form/issues/new))
4. Do not remove the Label "form", it helps us to investigate the origin of the reports.


# Geolocation

There are some issues that have a "Location" field, like this [one](https://github.com/emergenzeHack/covid19italia_segnalazioni/issues/332).

And they end up on the map [here]([https://www.covid19italia.help/issues/](https://www.covid19italia.help/issues/)).


## Check geolocation

If the report does not have a geolocation, the script tries to search for municipality/city names within the various fields filled in. If it finds something, it adds the location itself. When it does, the “Posizione da verificare” label is applied and the bot will comment asking you for confirmation, also giving you a link to those coordinates to see if they make sense or not.

If no position is found even after this attempt, the “Posizione Mancante” label is applied so that you can filter out any that still need it.


## Add geolocation

Therefore, issues marked with the “Posizione Mancante” label need manual intervention to add the position.


## How to find the coordinates of a location?

Let's take for example [this](https://www.covid19italia.help/issues/) report on Milan.

You can use this site: [Nominatim](https://nominatim.openstreetmap.org/).

In the top right corner there is a button called "Show map bounds". When pressed, a rectangle containing the coordinates appears. The most important line is "Last click".

There are two numbers, separated by a comma, are latitude and longitude. Copy them.


### Add the coordinates to the report

On the Issue, click the “...” button at the top right of the Issue, then "edit".

Now add (or edit) the ‘Posizione’ field, adding the coordinates obtained earlier:

```

...

Posizione: 43.768137 11.241812

```

The first value is Latitude, the second is Longitude (mandatory). The third and fourth indicate Altitude and Accuracy (meters). The latter two are optional.

Example:


### Manual entry of region and/or province and/or municipality

**How to know which region/province/commune has identified the system?**

By looking on the site at www.covid19italia.help/issues/ (for example https://www.covid19italia.help/issues/748/) if the report has a position already entered, the values ‘Provincia’ and ‘Region’ are those recognized based on geographical data. **In this case, if there are errors, it would be more useful to fix the position**.

There may be reports that have a region or province or municipality of reference, but for which it makes no sense to enter a pair of coordinates. In order for these reports to be listed on the page by region or province anyway, you can enter a field in the data of type

```

regione_manuale: Veneto

```

or

```

provincia_manuale: Bologna

```

or

```

comune_manuale: Cento

```

(Of course, since you do not have a location, the report will not be displayed on the map.)

**N.B. Pay attention to the spelling of the name: it must be exactly what is used by the other reports.**

Final example of a report:

```

&lt;pre>&lt;yamldata>

Da_chi_offerta: comitati di quartiere

Descrizione: 'Iniziativa di cittadini e cittadine, comitati ed associazioni del Quartiere

 (Centro storico) di Firenze: consegnano cibo e beni primari a chi ne fa richiesta.'

Destinatari: Consegna di cibo e generi di prima necessità

Link: https://google.it

Natura: solidale

Posizione: 43.768137 11.241812

Tipo_di_soggetto: privato

Titolo: Serve aiuto?

&lt;/yamldata>&lt;/pre>

```


### Policies

These are some of the policies, guidelines and rules which have been decided:



*   We do not accept reports of scientific research ([https://github.com/emergenzeHack/covid19italia_segnalazioni/issues/315#issuecomment-598456738](https://github.com/emergenzeHack/covid19italia_segnalazioni/issues/315#issuecomment-598456738)).
*   If some fields seem to be invalid, try to correct them or search for more information on Google from the title, DO NOT close the Issue immediately if the link fails or similar problems occur.

To discuss or provide feedback, open an Issue.


## How the TCI method works (in short)

This project is "cloned" from a precedent used for the 2016 earthquake in central Italy called TCI.

TCI (terremotocentroitalia.info) is a "dynamic" site based on:



*   a management of reports through issue github and from some scripts (from now on "backend")
*   a cataloguing and pagination of alerts by jekyll (from now on "frontend")


### Backend

The backend is directly represented by a github repo of which only the reporting part is used (you can see it [here](https://github.com/emergenzeHack/terremotocentro_segnalazioni/issues)).

Pros:



*   the system is robust, functional, managed by others
*   very easy to use, there are several people who already have experience
*   possibility to add tags to reports for cataloguing
*   API to download

Against:



*   to insert "machine readable" info in the reports we use YAML, which must be managed by an external editor
*   if the YAML breaks, you have to intervene "by hand".


### Conversion Script

Every 5 minutes, a [script](https://github.com/emergenzeHack/covid19italia/blob/master/scripts/csvupdate.sh):



*   download all the reports from github
*   decode the YAML file
*   creates a JSON array that contains the alerts and the YAML file converted to JSON
*   commits any differences on the GIT repo, triggering webhook and new build


### Frontend

Since Jekyll reads JSON directly, there are several pages that filter JSON and create HTML with lists, maps, etc.

The frameworks used are:



*   bootstrap for the layout
*   openlayers/leaflet for maps

Pros:



*   very fast to serve
*   you can rely on external sites like netlify
*   practically unbreakable

Against:



*   in moments of maximum usage, the update is every 5 minutes


## Things that could be improved



*   Processing issues on the site could be done more efficiently using github hooks and any DB to store data, so you can have faster updates. The fact remains that when the site is "stopped", it doesn't make sense to have a DB to query every moment


## Convert a Google Docs document to Markdown

Here are some simple steps to convert a document made in Google Docs into a format compatible with this WIKI or as a blog post of this site so you can continue to use Google Docs if you use it normally to write and then publish content on covid19italia.help.



*   Install the "Docs to markdown" plugin in Add-ons (from the Additional Components menu -> Install Add-ons look for "Docs to markdown".
*   once the document in Google Doc is ready open the Additional Components menu select "Docs to markdown" and then "Convert".
*   From the left panel press the Markdown button.

Now select all the text that is translated below...copy it with a normal "Copy" : this is your text in a Github compatible language!

Go for example to the WIKI section, create a new page by giving it a title and paste the text. At the end save the page and you will find it published.

Note: the guide on how to use "Docs to markdown" in detail can also be found [here](https://github.com/evbacher/gd2md-html/wiki#installing-docs-to-markdown).

Done it! Easy, right?


## How to insert an element in Press

To insert an item in the [PRESS](https://www.covid19italia.help/about/#press) table proceed as follows:



*   Go to this PRESS [file](https://github.com/emergenzeHack/covid19italia_data/blob/master/press.csv)
*   Click the pencil icon to edit the file on Github
*   Add a line to the file and insert in sequence date,source,title,comma separated links. Note: there must be no additional commas except those separating the 4 fields.
*   Click on the "Commit changes" or "Propose changes" button at the bottom of the page.
*   If a green "Create Pull Request" button is provided, press it and wait for the administrators to validate the change.

Done.


## Develop locally on site

This short guide will explain how to create a copy of the site on your computer. In this way the changes to the code will be immediately visible in your local copy, and you can test all the improvements you are planning. Let's get started!


### Prerequisites

You will need to install some development software on your computer. On the linked pages you will find all the instructions in detail.



*   The [Ruby](https://www.ruby-lang.org/it/documentation/installation/) programming language
*   The [git](https://git-scm.com/downloads) distributed development system

A minimum of familiarity with the command line terminal is required for the next steps. Nothing special, it is a tool that allows us to give commands to the computer in the form of text instead of clicking with a mouse in a window. Mac and Linux users should already have the Terminal application installed; for Windows users the git installation already includes a terminal similar to the Linux terminal.

We will also gloss over many details of git and Github, referring you to the other guide in our wiki.

The commands to insert in the terminal (also copy-paste) will be indicated as follows: `example command`.


### Preparation of the environment

First we verify that we have Ruby and bundler installed, which in turn will help us install all the dependencies we need.

On Mac with Homebrew:

```sh

brew install ruby

```

install the gem bundle

```sh

sudo gem install bundler:1.17.3

```

install command line developer tools

```sh

xcode-select --install

```

On Ubuntu:

```sh

sudo apt install build-essential git ruby-full ruby-bundler zlib1g-dev

```

Let's fork the repository on github, then clone our fork locally (remember to use your real username):

```sh

git clone https://github.com/username/covid19italia.git

```

If you work on data (_data/) you will need to fork and work on covid19italia_data instead of covid19italia.

Let's go inside the new folder:

```sh

cd covid19italia

```

We install all project dependencies:

```sh

bundle install --path vendor/bundle

```

Let's get the site up and running!

Let's execute, always in the folder `covid19italia`:

```sh

bundle exec jekyll serves

```

The program will then print on screen the address to open in the browser, which will be of the type http://127.0.0.1:4000/.

That's it, that's it! Good job :muscle:


### Get a build

To get a static version of the site you need to run the build process.

This is the same process that is performed when the update is released on the public version of the site.

To build locally you need to run this command:

```sh

bundle exec jekyll build

```


### Troubleshooting errors


#### To open the site from another computer on the network

If you run the site on a machine running Linux and developed under Windows you have to add -H 0.0.0.0 to the command you need, like:

```sh

bundle exec jekyll serves -H 0.0.0.0

```

In this way you can open the site from any location connected to your network and not only from the localhost. Useful to test the changes with mobile phones, tablets or other browsers.
