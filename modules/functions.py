FILEPATH= "files/todos.txt"
#FILEPATH="/home/lorenzo/pythonProjects/pythonMegaCourse_project1/todos.txt"

import os
import time


def verify_if_exist_file(filepath=FILEPATH):
    """
    verifica se esiste il file <filepath>
    se esiste lo apre, se non esiste lo crea
    :param filepath:
    :return:  restituisce una stringa
    """
    if not os.path.exists(filepath):
        with open(filepath, "w") as file:
            now = time.strftime("%d-%b-%Y %H:%M:%S")
            return (f"{now}: Il file {filepath} non esiste. Lo creo")

    else:
        now = time.strftime("%d-%b-%Y %H:%M:%S")
        return(f"{now}: Il file {filepath} esiste già. NON lo creo")

        pass
def funzione_solo_doc():
    """
    questa funzione contiene solo doc-string
    :return: return stringa "documentazione mostrata!"
    """
    return "documentazione mostrata"
#CUSTOM FUNCTION
#utilizzo parametro di default
def get_todos(filepath=FILEPATH):
    """
        Apro il file dentro <filepath>
        in modalità read e ritorno il contenuto
        del file
    """
    with (open(filepath, "r")) as file_local:
        now = time.strftime("%d-%b-%Y %H:%M:%S")
        print(f"{now}: Sto aprendo il file {filepath} in modalità lettura")
        todos_local = file_local.readlines()
    return todos_local

#N.B. se ci sono dei parametri senza default definito vanno messi all'inizio
def write_todos(todos_arg,filepath=FILEPATH):
    """
        Apro il file dentro <filepath>
        in modalità write e ci scrivo dentro
        il contenuto di <todos_arg>
        """
    with open(filepath, "w") as file_local:
        #print(f"Sto aprendo il file {filepath} in modalità scrittura")
        file_local.writelines(todos_arg)

# se uso la condizione if __name__ == "__main__"
# eseguo il contenuto dell'if SOLO SE sto lanciando
# esplicitamente il file dove è espressa la funzione
# e NON TRAMITE import

if __name__ == "__main__":
    now = time.strftime("%d-%b-%Y %H:%M:%S")
    print(f"{now}: Il file __main__ del run è {__file__}")
    print(f"{now}: Il __name__ è {__name__}")
else:
    now = time.strftime("%d-%b-%Y %H:%M:%S")
    print(f"{now}: Importato file: {__name__}")