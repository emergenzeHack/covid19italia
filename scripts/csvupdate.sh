#! /bin/bash

logger reset repo
git clean -fxd
git reset --hard HEAD
git pull

logger github2CSV
(cd .. && python covid19italia/scripts/github2CSV.py covid19italia/_data/issues.csv covid19italia/_data/issuesjson.json covid19italia/_data/issues.geojson)


sed -i 's/\r$//g' _data/*.csv

logger push
git add _data
#git add vittime.md
git commit -m "auto CSV update $(date -Iseconds)"
git pull --rebase
git push

logger clean
git clean -fxd
git reset --hard HEAD

