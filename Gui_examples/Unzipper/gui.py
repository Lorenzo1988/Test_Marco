import PySimpleGUI as sg
from zip_extractor import extract_archive

# THEME
sg.theme("Black")
#DAAAAAAAAAAAAAAAAA QUI

#WIDGET

label_selection_files = sg.Text("seleziona l'archivio da decomprimere: ".title())
label_selection_destination_folder = sg.Text("seleziona la folder di destinazione: ".title())
box_selection_files = sg.Input(tooltip="seleziona i files da decomprimere",
                                        key="box_selection_files_key")

box_destination_folder = sg.Input(tooltip="seleziona la directory dove verranno deocompressi",
                                           key="box_destination_folder_key")

button_extract = sg.Button("Extract")
output_label = sg.Text(key="Output",text_color="green")

#PySimpleGUI.FileBrowse() è un bottone speciale già programmato per la selezione di files dal proprio filesystem
button_selection_file = sg.FilesBrowse("button_selection_files",key="button_selection_files_key")
#PySimpleGUI.FolderBrows() è un bottone speciale già programmato per la selezione di folders dal proprio filesystem
button_destination_folder = sg.FolderBrowse("button_destination_folder",key="button_destination_folder_key")
exit_button=sg.Button("Exit",key="Exit")


########
#WINDOW#
window_instance = sg.Window("Archive Extractor",
                                layout=[
                                        [label_selection_files, box_selection_files, button_selection_file],
                                        [label_selection_destination_folder, box_destination_folder, button_destination_folder],
                                        [button_extract,output_label],
                                        [exit_button]
                                        ],
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
    event_button,values_tupla= window_instance.read()
    if event_button =="Exit":
            break
    else:
        print(event_button,values_tupla)
        archivepath=values_tupla["box_selection_files_key"]
        directory_output = values_tupla["box_destination_folder_key"]
        extract_archive(archivepath=archivepath,directory_output=directory_output)
        window_instance["Output"].update(value="Estrazione Completata!")

window_instance.close()