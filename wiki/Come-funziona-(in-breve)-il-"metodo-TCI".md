Questo progetto è "clonato" da un precedente usato per il terremoto del centro italia del 2016 chiamato TCI.

TCI (terremotocentroitalia.info) è un sito "dinamico" basato su:
* una gestione di segnalazioni tramite issue github e da alcuni script (d'ora in poi "backend")
* una catalogazione e impaginazione delle segnalazioni tramite jekyll (d'ora in poi "frontend")

## Backend

Il backend è direttamente rappresentato da un repo github del quale viene utilizzata solo la parte di segnalazioni (lo potete vedere qui https://github.com/emergenzeHack/terremotocentro_segnalazioni/issues).

Pro:
* il sistema è robusto, funzionale, gestito da altri
* molto facile da usare, ci sono varie persone che hanno già esperienza
* possibilità di aggiungere tag alle segnalazioni per la catalogazione
* API per scaricare

Contro:
* per inserire info "machine readable" nelle segnalazioni usiamo YAML, che dev'essere gestito da un editor esterno
* se lo YAML si rompe, bisogna intervenire "a mano"

### Script di conversione

Ogni 5 minuti, uno script (https://github.com/emergenzeHack/covid19italia/blob/master/scripts/csvupdate.sh):
* scarica tutte le segnalazioni da github
* decodifica lo YAML
* crea un array JSON che contiene le segnalazioni e lo YAML convertito in JSON
* committa eventuali differenze sul repo GIT, scatenando webhook e nuova build

## Frontend

Siccome Jekyll interpreta direttamente JSON, ci sono varie pagine che filtrano il JSON e creano HTML con liste, mappe, etc

I framework utilizzati sono:

* bootstrap per il layout
* openlayers/leaflet per le mappe

Pro:

* molto veloce da servire
* si può appoggiare su siti esterni come netlify
* praticamente inattaccabile

Contro:

* nei momenti di massimo movimento, l'aggiornamento è ogni 5 minuti

# Cose che si potrebbero migliorare

* La trasformazione delle issue nel sito potrebbe essere fatta in modo più efficiente usando gli hook di github e un DB qualsiasi per memorizzare i dati, in modo da poter avere aggiornamenti più rapidi. Resta il fatto che quando il sito è "fermo", non ha senso avere un DB da interrogare ogni momento
