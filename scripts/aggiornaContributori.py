#!/usr/bin/env python

import csv
import os
from github import Github

g = Github(os.getenv("GITHUB_TOKEN"))
repo = g.get_repo(os.getenv("GITHUB_REPOSITORY", "emergenzeHack/covid19italia"))

contributors = []
for contributor in repo.get_contributors():
    name = contributor.name or contributor.login
    contributors += [{ 'name': name, 'url': contributor.html_url }]

# FIXME get those from issues
contributors += [
                 { 'name': 'Andrea Borruso' },
                 { 'name': 'Chiara Parapini' },
                 { 'name': 'Cristina Galasso' },
                 { 'name': 'Donata Columbro' },
                 { 'name': 'Marieva Favoino' },
                 { 'name': 'luciaroma' },
                 { 'name': 'Saraveg' },
                ]

with open(os.path.dirname(__file__) + '/../_data/contributori.csv', 'w') as csv_file:
    fieldnames = ['name', 'url']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(contributors)
