import PySimpleGUI
import modules.functions as functions

#WIDGET
label_instance = PySimpleGUI.Text("Metti qui i TO-DO")
input_box_instance = PySimpleGUI.InputText(tooltip="suggerimento: Inserisci il ToDo",key="todo_key",do_not_clear=False)
                                                            # key è la chiave del dizionario
add_button_instance = PySimpleGUI.Button("Add")
list_box_instance = PySimpleGUI.Listbox(functions.get_todos(),key="list_todos_key",enable_events=True,size=[45,20])
edit_button_instance = PySimpleGUI.Button("Edit")

layout = [[label_instance]# riga1
          ,[input_box_instance,add_button_instance]   # riga2
          ,[list_box_instance,edit_button_instance]   # riga3
          ]
#esempio se voglio creare dei bottoni dinamicamente
#button_labels = ["Button_1","Button_2"]
#layout = []

#for bl in button_labels:
#    layout.append([PySimpleGUI.Button(bl)])



########
#WINDOW#
window_instance = PySimpleGUI.Window("Titolo App"
                            ,layout=layout

                            ,font=("Helvetica",20))

# Se togliamo le [] interne otteniamo errore
# #window_instance = sg.Window("Titolo App", layout=[label_instance, input_box_instance, add_button_instance])
# ogni riga deve essere un elenco a se stante

# gli elementi dentro sg.Window(layout= devono essere dei Widget)

#layout deve essere una list
                                        #le parentesi [] esterne indicano l'oggetto
                                        # le parentesi [] interne indicano le righe
                                        # se metto label e input_box in due []] interne diverse ottengo su due righe

#INIZIO ESECUZIONE FINESTRA
print("Inizio esecuzione finestra")
while True:
    event_button,event_tupla=  window_instance.read()
    print(f"event_button: {event_button}")
    print(f"event_tupla: {event_tupla}")
    match event_button:
        case "Add":
            todos= functions.get_todos()
            new_todo = event_tupla['todo_key'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window_instance["list_todos_key"].update(values=todos)
        case "Edit":
            todo_to_edit = event_tupla["list_todos_key"][0]
            new_todo = event_tupla["todo_key"]
            todos = functions.get_todos()
            index= todos.index(todo_to_edit)
            todos[index] = new_todo+"\n"
            functions.write_todos(todos)
            window_instance["list_todos_key"].update(values=todos)
        case "list_todos_key":
            window_instance["todo_key"].update(value=event_tupla["list_todos_key"][0])
        case PySimpleGUI.WIN_CLOSED:
            break

#FINE ESECUZIONE
print("Fine esecuzione finestra")
window_instance.close()