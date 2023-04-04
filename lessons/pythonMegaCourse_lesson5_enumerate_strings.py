
#while True

todos=[]
i=0
# strip method serve per eliminare gli spazi alla fine
#cancello spazi bianchi e confronto solo la prima lettera con A/S/E
user_prompt="Type ADD - SHOW - EDIT - EXIT - COMPLETE: "
while True:
    richiesta = input(user_prompt)
    match richiesta.strip().upper()[0:2]:
#bitwise or operator
        case 'AD'|"+":
            i=i+1
            todo = input("Aggiungi attività: ")
            todos.append(todo)
        case 'SH':
#usiamo la funzione enumerate
#la funzione enumerate restituisce un oggetto enumerate che associa id-valore
#Esempio enumerate(["a","b","c"]) == [(0,"a"),(1,"b"),(2,"c")]
            for index, item in enumerate(todos):
                righetta= f"{index+1}-{item}"
#voglio printare con la lettera maiuscola
                item=item.title()
#uso la f-string --> permette di inserire, dentro una stringa, delle valorizzazioni di variabili
                print(righetta)
# faccio un print fuori dal ciclo loop per usare l'ultima valorizzazione di index e vedere il numero di elementi
#            print(f"Il numero di attività è {index+1}")
# E' più opportuno usare la funzione len
            print("Il numero di attività è:",len(todos))
        case 'ED':
#uso la funzione int per convertire una stringa in numero
            number = int(input("seleziona item da modificare: "))
            number_1= number -1
            print(todos[number_1].title())
            new_todo = input("Inserisci il nuovo item {}: ".format(number))
            todos[number_1] = str(i) + ". " + str(new_todo)
        case 'EX':
            break
        case 'CO':
            number=int(input("Inserisci numero elenco da cancellare perchè completo: "))
#funzione pop --> cancella un elemento da una lista in base al numero dell'elemento nella lista
            todos.pop(number-1)
# si usa case _ per dire: in tutti gli altri casi
        case _:
            print("Hai inserito una stringa non riconoscibile!")
print("ciao ciao!")
