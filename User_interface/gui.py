import PySimpleGUI as sg
import modules.functions as functions
#WIDGET
label_instance = sg.Text("Metti qui i TO-DO")
input_box_instance = sg.InputText(tooltip="suggerimento: Inserisci il ToDo",key="todo",)
                                                            # key è la chiave del dizionario
add_button_instance = sg.Button("ADD")


########
#WINDOW#
window_instance = sg.Window("Titolo App"
                            ,layout=[[label_instance],[input_box_instance,add_button_instance]]
                            ,font=("Helvetica",20))

# Se togliamo le [] interne otteniamo errore
# #window_instance = sg.Window("Titolo App", layout=[label_instance, input_box_instance, add_button_instance])
# ogni riga deve essere un elenco a se stante

# gli elementi dentro sg.Window(layout= devono essere dei Widget)

#layout deve essere una list
                                        #le parentesi [] esterne indicano l'oggetto
                                        # le parentesi [] interne indicano le righe
                                        # se metto label e input_box in due []] interne diverse ottengo su due righe

#INIZIO ESECUZIONE
print("Fine esecuzione finestra")
while True:
    event,values=  window_instance.read()
    print(event)
    print(values)
    match event:
        case "ADD":
            todos= functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

#FINE ESECUZIONE
print("Fine esecuzione finestra")
window_instance.close()