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