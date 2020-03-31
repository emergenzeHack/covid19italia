---
layout: page
title: "Coronavirus Emergency: how activate your community in other countries"
subtitle: "Contribute to Covid 19Italia.help!"
permalink: en/contribute/
lang: en
---

The project is open in terms of code, data and in terms of approaches to informations and process to collect.

We need the help of active citizens of the world in other to be help people in different countries.

Our project is [Github](www.github.com) based. If you don't know Github you can look at [this video](https://www.youtube.com/watch?v=noZnOSpcjYY&t) as introduction.

Here a simple diagram of how our project works.

![](https://raw.githubusercontent.com/emergenzeHack/covid19italia/master/images/process1.jpg)


## Are you are interested in development of this project?

You can contribute in different ways:

* Do you have a civic hackers community to develop coding? Ok. You can start to open issues, discuss here and make a part of  job on Github [here](https://github.com/emergenzeHack/covid19italia/issues).

* Do you have other active citizens or associations? Ok. You can also contribute to the translation in your country languages, translate part of the website and then you can pull request in the Github Repo Or you can send your translation with a specific issue [here](https://github.com/emergenzeHack/covid19italia/issues) asking to add the translation.

## How organize your community to crowdsource reports?

In addition to civic hacker community the most important part of the project is composed by a Reports Moderation Team.

You need one Moderation Team active for your country (in order to moderate and verify every report that you receive).

When you are ready with this please open an issue [here](https://github.com/emergenzehack/covid19italia/issues/new?title=%5BNewCountryCollaboration%5D), describing your country and your situation so we can abilitate the possibility to send reporting and collect your data for your country using the same process and platform!

Here the basic step to integrate you in our platform (we can support you in this procedure), you need:

### On Telegram
- At least a [Telegram](https://web.telegram.org/#/login) account to contact us. We will create a Telegram group for coordination.

### On Github
- At least a [Github](www.github.com) Account to moderate issues and make modifications to the web platform. We will create a Github editor group for reports management.

- A Github Repo to store the reports [like this one]
(https://github.com/emergenzeHack/covid19italia_segnalazioni/issues) is necessary in order to organize reporting with labels and in order to make moderation with your moderation team.

- A Github Repo to store platform data [like this one](https://github.com/emergenzeHack/covid19italia_data) to store moderated reports and platform data.

- A branch of our master platform branch on Github. We will provide a branch. For the domain, we can provide you a web address and/or you can indicate your specific domain, we try to manage a redirect on the right web page.

- Be sure that you have a list of LABELS to organize your reports in categories (example: request of help, news, fake news etc etc...).

#### Technical remarks for GitHub Side

- Github Repo of the data as used to store you reports dataset and is used by Github Repo of website to build website.
- In the Github Repo to store reports as issue you have to define a list of LABELS to categorized the issues. They will be the tags that you'll can manage in the frontend of the website. Remember to define a label "Approvato" to accept a reports.
Labels should be the same listed in "categorieissue" tag in _config.yml file inside the repo of the website.
- In the repo of the website you have to do at least this actions on the frontend sites
  - Adjust _config.yml file as you prefer
  - For each page of reports categories you must configure the permalink, title and the relative LABEL in the page
  - Adjust the maps on your country

### On Kobo Toolbox
- At least a [Kobo](https://kobo.humanitarianresponse.info/) Toolbox account in order to manage your webforms and translate them. We will share basic form that you have to translate in your language in this way:
  - Go into your Kobo Profile and search the web form shared by us.
  - Under "Current version" of Web Form click on the world icon "Manage Translations"
  - Add a "your" language on the Kobo Forms
  - Near the desired language, click again the world icon "Update Translations" and add translation
  - Set "your" language as default
  - Re-deploy the form

**From the moment when you will integrate your Moderation Team will be able to see in the Github Reports repo your reports, will accept the reports and then the reports will be publish on the website.**

Here a little diagram to explain how the project is organized in multi-country configuration. We wait you! Thanks!

![](https://raw.githubusercontent.com/emergenzeHack/covid19italia/master/images/diagramma%20(1).png)