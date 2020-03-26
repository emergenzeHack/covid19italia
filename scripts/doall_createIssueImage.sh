jq -cj  '.[] | select( .issue.labels | contains("accettato")) | .number,.issue.title,.issue.labels | tojson+"\u0000"'  < _data/issuesjson.json   | xargs -0 -n3 -P4 scripts/createIssueImage.sh img/templates/issue_templatew.png 900x490 "+80+50" images/issues/

