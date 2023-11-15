
file_directory= "../files"
file_name="todos_bkp.txt"
todos=[]
i=0
# strip method serve per eliminare gli spazi alla fine
#cancello spazi bianchi e confronto solo la prima lettera con A/S/E
user_prompt="Type ADD - SHOW - EDIT - EXIT - COMPLETE: "
while True:
    richiesta = input(user_prompt)
    match richiesta.strip().upper()[0:2]:

        case 'AD'|"+":
            todo = input("Aggiungi attività: ") + "\n"
            file = open(file_directory+"/"+file_name, "r")
            todos = file.readlines()
            file.close()
            todos.append(todo)
            file=open(file_directory+"/"+file_name, "w")
            file.writelines(todos)
            file.close()

        case 'SH':
            file = open(file_directory+"/"+file_name, 'r')
            todos = file.readlines()
            file.close()
            print(todos)
#   opzione 1 per rimuovere le righe vuote: ciclo e elimino con strip \#n
#           new_todos = []
#           for item in todos:
#               new_item = item.strip('\n')
#               new_todos.append(new_item)

    #opzione 2 list comprehension: non devo dichiarare una lista vuota. il ciclo è implicito nelle parentesi quadre
            new_todos = [item.strip('\n') for item in todos]
#
            for index,item in enumerate(new_todos):
                row= f"{index+1}-{item.title()}"
                print(row)
            print("Il numero di attività è:",len(todos))




        case 'ED':
            file = open(file_directory+"/"+file_name, 'r')
            todos = file.readlines()
            file.close()
            number = int(input("seleziona item da modificare: "))
            number_1= number -1
            print(todos[number_1].title())
            new_todo = input("Inserisci il nuovo item {}: ".format(number))
            todos[number_1] = str(new_todo) + "\n"
            print(todos)
            file = open(file_directory+"/"+file_name, "w")
            file.writelines(todos)
            file.close()
        case 'EX':
            break
        case 'CO':
            number=int(input("Inserisci numero elenco da cancellare perchè completo: "))
#funzione pop --> cancella un elemento da una lista in base al numero dell'elemento nella lista
            todos.pop(number-1)
            file = open(file_directory + "/" + file_name, "w")
            file.writelines(todos)
            file.close()
# si usa case _ per dire: in tutti gli altri casi
        case _:
            print("Hai inserito una stringa non riconoscibile!")
print("ciao ciao!")
