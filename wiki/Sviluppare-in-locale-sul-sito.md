Questa breve guida ti spiegherà come creare sul tuo computer una copia del sito. In questo modo le modifiche al codice saranno immediatamente visibili nella tua copia locale, e potrai testare tutti i miglioramenti che stai progettando. Cominciamo!

## Prerequisiti

Dovrai installare sul tuo computer alcuni software per lo sviluppo. Nelle pagine linkate trovi tutte le istruzioni in dettaglio.

- Il linguaggio di programmazione [Ruby](https://www.ruby-lang.org/it/documentation/installation/)
- Il sistema di sviluppo distribuito [git](https://git-scm.com/downloads)

Per gli step successivi è richiesto un minimo di dimestichezza con il terminale a riga di comando. Niente di speciale, è uno strumento che ci consente di dare comandi al computer sotto forma di testo invece che cliccando con un mouse in una finestra. Gli utenti Mac e Linux dovrebbero avere già l'applicazione *Terminale* installata; per gli utenti Windows l'installazione di git include già un terminale simile a quello di Linux.

Glisseremo anche su molti dettagli di git e Github, rimandandovi all'altra guida presente nella nostra wiki.

I comandi da inserire nel terminale (anche copia-incollando) saranno indicati in questo modo: `comando di esempio`

## Predisposizione dell'ambiente

Per prima cosa verifichiamo di avere installato Ruby e bundler, che a sua volta ci aiuterà a installare tutte le dipendenze che ci servono.

Su Mac con Homebrew:

```
brew install ruby
```

installa la gem bundle
```
sudo gem install bundler:1.17.3
```

installa _command line developer tools_
```
xcode-select --install
```


Su Ubuntu:

```
sudo apt install build-essential git ruby-full ruby-bundler zlib1g-dev
```

Facciamo su github il *fork* del repository, poi cloniamo il nostro fork in locale: `git clone https://github.com/nomeutente/covid19italia.git` (ricordati di sostituire il tuo vero nome utente)

Se si lavora sui dati (_data/) bisognerà forkare e lavorare su covid19italia_data invece che su covid19italia.

Portiamoci all'interno della nuova cartella: `cd covid19italia`

Installiamo tutte le dipendenze del progetto: `bundle install --path vendor/bundle`

## Facciamo partire il sito!
Eseguiamo, sempre nella cartella covid19italia, `bundle exec jekyll serve`

Il programma stamperà a video l'indirizzo da aprire nel browser, che sarà del tipo http://127.0.0.1:4000/.

Ecco fatto, tutto qui! Buon lavoro :muscle: 

## Ottenere una "build"

Per ottenere una versione _statica_ del sito bisogna eseguire il processo di _build_.

È lo stesso processo che viene eseguito quando viene rilasciato l'aggiornamento sulla versione pubblica del sito.

Per eseguire la _build_ in locale bisogna eseguire questo comando:

```shell
bundle exec jekyll build
```

## Risoluzione di eventuali errori

#### Per aprire il sito da un altro computer della rete
Se fate girare il sito su una macchina con Linux e sviluppate sotto Windows dovrete aggiungere -H 0.0.0.0 al comando serve, tipo:

`bundle exec jekyll serve -H 0.0.0.0`
 
In questo modo potrete aprire il sito da qualsiasi postazione connessa alla vostra rete e non solo dal localhost. Utile per testare le modifiche con cellulari, tablet o altri browser.