#!/usr/bin/env python

import csv
import os
from github import Github

g = Github(os.getenv("GITHUB_TOKEN"))
repoSegnalazioni = g.get_repo(os.getenv("GITHUB_REPOSITORY", "emergenzeHack/covid19italia_segnalazioni"))

labels = repoSegnalazioni.get_labels()

data = []

data.append({ 'Tipo': "Segnalazioni totali", 'Valore': repoSegnalazioni.get_issues().totalCount })

for label in labels:
	print(label.name)
	count = repoSegnalazioni.get_issues(labels=[label.name]).totalCount
	if count != 0:
		data.append({ 'Tipo': label.name,
					  'Valore': count} )

print(data)

with open(os.path.dirname(__file__) + '/../_data/statisticheSegnalazioni.csv', 'w') as csv_file:
	fieldnames = ["Tipo", "Valore"]
	writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

	writer.writeheader()
	writer.writerows(data)