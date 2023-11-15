
file_directory= "../files"
file_name="todos_bkp.txt"
todos=[]
possible_actions=['ADD',"SHOW","EDIT","EXIT","COMPLETE"]
azioni = ' - '.join(possible_actions)
user_prompt=f"Type {azioni}: "

while True:
    richiesta = input(user_prompt)

    #CASO ADD
    if  richiesta.upper().startswith(str(possible_actions[0])):
        if len(richiesta) <4:
        #azione se len<4
            todo = input("Aggiungi attività: ") + "\n"
        else:
            todo = richiesta[4:] + "\n"

# creo il context manager
        with (open(file_directory+"/"+file_name, "r")) as file:
            todos = file.readlines()

        todos.append(todo)
#  creo il context manager
        with open(file_directory+"/"+file_name, "w") as file:
           file.writelines(todos)

    #CASO SHOW
    elif  richiesta.upper().startswith(str(possible_actions[1])):
#  creo il context manager
        with (open(file_directory+"/"+file_name, "r")) as file:
            todos = file.readlines()
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


        # caso di inserimento di edit numero e valore
        else:
            number_split= richiesta.split(" ")
            number_1 = int(number_split[1]) -1
            new_todo = ("".join(str(i) for i in number_split[2:]))

        with open(file_directory + "/" + file_name, 'r') as file:
            todos = file.readlines()
            todos[number_1] = str(new_todo) + "\n"
        with open(file_directory + "/" + file_name, "w") as file:
            file.writelines(todos)


        # creo il context manager per leggere il file

    #CASO  COMPLETE
    elif richiesta.upper().startswith(str(possible_actions[4])):
        number=int(input("Inserisci numero elenco da cancellare perchè completo: "))

        number_to_remove = number -1
        todo_to_remove = todos[number_to_remove].strip('\n')
        todos.pop(number_to_remove)

        with open(file_directory+"/"+file_name,"w") as file:
            file.writelines(todos)

        message = f"Rimosso l'item {todo_to_remove}"
        print(message)
# si usa case _ per dire: in tutti gli altri casi
    elif richiesta.upper().startswith(str(possible_actions[3])):
        break

    else:
        print("Hai inserito una stringa non riconoscibile!")

print("ciao ciao!")
