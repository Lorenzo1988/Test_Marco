contents = ["Nel mezzo del cammin di nostra vita"
    ,"Il mio nome è Ismaele"
    ,"In principio era il Verbo"
    ,"Le famiglie felici sono tutte uguali; ogni famiglia infelice è infelice a modo suo"]
filenames = ["Divina_Commedia.txt"
    ,"Moby_Dick.txt"
    ,"Bibbia.txt"
    ,"Anna_Karenina.txt"]


# usiamo la funzione zip che funziona in modo simile alla funzione contents
# solo che la funzione zip non ritorna indice e valore ma cicla sue due liste
path= "../files/incipit_libri"
for content,filename in zip(contents,filenames):
    file = open(f"{path}/Incipit_{filename}","w")
    file.write(content)
    file.close()
