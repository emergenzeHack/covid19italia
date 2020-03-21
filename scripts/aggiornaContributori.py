#!/usr/bin/env python

import csv
import os
from github import Github

def getGitHubData(listOfUsernames):
    contriblist = []
    for contributorName in listOfUsernames:
        contributor = g.get_user(login=contributorName)

        contributorObj = {
            'name': contributor.name or contributor.login,
            'url': contributor.html_url,
            'avatarUrl': contributor.avatar_url
        }
        
        contriblist.append(contributorObj)
    return contriblist

def writeCsv(contribData, filename):
    with open(os.path.dirname(__file__) + '/../_data/' +filename, 'w') as csv_file:
        fieldnames = list(contribData[0])
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(contribData)

g = Github(os.getenv("GITHUB_TOKEN"))

repoCore = g.get_repo(os.getenv("GITHUB_REPOSITORY", "emergenzeHack/covid19italia"))
repoApp = g.get_repo(os.getenv("GITHUB_REPOSITORY", "emergenzeHack/covid19italia_app"))

# GitHub usernames of the Editors team
editorsTeam = ["cristigalas",
               "chiccap",
               "favoeva",
               "Saraveg",
               "claudiamazzantiact",
               "luciaroma",
               "FrancescaZambi89"]

coreTeam = []
excludeList = ["ehack-italy"]
for contrib in repoCore.get_contributors():
    # Evita duplicati
    if contrib.login not in editorsTeam and contrib.login not in excludeList:
        coreTeam.append(contrib.login)

coreContributors = getGitHubData(coreTeam[:10])
#appContributors = getGitHubData(repoApp.get_contributors())
editorsContributors = getGitHubData(editorsTeam)

writeCsv(coreContributors, 'contributorsCore.csv')
writeCsv(editorsContributors, 'contributorsEditors.csv')
#writeCsv(appContributors, 'contributorsApp.csv')
