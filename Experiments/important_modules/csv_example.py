import csv

 # IL MODULO csv SERVE PER LAVORARE CO I FILES .csv

with(open("files/Family.csv","r")) as file:
    data= list(csv.reader(file))

name = input("Inserisci un nome della famiglia: ").upper()

#inserisco l'iterazione da 1 e non da 0 perchè la prima riga è l'intestazione
for riga in data[1:]:
    if riga[0].upper() == name:
     print(riga)
