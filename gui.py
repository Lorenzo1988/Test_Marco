import PySimpleGUI as sg
import modules.functions as functions
import time
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

if __name__ == "__main__":
    now = time.strftime("%d-%b-%Y %H:%M:%S")
    print(f"{now}: Il file __main__ del run è -->  {__file__}")
    print(f"{now}: Il __name__ è {__name__}")

# VERIFICA SE ESISTE IL FILE todos_bkp.txt altrimenti lo crea
verifica_todo= functions.verify_if_exist_file()
print(verifica_todo)
#WIDGET

#TESTO_BOTTONI


#RIGA 0
label_clock = sg.Text("",key="clock_key")

#RIGA 1
label_instance = sg.Text("Metti qui i TO-DO")

#RIGA 2
input_box_instance = sg.InputText(tooltip="suggerimento: Inserisci il ToDo",key="box_inserisci_attivita",do_not_clear=False)
add_button_instance = sg.Button("Add")

#RIGA 3
list_box_instance = sg.Listbox(functions.get_todos(),key="box_elenco_attivita",enable_events=True,size=[45,20])
edit_button_instance = sg.Button("Edit")
complete_button= sg.Button("Complete")

#RIGA 4
exit_button=sg.Button("Exit",)

#LAYOUT
layout = [[label_clock]                                                 # riga0 clock
          ,[label_instance]                                             # riga1
          ,[input_box_instance,add_button_instance]                     # riga2
          ,[list_box_instance,edit_button_instance,complete_button]     # riga3
          ,[exit_button]                                                # riga4
          ]

#esempio se voglio creare dei bottoni dinamicamente
#button_labels = ["Button_1","Button_2"]
#layout = []

#for bl in button_labels:
#    layout.append([PySimpleGUI.Button(bl)])



########
#WINDOW#
window_instance = sg.Window("Titolo App"
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
print("-------\nInizio esecuzione finestra\n-------")
azione = 0
while True:
    azione += 1
    now = time.strftime("%d-%b-%Y %H:%M:%S")
    azione_eseguita,risultati_azione=  window_instance.read(timeout_key=1)
    window_instance["clock_key"].update(value=now)
    match azione_eseguita:
        case "Add":
            print(f"\n{now}: AZIONE {azione}. ADD. Azione_eseguita: {azione_eseguita}")
            print(f"{now}: AZIONE {azione}.ADD. Risultati_azione: {risultati_azione}")

            todos= functions.get_todos()
            new_todo = risultati_azione['box_inserisci_attivita'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window_instance["box_elenco_attivita"].update(values=todos)
        case "Edit":
            print(f"\n{now}: AZIONEp {azione}. EDIT. Azione_eseguita: {azione_eseguita}")
            print(f"{now}: AZIONEq {azione}. EDIT. Risultati_azione: {risultati_azione}")

            try:
                todo_to_edit = risultati_azione["box_elenco_attivita"][0]
                new_todo = risultati_azione["box_inserisci_attivita"]
                todos = functions.get_todos()
                index= todos.index(todo_to_edit)
                todos[index] = new_todo+"\n"
                functions.write_todos(todos)
                window_instance["box_elenco_attivita"].update(values=todos)
            except IndexError:
                sg.popup("Non hai selezionato l'elemento da editare",font=("Helevetica",20))
        case "Complete":
            print(f"\n{now}: AZIONE {azione}. COMPLETE. Azione_eseguita: {azione_eseguita}")
            print(f"{now}: AZIONE {azione}.COMPLETE. Risultati_azione: {risultati_azione}")

            todo_to_complete = risultati_azione["box_elenco_attivita"][0]
            todos=functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window_instance["box_elenco_attivita"].update(values=todos)
            #window_instance["todo_key"].update(values="")
        case "Exit":
            break


        case "box_elenco_attivita":
            print(f"\n{now}: AZIONE {azione}. SELEZIONA DA ELENCO. Azione_eseguita: {azione_eseguita}")
            print(f"{now}: AZIONE {azione}. SELEZIONA DA ELENCO. Risultati_azione: {risultati_azione}")

            window_instance["box_inserisci_attivita"].update(value=risultati_azione["box_elenco_attivita"][0])

        case sg.WIN_CLOSED:
            break

#FINE ESECUZIONE
print(f"-------\n{now}: Fine esecuzione finestra\n-------")
window_instance.close()