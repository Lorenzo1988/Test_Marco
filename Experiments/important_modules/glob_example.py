import glob

# LA FUNZIONE glob() RESTITUISCE UNA LIST CON TUTTI I FILES CHE RISPECCHIANO UN FILTRO
myfiles = glob.glob("files/*.txt")

print(myfiles)


for filepath in myfiles:
    with open(filepath, "r") as file:
        print(f"\nSto aprendo il file {filepath} in modalità scrittura")
        print(file.read())
