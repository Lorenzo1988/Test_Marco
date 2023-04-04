
#while True

todos=[]

# strip method serve per eliminare gli spazi alla fine
#cancello spazi bianchi e confronto solo la prima lettera con A/S/E
user_prompt="Type ADD - SHOW - EXIT: : "
while True:
    richiesta = input(user_prompt)
    match richiesta.strip().upper()[0]:
#bitwise or operator
        case 'A'|"+":
            todo = input("Aggiungi attività: ")
            todos.append(todo)
        case 'S':
            for item in todos:
#voglio printare con la lettera maiuscola
                item=item.title()
                print(item)
        case 'E':
            break
# si usa case _ per dire: in tutti gli altri casi
        case _:
            print("Hai inserito una stringa non riconoscibile!")
print("ciao ciao!")
