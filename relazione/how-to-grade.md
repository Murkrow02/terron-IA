## REGOLE
Regole generali per valutare al meglio i prompt. Vengono date delle scalette di riferimento per ogni voto di ogni prompt.


## Prompt 1 (domanda più generica che potrebbe avere risposte già nel modello base, che con un pò di training vediamo se cambia)
> **Prompt**: How does Jolie handle REST API's? Can you explain how does the language work when implementing them?


0. non capisce nemmeno il contesto
1. ha capito il contesto ma allucina completamente la risposta
2. ha capito il contesto, qualcosa risulta sensata ma continua ad allucinare
3. comincia a capire il contesto di jolie ma sbaglia gli esempi
4. comincia a capire il contesto di jolie e a fare esempi sensati o semi sensati su Jolie
5. comprende il contesto di Jolie e risponde in maniera corretta


## Prompt 2 (domanda teorica inerente a Jolie, più nello specifico)
> **Prompt**: What's the difference between processes and sessions in Jolie? Can you expand a bit more on the sessions?


0. non capisce nemmeno il contesto
1. ha capito il contesto ma allucina completamente la risposta
2. ha capito il contesto, qualcosa risulta sensata ma continua ad allucinare
3. comincia a capire il contesto di jolie ma sbaglia a capire la differenza tra i due concetti
4. comincia a capire il contesto di jolie e capisce la differenza tra i due concetti
5. comprende il contesto di Jolie e risponde in maniera corretta


## Prompt 3 (domanda ibrida tra teoria e pratica, con esempio di codice per collegamento database)
> **Prompt**: How does Jolie handle database connections? Can you explain to me how that works and give me some practical examples on how to use them?


0. non capisce nemmeno il contesto
1. ha capito il contesto ma allucina completamente la risposta
2. ha capito il contesto, qualcosa risulta sensata ma continua ad allucinare
3. comincia a capire il contesto di jolie ma il codice è completamente sbagliato
4. comincia a capire il contesto di jolie ed il codice comincia ad avere qualche somiglianza a Jolie
5. comprende il contesto di Jolie e risponde in maniera corretta


## Prompt 4 (domanda di codice iper generica, dove possiamo osservare correttezza di sintassi)
> **Prompt**: Can you give me the code for two Jolie programs that communicate with eachother. I want to send an "Hello World" message from one to the other.


0. non capisce nemmeno il contesto
1. ha capito il contesto ma allucina completamente la risposta
2. ha capito il contesto, qualcosa risulta sensata ma continua ad allucinare
3. comincia a capire il contesto di jolie ma il codice è completamente sbagliato
4. comincia a capire il contesto di jolie ed il codice comincia ad avere qualche somiglianza a Jolie
5. comprende il contesto di Jolie e risponde in maniera corretta


## Prompt 5 (domanda di codice leggermente più complessa)
> **Prompt**: Help me write the code for a calculator in Jolie. I want my calculator to be able to do basic functions, like sum, subtraction, divide, multiply. Give me the code for the Calculator and the code to try and communicate with it.


0. non capisce nemmeno il contesto
1. ha capito il contesto, qualcosa risulta sensata ma continua ad allucinare
2. comincia a capire il contesto di jolie ma il codice è completamente sbagliato
3. comincia a capire il contesto di jolie ed il codice comincia ad avere qualche somiglianza a Jolie
4. comprende il contesto di Jolie e risponde in maniera corretta, con codice funzionante almeno all'70%
5. comprende il contesto di Jolie e risponde in maniera corretta, con codice funzionante almeno all'90%