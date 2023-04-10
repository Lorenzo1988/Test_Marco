import zipfile
import pathlib

#shutil STA PER SHELL UTILITIES
def extract_archive(archivepath,directory_output):
    with zipfile.ZipFile(archivepath,'r') as archive:
            archive.extractall(directory_output)

if __name__ == "__main__":
    extract_archive(archivepath="/home/lorenzo/pythonProjects/pythonMegaCourse_project1/Gui_examples/Unzipper/directory_compressed/Divina_Commedia.txt.zip"
                    , directory_output="/home/lorenzo/pythonProjects/pythonMegaCourse_project1/Gui_examples/Unzipper/directory_uncompressed")
