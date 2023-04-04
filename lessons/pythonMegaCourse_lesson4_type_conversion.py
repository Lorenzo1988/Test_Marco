
#while True

todos=[]
i=0
# strip method serve per eliminare gli spazi alla fine
#cancello spazi bianchi e confronto solo la prima lettera con A/S/E
user_prompt="Type ADD - SHOW - EDIT - EXIT: : "
while True:
    richiesta = input(user_prompt)
    match richiesta.strip().upper()[0:2]:
#bitwise or operator
        case 'AD'|"+":
            i=i+1
            todo = input("Aggiungi attività: ")
            todoi = str(i) + ". " + str(todo)
            todos.append(todoi)
        case 'SH':
            for item in todos:
#voglio printare con la lettera maiuscola
                item=item.title()
                print(item)
        case 'ED':
#uso la funzione int per convertire una stringa in unmero
            number = int(input("seleziona item da modificare: "))
            number_1= number -1
            print(todos[number_1].title())
            new_todo = input("Inserisci il nuovo item {}: ".format(number))
            todos[number_1] = str(i) + ". " + str(new_todo)
        case 'EX':
            break
# si usa case _ per dire: in tutti gli altri casi
        case _:
            print("Hai inserito una stringa non riconoscibile!")
print("ciao ciao!")
