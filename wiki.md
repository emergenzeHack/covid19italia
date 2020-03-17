---
layout: page
title: Documentazione Tecnica
permalink: /wiki/
---

Benvenuto nel wiki di Covid19Italia, una community basata sui *social media*, nata per condividere informazioni utili e verificate sul corona virus in Italia.

Il progetto è completamente aperto e chiunque può dare il suo contributo seguendo queste linea guida.

## Il sito

Il nostro sito è creato con [Github](http://www.github.com).

## Diventa un contributore
Per essere aggiunto alla lista degli sviluppatori del repository apri un issue [qui](https://github.com/emergenzehack/covid19italia/issues/new?title=%5Brichiesta%20iscrizione%5D), richiedi l'accesso lasciando il tuo username [Telegram](https://web.telegram.org/).

##  Aiutaci a migliorare

*Covid19Italia è un progetto in divenire*, per suggerire miglioramenti apri un [issue qui](https://github.com/emergenzeHack/covid19italia/issues). Alla stessa pagina puoi vedere le segnalazioni aperte dagli altri utenti; da lì puoi vedere quello che c'è ancora da fare e da sistemare.

Grazie, aspettiamo il tuo aiuto!

## Riuso
Covid19Italia è un progetto opensource composto da varie applicazioni integrate. Questo WIKI consente di capire come è strutturato il progetto e come poterlo riusare. TerremotoCentroItalia è concesso con licenza Creative Commons Attribuzione 3.0 (CC BY) il cui testo è disponibile [a questo indirizzo](https://creativecommons.org/licenses/by/3.0/it/). Ove non diversamente specificato (ad esempio nei repository del codice sorgente) ti chiediamo se riusi parte del nostro progetto di rispettare i criteri di questa licenza.


### Indice dei contenuti

- Aprire una Issue
- Come si usa GitHub
- Lavorare sulle Segnalazioni
- Come funziona in breve il metodo TCI
- Convertire un documento Google Docs in Markdown
- Come si inserisce un elemento in Press
- Sviluppare in locale sul sito

---

# Aprire una Issue

Gli Issues possono essere usati per tenere traccia di bug, miglioramenti o altre richieste di progetto. 

Tutti gli utenti GitHub possono creare un issue per un progetto di tipo pubblico.

- Su Github naviga fino alla pagina principale del progetto.
- Sotto il nome del progetto fai click sul tab Issue del progetto.
- Fai click sul bottone verde "New Issue"

![](https://help.github.com/assets/images/help/issues/new_issues_button.png)

- Inserisci un titolo e una descrizione per il tuo issue.

Se sei un manutentore del progetto tu puoi assegnare l'issue a qualcuno, associarlo a delle milestone o aggiungere un'etichetta.

Puoi allegare un file trascinandolo nel campo descrizione.

Quando hai fatto fai click su "Submit new issue"

Note: i manutentori del progetto possono

- Creare un template per gli issue in un progetto. I template includono comandi che il manutentore del progetto sceglie di mostrare nella descrizione dell'issue.
- Disabilitare gli issue per un progetto.

# Come si usa GitHub?

Questa pagina è la traduzione di [questo semplice tutorial](https://guides.github.com/activities/hello-world/) in italiano e descrive i primi passi per iniziare ad usare Github come strumento di progettazione condivisa.

**Cosa è Github?**

Github è una piattaforma di archiviazione di codice per controllo versione e collaborazione. Ti permette di lavorare assieme agli altri su progetti ovunque.

Questo tutorial ti insegna le cose essenziali per usare Github, come i repository, i branch, i commit e le pull request. Sarai in grado di creare da solo un repository "Ciao Mondo!" ed imparare il flusso di gestione delle pull request, un modo molto popolare di creare e revisionare il codice.

Non è richiesto programmare.

Per completare questo tutorial, hai bisogno di un account Github e un accesso internet. Non hai bisogno di conoscere come programmare, usare la linea di comando o installare GIT (il software per controllare le versioni da riga di comando, integrato in Github).

Trucco: apri questa guida in una pagina del browser separata cosi tu puoi vederla mentre completi i passi del tutorial.

**1. Creare un repository**

Un repository di solito è usato per organizzare un progetto. I repository possono contenere cartelle e file, immagini, video, fogli di calcolo ed insiemi di dati - ogni cosa che sia necessaria per il tuo progetto. Raccomandiamo di includere sempre un README o un file con informazioni sul progetto. GIthub rende facile crearne uno al momento in cui crei i repository. Ti offre altre opzioni come ad esempio quella di inserire un file di licenza.

Il tuo repository ciao-mondo può essere un posto dove memorizzare idee, risorse o anche condividere e discutere cosa con altri.

Per creare un nuovo repository:

- In alto a destra, dopo aver fatto il login, fai click sul + e poi seleziona New Repository.
- Chiama il tuo repository ciao-mondo.
- Scrivi una breve descrizione.
- Seleziona "Initialize this repository with a README"

![](https://guides.github.com/activities/hello-world/create-new-repo.png)

- Fai click su "Create Repository"

**2. Creare un branch**

Fare un branch è un modo di lavorare su più versioni di un progetto alla volta.

Per default il tuo repository ha un branch chiamato master che è considerato essere il branch ultimo. Usiamo i branch per sperimentare e fare modifiche prima di inserirle nel branch master.

Quando fai un branch rispetto al master, stai copiando, o facendo una foto del master cosi come era in quel momento.
Se qualcun'altro fa una modifica al master mentre tu stai lavorando sul tuo branch, tu potresti prelevare i suoi aggiornamenti.

Questo diagramma mostra:
- Il branch master
- Un nuovo branch chiamato feature (perchè noi stiamo facendo "feature work" su questo branch)
- Il percorso che feature fa prima che sia fuso con master

![](https://guides.github.com/activities/hello-world/branching.png)

Hai mai salvato diverse versioni di un file? Qualcosa tipo:

storia.txt
storia-joe-modificata.txt
storia-joe-modificata-rivista.txt

I branch facilitano questa cosa nei repository di Github.

Qui, presso Github, i nostri sviluppatori, scrittori e designers usano i branch per tenere traccia delle correzioni dei bug e delle feature separate dal brach di produzione master. Quando una modifica è pronta, la fondono dal loro branch nel master.

Per creare un nuovo branch:

- Vai nel tuo nuovo repository ciao-mondo
- Fai click sul menu in altro sopra la lista dei file dove trovi la dicitura: master
- Scrivi un nome del branch, per esempio "readme-edits", nella casella di testo.
- Seleziona la box Create o premi Enter sulla tastiera

![](https://guides.github.com/activities/hello-world/readme-edits.gif)

Ora hai due branch. master e readme-edits. Essi sembrano proprio lo stesso ma non lo saranno per molto! Fra poco faremo delle modifiche al nuovo branch.

**3. Fai e committa modifiche**
Bravo! 
Adesso sei sulla vista del codice per il branch readme-edits, che è una copia del master. Facciamo delle modifiche.

Su Github, le modifiche salvate sono chiamate commit. Ogni commit ha un messaggio associato di commit, che è una descrizione che spiega perchè una particolare modifica è stata fatta. I messaggi di commit tengono traccia della storia delle modifiche, cosi gli altri contributori possono capire cosa hai fatto è perchè.

Fare e committare modifiche:

- Fai click sul file README.md.
- Fai click sull'icona della matita in alto a destra della vista dei file per fare una modifica.
- Nell'editor scrivo un po' di cose su di te. 
- Scrivi un messaggio di commit che descrive la tua modifica
- Fai click sul pulsante Commit changes

![](https://guides.github.com/activities/hello-world/commit.png)

Queste modifiche saranno fatte al README file solo nel tuo branch readme-edits, cosi che ora questo branch contiene contenuti diversi dal branch master.

**4. Aprire una Pull Request**

Ottime modifiche! 
Ora che hai modificato un file in un branch, potrai aprire una pull request.

Le pull request sono il cuore della collaborazione con Github. Quando apri una pull request, proponi le tue modifiche e richiedi che qualcuno le riveda e le "tiri" su e le fonda nel suo branch. Le pull requests mostrano le differenze dei contenuti di entrambi i branch. Le modifiche, aggiunte e le eliminazioni sono mostrate in verde e rosso.

Come fai una commit, puoi aprire una pull request e iniziare una discussione, prima che il codice sia finito.

Usando il sistema di "@" menzioni con Github nel tuo messaggio della pull request, puoi chiedere un feedback da una specifica persona o un team.

Puoi anche aprire pull request nel tuo repository e fonderle da solo. E' un buon modo di imparare il flusso di gestione prima di lavorare su progetti complessi.

Aprire una pull request per una modifica al file README

Fai Click sul tab Pull Request tab, quindi dalla pagina Pull Request, fai click sul bottone verde New pull request.	
![](https://guides.github.com/activities/hello-world/pr-tab.gif)

Seleziona il branch dove hai fatto le modifiche per compararlo con il master.
![](https://guides.github.com/activities/hello-world/pick-branch.png)

Guarda le tue modifiche nel diff sulla pagina di Compare, assicurati che sono cosa tu vuoi sottomettere.
![](https://guides.github.com/activities/hello-world/diff.png)

Quando tu sarai soddisfatto delle modifiche, fai click sul grande pulsante "Create Pull Request"
![](https://guides.github.com/activities/hello-world/create-pr.png)

Dai alla tua pull request un titolo e scrivi una breve descirzione delle tue modifiche.
![](https://guides.github.com/activities/hello-world/pr-form.png)

Quando hai scritto il tuo messaggio, fai click su Create pull request!

Suggerimento: puoi usare emoji e fare drag and drop di immagini e gif nei commenti.

**5. Fondere una Pull Request**

In questo step finale, è tempo di portare le tue modifiche fondendole dal tuo branch readme-edits nel branch di produzione master.

- Fai click sul pulsante verde Merge pull request per fondere le modifiche sul branch master
- Fai click su Confirm merge
- Procedi e cancella il branch, dato che le tue modifiche sono state incorporate, con il pulsante "Delete branch" in viola.
![](https://guides.github.com/activities/hello-world/merge-button.png)

![](https://guides.github.com/activities/hello-world/delete-button.png)


Evviva!

Completando questo tutorial, hai imparato a creare un progetto e fare una pull request su Github! 

Qui a cosa ti sarà utile questo tutorial:

- Creare un repository opensource
- Iniziare e gestire un nuovo branch
- Modificare un file e committare le modifiche su Github
- Aprire e Fondere una Pull Request

Dai un'occhiata al tuo profilo Github e vedrai un nuovo spazio di contributi!

Per molti altri tutorial su Github consulta [questa pagina](https://guides.github.com/).

# Lavorare sulle segnalazioni

Premessa:

> Questo documento è destinato al team che lavora sulle Segnalazioni. Gli altri utenti non hanno i permessi per effettuare le operazioni descritte qui, ma possono liberamente lasciare un commento su qualsiasi Issue contribuendo alla stessa. Ad esempio, a [questo link](https://github.com/emergenzeHack/covid19italia_segnalazioni/issues?q=is%3Aissue+is%3Aopen+label%3A%22Posizione+mancante%22) si possono vedere tutte le segnalazioni a cui ancora manca una posizione. Si possono suggerire in un commento le coordinate. Un moderatore la prenderà in carico e applicherà i vostri suggerimenti il prima possibile.
>
> Per entrare a far parte del team di Moderatori, assicurati di essere un membro attivo della community, di aver contribuito precedentemente ed entra nella chat di gruppo dei collaboratori.

# Meccanismo

Ogni compilazione di un modulo di Covid19Italia genera - dopo circa 30 secondi - una nuova Issue [qui](https://github.com/emergenzeHack/covid19italia_segnalazioni/issues). 

A queste Issue vengono applicate diverse etichette per descriverne la natura e lo stato di approvazione (che ne determina la pubblicazione finale sul sito, sui bollettini, su Twitter, sui canali e bot Telegram,..).

Questo permette a tutti di poter collaborare alla classificazione, moderazione e **verifica** comunitaria delle segnalazioni. È disponibile uno storico di tutte le modifiche, operazioni e moderazioni su ogni singola Issue.

Basta un account su GitHub e un browser web, nessuna conoscenza o strumento informatico è richiesto.

### Struttura

Le segnalazioni devono mantenere questa struttura:

```
<pre><yamldata>

Campo1: Valore del campo1
Campo2: Valore del campo2

</yamldata></pre>
```

Prestate attenzione alle seguenti convenzioni, quando modificate il contenuto di una Issue:

1. I campi che vanno su più righe vanno delimitati da un `'`. Esempio:

```
Descrizione: 'Il contenuto di questo campo
va su più
righe
'
Campo2: Questo campo invece è su una sola riga
```

Attenzione: Sui campi su più righe, `'` è usato per delimitare il contenuto di un campo quindi non può essere usato con la normale funzione di apostrofo all'interno. Per poter usare `'` letteralmente, e non come delimitatore, utilizzare `\'`

2. Il titolo dell'Issue diventa il titolo della segnalazione sul sito frontale.

3. Le modifiche (inclusa la pubblicazione/depubblicazione) appaiono sul sito finale dopo massimo 15 minuti. Usate <kbd>CTRL</kbd>+<kbd>F5</kbd> oppure la modalità navigazione in anonimo se non vedete cambiamenti. Se dopo queste operazioni ancora le cose non vi tornano procedente ad aprire Issue riportando il problema. Le Issue sui moduli (campi, struttura, dati mancanti) vanno aperte su [covid19italia_forms](https://github.com/emergenzeHack/covid19italia_form/issues).

4. Se avete bisogno di cambiare le Label che vengono preassegnate alle Issue (quelle che vedete già assegnate automaticamente) segnalatecelo [qui](https://github.com/emergenzeHack/covid19italia_form/issues/new)

5. Non rimuovete la Label "form", ci aiuta ad investigare l'origine delle segnalazioni.

# Geolocalizzazione

Ci sono alcune issue che hanno un campo "Posizione", come [questa](https://github.com/emergenzeHack/covid19italia_segnalazioni/issues/332)

E finiscono nella mappa che c'è [qui](https://www.covid19italia.help/issues/)

## Verificare geolocalizzazione

Se la segnalazione non ha una geolocalizzazione, lo script prova da solo a cercare nomi di comuni/città all'interno dei vari campi compilati. Se trova qualcosa, aggiunge *da solo* la posizione. Quando succede, viene applicata l'etichetta <kbd>Posizione da verificare</kbd> e il bot commenterà chiedendovi una conferma, dandovi anche un link a quelle coordinate per vedere subito se hanno senso o no.

Se anche dopo questo tentativo non si trova una posizione, viene applicata l'etichetta <kbd>Posizione mancante</kbd> così da poter filtrare tutte quelle che ne hanno ancora bisogno.


## Aggiungere geolocalizzazione

Quindi, le issue segnalate con la label <kbd>Posizione mancante</kbd> hanno bisogno di un intervento manuale che aggiunga la posizione.

### Come trovare le coordinate di un luogo?

Prendiamo ad esempio [questa](https://github.com/emergenzeHack/covid19italia_segnalazioni/issues/334) segnalazione su Milano) 

Si può usare questo sito: [Nominatim](https://nominatim.openstreetmap.org/).

In alto a destra c'è un tasto che si chiama "Show map bounds". Quando viene premuto, compare un rettangolo che contiene le coordinate. La riga più importante è "Last click".

Ci sono due numeri, separati da una virgola, sono latitudine e longitudine. Copiateveli.

### Aggiungere le coordinate alla segnalazione

Adessa, sulla Issue, va cliccato il tasto ... in alto a destra, quindi "edit".

Adesso aggiungete (o modificate) il campo 'Posizione', aggiungendo le coordinate ottenute poco fa:

```
...
Posizione: 43.768137 11.241812
```

Il primo valore è la Latitudine, il secondo la Longitudine (obbligatori). Il terzo e il quarto indicano Altitudine e Precisione (metri). Questi ultimi due sono facoltativi.


Esempio:

![GIF come georiferire issue](https://raw.githubusercontent.com/emergenzeHack/covid19italia/master/_doc/come_georiferire_issue.gif)


#### Esempio finale di segnalazione:

```
<pre><yamldata>
Da_chi_offerta: comitati di quartiere
Descrizione: 'Iniziativa di cittadini e cittadine, comitati ed associazioni del Quartiere
 (Centro storico) di Firenze: consegnano cibo e beni primari a chi ne fa richiesta.'
Destinatari: Consegna di cibo e generi di prima necessità
Link: https://google.it
Natura: solidale
Posizione: 43.768137 11.241812
Tipo_di_soggetto: privato
Titolo: Serve aiuto?
</yamldata></pre>
```


## Politiche

Queste sono alcune delle politiche, linee guida e regole su cui è stato deciso:

1. Non accettiamo segnalazioni riguardo ricerca scientifica (https://github.com/emergenzeHack/covid19italia_segnalazioni/issues/315#issuecomment-598456738)
2. Se alcuni campi sembrano invalidi, provare a correggerli o cercare maggiori informazioni su Google a partire dal titolo, NON chiudere immediatamente la Issue se non va il link o problemi analoghi.

Per discutere o fornire feedback, aprite un Issue



# Come funziona (in breve) il metodo TCI

!INCLUDE "covid19italia.wiki/Come-funziona-(in-breve)-il-"metodo-TCI".md"


# Convertire un documento Google Docs in Markdown

Sotto qualche semplice passaggio per convertire un documento fatto in Google Docs in un formato compatibile con questo WIKI o come post del blog di questo sito così da poter continuare ad usare Google Docs se lo si usa normalmente per scrivere e poi pubblicare contenuti su covid19italia.help

- Installare nei Componenti aggiuntivi il plugin "Docs to markdown" (dal menu Componenti Aggiuntivi -> Installa componenti aggiuntivi cercate "Docs to markdown". 
- una volta che il documento in Google Doc è pronto aprire il menu Componenti Aggiuntivi selezionate la voce "Docs to Markdown" e poi "Convert"
- Dal pannello a Sinistra premete sul pulsante Markdown. 

A questo punto selezionate tutto il testo che viene tradotto sotto...copiatelo con un normale "Copia" : questo è il vostro testo nel linguaggio compatibile con Github!

![](https://camo.githubusercontent.com/2f678a5b7b89a92fb486a04ec192c33bbf475890/68747470733a2f2f646f63732e676f6f676c652e636f6d2f64726177696e67732f642f3142304a35597752535a6c50556d7a712d3254582d6278573764756561304b6f33466e562d6c77744d65754d2f6578706f72742f706e67)

Andate ad esempio nella sezione WIKI, Create una nuova Pagina dandole un titolo ed incollate il testo. Alla fine salvate la pagina e la troverete pubblicata.

Nota: la guida di come si usa in dettaglio "Docs to markdown" si trova anche [qui](https://github.com/evbacher/gd2md-html/wiki#installing-docs-to-markdown)

Fatto!!
Facile no?

# Come si inserisce un elemento in Press

Per inserire un elemento nella tabella [PRESS](https://www.covid19italia.help/about/#press) procedere come segue:

* Andare su [questo file](https://github.com/emergenzeHack/covid19italia_data/blob/master/press.csv) dei PRESS
* Cliccare sull'icona matita per editare il file su Github
![cliccare l'icona per modificare il file PRESS](https://d186loudes4jlv.cloudfront.net/git/images/github_my_first_repo_readme.png)
* Aggiungere una riga al file ed inserire in sequenza data,fonte,titolo,link separati da virgola. Nota: non devono esserci virgole ulteriori eccetto quelle che separano i 4 campi.
* Cliccare sul pulsante "Commit changes" o "Propose changes" in basso
* Se viene proposto un pulsante verde "Create Pull Request" Premerlo ed attendere che li amministratori validino la modifica.

Fatto.

# Sviluppare in locale sul sito

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