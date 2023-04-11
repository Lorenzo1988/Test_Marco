#VARIABLES
file_directory= "../files"
file_name="todos_bkp.txt"
todos=[]
possible_actions=['ADD',"SHOW","EDIT","EXIT","COMPLETE"]

#CUSTOM FUNCTION
def get_todos():
    with (open(file_directory + "/" + file_name, "r")) as file_local:
        print(f"Sto aprendo il file {file_directory}/{file_name} in modalità lettura")
        todos_local = file_local.readlines()
    return todos_local

def write_todos():
    with open(file_directory + "/" + file_name, "w") as file_local:
        print(f"Sto aprendo il file {file_directory}/{file_name} in modalità scrittura")
        file_local.writelines(todos)
    return todos

user_prompt="Type ADD - SHOW - EDIT - EXIT - COMPLETE: "
while True:
    richiesta = input(user_prompt).strip()

    #CASO ADD
    if  richiesta.upper().startswith(str(possible_actions[0])):
        if len(richiesta) <4:
        #azione se len<4
            todo = input("Aggiungi attività: ") + "\n"
        else:
            todo = richiesta[4:] + "\n"

        todos = get_todos()
        todos.append(todo)
        write_todos()


    #CASO SHOW
    elif  richiesta.upper().startswith(str(possible_actions[1])):
        todos = get_todos()
        print(todos)
        new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(new_todos):
             item=item.strip('\n').title()
             row=f"{index+1}-{item}"
             print(row)
        print("\tIl numero di attività è:",len(todos))

    #CASO  EDIT
    elif  richiesta.upper().startswith(str(possible_actions[2])):

        #caso di inserimento solo di EDIT
        if len(richiesta.split(" ")) <2:
            number = input("seleziona item da modificare: ")
            number_1 = int(number) - 1
            new_todo = input("Inserisci il nuovo item {}: ".format(number))

        # caso di inserimento di edit e numero

        elif len(richiesta.split(" ")) == 2:
            try:
                number = int(richiesta.split(" ")[1])
                number_1 = int(number)
                new_todo = input("Inserisci il nuovo item {}: ".format(number))
            except ValueError:
                print("Errore Valorizzazione numero da modificare")

        # caso di inserimento di edit numero e valore
        else:
            # il comando try prepara all'excepet di gestione errore
            try:
                number_split= richiesta.split(" ")
                number_1 = int(number_split[1]) -1
                new_todo = ("".join(str(i) for i in number_split[2:]))
            except ValueError:
                print("Errore Valorizzazione numero da modificare")
                #il comando continue è l'opposto di break. Praticamente dice riparti
                continue

        todos = get_todos()
        todos[number_1] = str(new_todo) + "\n"
        write_todos()

    # CASO COMPLETE
    elif richiesta.upper().startswith(str(possible_actions[4])):
        if len(richiesta.split(" ")) <2:
            number=int(input("Inserisci numero elenco da cancellare perchè completo: "))
        else:
            number = int(richiesta.split(" ")[1])

        try:
            number_to_remove = number -1
            print(f"number_to_remove: {number_to_remove}")
            todo_to_remove = todos[number_to_remove].strip('\n')
            print(f"todo_to_remove: {number_to_remove}")
            todos.pop(number_to_remove)
            todos = write_todos()

            message = f"Rimosso l'item {todo_to_remove}"
            print(message)
        except IndexError:
            print("Numero di item non presente")
            continue
    elif richiesta.upper().startswith(str(possible_actions[3])):
        break

    else:
        print("Hai inserito una stringa non riconoscibile!")

print("ciao ciao!")
