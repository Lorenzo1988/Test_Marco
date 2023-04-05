
file_directory= "../files"
file_name="todos.txt"
todos=[]

user_prompt="Type ADD - SHOW - EDIT - EXIT - COMPLETE: "
while True:
    richiesta = input(user_prompt)
    match richiesta.strip().upper()[0:2]:

        case 'AD'|"+":
            todo = input("Aggiungi attività: ") + "\n"

# creo il context manager
            with (open(file_directory+"/"+file_name, "r")) as file:
                todos = file.readlines()


            todos.append(todo)
#  creo il context manager
            with open(file_directory+"/"+file_name, "w") as file:
               file.writelines(todos)

        case 'SH':
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

        case 'ED':
            number = int(input("seleziona item da modificare: "))
            number_1= number -1

            # creo il context manager per leggere il file
            with open(file_directory + "/" + file_name, 'r') as file:
                todos = file.readlines()
            new_todo = input("Inserisci il nuovo item {}: ".format(number))
            todos[number_1] = str(new_todo) + "\n"

#creo il context manager per scrivere nel file
            with open(file_directory+"/"+file_name, "w") as file:
                file.writelines(todos)

        case 'CO':
            number=int(input("Inserisci numero elenco da cancellare perchè completo: "))

            number_to_remove = number -1
            todo_to_remove = todos[number_to_remove].strip('\n')
            todos.pop(number_to_remove)

            with open(file_directory+"/"+file_name,"w") as file:
                file.writelines(todos)

            message = f"Rimosso l'item {todo_to_remove}"
            print(message)
# si usa case _ per dire: in tutti gli altri casi
        case 'EX':
            break

        case _:
            print("Hai inserito una stringa non riconoscibile!")
print("ciao ciao!")
