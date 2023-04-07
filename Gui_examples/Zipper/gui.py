import PySimpleGUI
import zip_creator

#WIDGET
label_selection_files = PySimpleGUI.Text("seleziona i files da comprimere".title())
label_selection_destination_folder = PySimpleGUI.Text("seleziona la folder di destinazione".title())
box_selection_files = PySimpleGUI.Input(tooltip="seleziona i files da comprimere",key="box_selection_files_key")
box_destination_folder = PySimpleGUI.Input(tooltip="seleziona i files da comprimere",key="box_destination_folder_key")
button_compress = PySimpleGUI.Button("Compress")
output_label = PySimpleGUI.Text(key="Output")

#PySimpleGUI.FileBrowse() è un bottone speciale già programmato per la selezione di files dal proprio filesystem
button_selection_file = PySimpleGUI.FilesBrowse("button_selection_files",key="button_selection_files_key")
#PySimpleGUI.FolderBrows() è un bottone speciale già programmato per la selezione di folders dal proprio filesystem
button_destination_folder = PySimpleGUI.FolderBrowse("button_destination_folder",key="button_destination_folder_key")


########
#WINDOW#
window_instance = PySimpleGUI.Window("File Compressor",
                            layout=[[label_selection_files,box_selection_files,button_selection_file],
                                     [label_selection_destination_folder,box_destination_folder,button_destination_folder],
                                     [button_compress,output_label]],
                            font=("Helvetica",20))

# Se togliamo le [] interne otteniamo errore
# #window_instance = sg.Window("Titolo App", layout=[label_instance, input_box_instance, add_button_instance])
# ogni riga deve essere un elenco a se stante

# gli elementi dentro sg.Window(layout= devono essere dei Widget)

#layout deve essere una list
                                        #le parentesi [] esterne indicano l'oggetto
                                        # le parentesi [] interne indicano le righe
                                        # se metto label e input_box in due []] interne diverse ottengo su due righe
while True:
    event_button, event_tupla = window_instance.read()
    filepaths = event_tupla["box_selection_files_key"].split(";")
    folder = event_tupla["button_destination_folder_key"]
    print(f"ciao: {filepaths}")
    print(f"ciaone: {event_tupla['button_selection_files_key']}")
    zip_creator.make_archive(filepaths,folder)
    window_instance["Output"].update(value= "Compressione completata!")
    break

window_instance.close()