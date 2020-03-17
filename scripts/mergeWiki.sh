#!/bin/bash

git clone https://github.com/emergenzeHack/covid19italia.wiki.git
markdown-pp templateWiki.mdpp -o ../wiki.md
rm -rf covid19italia.wiki
