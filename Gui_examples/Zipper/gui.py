import PySimpleGUI
import PySimpleGUI as sg

#WIDGET
label_selection_files = sg.Text("seleziona i files da comprimere".title())
label_selection_destination_folder = sg.Text("seleziona la folder di destinazione".title())
box_selection_files = sg.Input(tooltip="seleziona i files da comprimere")
box_destination_folder = sg.Input(tooltip="seleziona i files da comprimere")
button_compress = sg.Button("COMPRESS")

#PySimpleGUI.FileBrowse() è un bottone speciale già programmato per la selezione di files dal proprio filesystem
button_selection_file = sg.FileBrowse("Scegli")
#PySimpleGUI.FolderBrows() è un bottone speciale già programmato per la selezione di folders dal proprio filesystem
button_destination_folder = sg.FolderBrowse("Scegli")


########
#WINDOW#
window_instance = sg.Window("File Compressor",layout=[[label_selection_files,box_selection_files,button_selection_file],
                                                  [label_selection_destination_folder,box_destination_folder,button_destination_folder],
                                                  [button_compress]])

# Se togliamo le [] interne otteniamo errore
# #window_instance = sg.Window("Titolo App", layout=[label_instance, input_box_instance, add_button_instance])
# ogni riga deve essere un elenco a se stante

# gli elementi dentro sg.Window(layout= devono essere dei Widget)

#layout deve essere una list
                                        #le parentesi [] esterne indicano l'oggetto
                                        # le parentesi [] interne indicano le righe
                                        # se metto label e input_box in due []] interne diverse ottengo su due righe
window_instance.read()

#l'interprete si ferma alla fine del comando read() fino a che non si preme una qualche pulsante. Poi va avanti e close()
window_instance.close()