import zipfile
import pathlib

#shutil STA PER SHELL UTILITIES
def make_archive(filepaths,directory_output):
    try:
        destination_path = pathlib.Path(directory_output,filepaths[0].rsplit("/",1)[1]+".zip")
        #destination_path = pathlib.Path(directory_output, "compresso.zip")
        # la funzione pathlib.Path() unisce directory_output + il nome del file selezionato come:
            # selezione della stringa dalla lista filepaths --> filepaths[0]
            # splitting usando "/"
            # selezione del primo elemento a partire da destra  --> rsplit("/",1)
            # questo divide in due blocci di cui il secondo [1] è il nome file
            # al nome file aggiungo ".zip"
        with zipfile.ZipFile(destination_path,'w') as archive:
            for filepath in filepaths:
                print(f"Pippo: {filepath}")
                filepath = pathlib.Path(filepath)
                archive.write(filepath,arcname=filepath.name)
    except IsADirectoryError:
        print(f"directory_output deve essere folder/<nome_file> non solo folder")

if __name__ == "__main__":
    make_archive(filepaths=["/home/lorenzo/pythonProjects/pythonMegaCourse_project1/Gui_examples/Zipper/directory_uncompressed/Divina_Commedia.txt,/home/lorenzo/pythonProjects/pythonMegaCourse_project1/Gui_examples/Zipper/directory_uncompressed/Divina_Commedia2.txt"]\
                 ,directory_output="directory_compressed")
