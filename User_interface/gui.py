import PySimpleGUI as sg

label_instance = sg.Text("Metti qui i TO-DO")
input_box_instance = sg.InputText(tooltip="suggerimento: Inserisci il ToDo")
add_button_instance = sg.Button("ADD")
########
#WINDOW#

window_instance = sg.Window("Titolo App",layout=[[label_instance],[input_box_instance,add_button_instance]])
                                        #layout deve essere una list
                                        #le parentesi [] esterne indicano l'oggetto
                                        # le parentesi [] interne indicano le righe
                                        # se metto label e input_box in due []] interne diverse ottengo su due righe
window_instance.read()
#l'interprete si ferma alla fine del comando read() fino a che non si preme una qualche pulsante. Poi va avanti e close()
window_instance.close()