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
convert  "${TMPTEMPLATE}" ${TMPFILE} -geometry "${text_pos}" -depth 4 -colors 16 -quality 9 -composite "${destdir}/${destfilename}"

optipng "${destdir}/${destfilename}" &



