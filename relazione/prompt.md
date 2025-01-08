# Prompts di valutazione modelli
Per ogni modello andremo a valutare il voto medio dato a 3 differenti risposte per prompt. Voti vanno da 1 a 5 per ogni campo.
Il metro di valutazione consiste nella correttezza teorica per le domande di teoria, senso logico per la domanda teorico pratica e correttezza della risposta e del codice per le domande di codice. Il voto massimo per le domande di codice viene raggiunto solo in caso di script funzionante al 100%.

## Prompt 1 (domanda più generica che potrebbe avere risposte già nel modello base, che con un pò di training vediamo se cambia)
How does Jolie handle REST API's? Can you explain how does the language work when implementing them?

## Prompt 2 (domanda teorica inerente a Jolie, più nello specifico)
What's the difference between processes and sessions in Jolie? Can you expand a bit more on the sessions?

## Prompt 3 (domanda ibrida tra teoria e pratica, con esempio di codice per collegamento database)
How does Jolie handle database connections? Can you explain to me how that works and give me some practical examples on how to use them?

## Prompt 4 (domanda di codice iper generica, dove possiamo osservare correttezza di sintassi)
Can you give me the code for two Jolie programs that communicate with eachother. I want to send an "Hello World" message from one to the other.

## Prompt 5 (domanda di codice leggermente più complessa)
Help me write the code for a calculator in Jolie. I want my calculator to be able to do basic functions, like sum, subtraction, divide, multiply. Give me the code for the Calculator and the code to try and communicate with it.