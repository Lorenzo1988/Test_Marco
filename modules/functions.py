# ordino le functions in questo file

# DEFINISCO DELLE VARIABILI USATE NELL FUNZIONI DI SOLITO IN MAIUSCOLO

FILEPATH= "../files/todos.txt"
#CUSTOM FUNCTION
#utilizzo parametro di default
def get_todos(filepath=FILEPATH):
    """
        Apro il file dentro <filepath>
        in modalità read e ritorno il contenuto
        del file
    """
    with (open(filepath, "r")) as file_local:
        print(f"Sto aprendo il file {filepath} in modalità lettura")
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
    print("Hello from functions solo da main")

print(f"Il __name__ è {__name__}")
print("Hello from functions anche da fuori il main")