user_prompt="Inserisci attività da fare: "

#while True

todos=[]

#nei cicli è meglio evitare la dichiarazione di variabili se non necessario

while True:
    todo = input(user_prompt)
    print(todo.title())
    todos.append(todo)
    print(todos)
    print("Next..")

#il comando dir(value) si usa per vedere tutti i metodi disponibili per quel type

#il comando help(value.method) si usa per avere i dettagli sul metodo

#BUILTINS per vedere tutte le funzioni disponibili

import builtins
dir(builtins)