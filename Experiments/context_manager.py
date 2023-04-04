file_directory = "files/incipit_libri"
file_name = "Incipit_Bibbia.txt"
#creo un context manager
with open("../"+file_directory+"/"+file_name) as file:
    lettura_incipit = file.read()

# NB una variabile usata dentro il context manager può essere usata anche fuori
print(lettura_incipit)