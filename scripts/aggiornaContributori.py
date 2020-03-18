#!/usr/bin/env python

import csv
import os
from github import Github

def getGitHubData(listOfUsernames):
    contriblist = []
    for contributor in listOfUsernames:
        avatar_url = g.get_user(contributor.login).avatar_url

        contributorObj = {
            'name': contributor.name or contributor.login,
            'url': contributor.html_url,
            'avatarUrl': avatar_url
        }
        
        contriblist.append(contributorObj)
    return contriblist

g = Github(os.getenv("GITHUB_TOKEN"))
repoCore = g.get_repo(os.getenv("GITHUB_REPOSITORY", "emergenzeHack/covid19italia"))
repoApp = g.get_repo(os.getenv("GITHUB_REPOSITORY", "emergenzeHack/covid19italia_app"))

# GitHub usernames of the Editors team
editorsTeam = ["cristigalas",
               "chiccap",
               "favoeva",
               "Saraveg",
               "claudiamazzantiact",
               "luciaroma"]

coreContributors = getGitHubData(repoCore.get_contributors())
# appContributors = getGitHubData(repoApp.get_contributors())
#editorsContributors = getGitHubData(editorsTeam)



with open('_data/contributori.csv', 'w') as csv_file:
    fieldnames = list(coreContributors[0])
    print(fieldnames)
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(coreContributors)
