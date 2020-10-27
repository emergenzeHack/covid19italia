#! /bin/bash

CFGFILE="${1}"
OUTBASEDIR="${2}"

for entry in $(jq -cr '.[] | @base64' "${CFGFILE}")
do
    url=$(echo "${entry}" | base64 -d | jq -r '.url')
    path=$(echo "${entry}" | base64 -d | jq -r '.path')

    echo "${url} -> ${path}"
    wget -O "${OUTBASEDIR}/${path}" "${url}"
done
