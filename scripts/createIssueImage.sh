#! /bin/bash

template_img="${1}"
text_size="${2}"
text_pos="${3}"
destdir="${4}"
number="${5}"
title="$(sed 's/^"\(.*\)"$/\1/' <<< ${6})"
labels="${7}"


destfilename="${number}.png"

TMPFILE=/tmp/${number}caption_img.png
TMPTEMPLATE=/tmp/${number}tmpl_img.png
TMPTEMPLATE2=/tmp/${number}whtmpl_img.png

trap 'rm -f ${TMPFILE} ${TMPTEMPLATE} ${TMPTEMPLATE2}' EXIT

case "${labels}" in
    *"Supporto psicologico"*) BACKCOLOR=blue;FRONTCOLOR=white;;
    *"Servizi e iniziative solidali"*) BACKCOLOR=cyan;FRONTCOLOR=black;;
    *"Raccolte fondi"*) BACKCOLOR=green;FRONTCOLOR=white;;
    *"Notizie utili"*|*"Informazioni utili"*) BACKCOLOR=yellow;FRONTCOLOR=black;;
    *"Attivita culturali e ricreative"*) BACKCOLOR="#FFC0CB";FRONTCOLOR=black;;
    *"Fonti istituzionali"*) BACKCOLOR=grey;FRONTCOLOR=black;;
    *"Fake News"*) BACKCOLOR=purple;FRONTCOLOR=white;;
    *) BACKCOLOR=black;FRONTCOLOR=white
esac

echo "Building image for n ${number} title ${title} labels ${labels} BACKCOLOR ${BACKCOLOR} FRONTCOLOR ${FRONTCOLOR}"

new_templmd5=$(md5sum ${template_img} | awk '{ print $1 }')
echo new_templmd5 "${new_templmd5}"

destlogdir="_buildlogs/${destdir}/"
destlogname="${destlogdir}/${destfilename}.json"
if [ ! -d "${destlogdir}" ]; then
    mkdir -p "${destlogdir}"
else
    if [ -f "${destlogname}" ]; then
        old_templmd5=$(jq -r .templmd5 < "${destlogname}")
        old_number=$(jq -r .number < "${destlogname}")
        old_title=$(jq -r .title < "${destlogname}")
        old_BACKCOLOR=$(jq -r .BACKCOLOR < "${destlogname}")
        old_FRONTCOLOR=$(jq -r .FRONTCOLOR < "${destlogname}")
        old_filemd5=$(jq -r .filemd5 < "${destlogname}")
        echo old_templmd5 "${old_templmd5}"
        echo new_templmd5 "${new_templmd5}"
        echo old_number "${old_number}"

        if [ "${old_templmd5}" == "${new_templmd5}" -a "${old_number}" == "${number}" -a "${old_title}" == "${title}" -a "${old_BACKCOLOR}" == "${BACKCOLOR}" -a "${old_FRONTCOLOR}" == "${FRONTCOLOR}" ]; then
            if [ -f "${destdir}/${destfilename}" ] ; then
                new_filemd5=$(md5sum "${destdir}/${destfilename}" | awk '{ print $1 }')

                if [ "${new_filemd5}" == ${old_filemd5} ]; then
                    echo SKIP existing
                    exit
                fi
            fi
        fi
    fi
fi

if [ ${FRONTCOLOR} = "black" ]; then
convert "${template_img}" -fuzz '10%' -fill "${BACKCOLOR}" -opaque 'white' "${TMPTEMPLATE}"
else
convert "${template_img}" -negate -colorspace RGB "${TMPTEMPLATE2}"
convert "${TMPTEMPLATE2}" -fuzz '10%' -fill "${BACKCOLOR}" -opaque black "${TMPTEMPLATE}"
fi

convert -background transparent -fill "${FRONTCOLOR}" -font Lato-Regular -size "${text_size}" \
          caption:"${title}" \
          "${TMPFILE}"

#convert  "${TMPTEMPLATE}" ${TMPFILE} -geometry "${text_pos}" -quality 9 -composite "${destdir}/${destfilename}"
#convert  "${TMPTEMPLATE}" ${TMPFILE} -geometry "${text_pos}" -depth 2 -colors 4 -quality 9 -composite "${destdir}/${destfilename}"
convert  "${TMPTEMPLATE}" "${TMPFILE}" -geometry "${text_pos}" -depth 4 -colors 16 -quality 9 -composite "${destdir}/${destfilename}"

optipng "${destdir}/${destfilename}" 

new_filemd5=$(md5sum "${destdir}/${destfilename}" | awk '{ print $1 }')

jq -n "{ templmd5: \"${new_templmd5}\", number: \"${number}\", title: \"${title}\", BACKCOLOR: \"${BACKCOLOR}\", FRONTCOLOR: \"${FRONTCOLOR}\", filemd5: \"${new_filemd5}\"}" > "${destlogname}"



