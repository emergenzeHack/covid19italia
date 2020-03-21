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

Attenzione: I campi su più righe devono essere delimitati da `'` (uno all'inizio e uno alla fine del campo). `'` è usato per delimitare il contenuto di un campo quindi non può essere usato con la normale funzione di apostrofo all'interno. Per poter usare `'` letteralmente, e non come delimitatore, utilizzare `\'`

Ad esempio, se volessi scrivere `l'altro` una volta per riga, in un campo multi campo, dovrei fare così:

```
'
L\'altro
L\'altro
'
```

`'` viene utilizzato come delimitatore, mentre viene scritto `\` per usarlo letteralmente. Nella segnalazizone finale verrà poi mostrato semplicemente come `'`.

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

### Inserimento manuale di regione e/o provincia e/o comune

#### Come sapere quale regione/provincia/comune ha individuato il sistema?

Guardando sul sito nella pagina www.covid19italia.help/issues/<numero issue>
(ad esempio https://www.covid19italia.help/issues/748/) se la segnalazione ha una posizione già inserita, i valori Provincia e Regione sono quelli riconosciuti in base ai dati geografici. **In questo caso, se ci sono errori, sarebbe più utile sistemare la posizione**.

Ci possono essere delle segnalazioni che hanno una regione o provincia o un Comune di riferimento, ma per le quali non ha senso inserire una coppia di coordinate. Perché queste segnalazioni vengano comunque elencate nella pagina per regione o per provincia, si può inserire un campo nei dati del tipo

```
regione_manuale: Veneto
```

oppure

```
provincia_manuale: Bologna
```
oppure

```
comune_manuale: Cento
```

(Naturalmente non avendo una posizione la segnalazione non sarà visualizzata in mappa)

**NB Attenzione all'ortografia del nome: dev'essere esattamente quello che è utilizzato dalle altre segnalazioni.**

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

