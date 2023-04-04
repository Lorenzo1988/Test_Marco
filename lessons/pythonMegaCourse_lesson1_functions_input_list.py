#funzione input

user_prompt="Inserisci attività da fare: "
todo1=input(user_prompt)
todo2=input(user_prompt)
todo3=input(user_prompt)

#liste
todos = [todo1,todo2,todo3]
print(todos)
print(type(todos))
pythonMegaCourse_lesson1_functions_input_list.py
#funzione len per lugnhezza
titolo=input("Enter a Title: ")
lunghezza= len(titolo)
print("La lunghezza del titolo è:",lunghezza)


#usa input per instanziare una variabile
nome=input("scrivi il tuo nome: ")
cognome= input("scrivi il cognome: ")
print("Il tuo identificativo è",nome,cognome)