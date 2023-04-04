from modules.functions.feet_parse import feet_parse
from modules.functions.feet_converter import feet_converter
from modules.functions.check_high import check_high

feet_inches =input("Inserisci piedi e pollici:")

from modules import functions
#Parso il valore passato
parsed = feet_parse(feet_inches)

#Converto le due parti del valore parsato

result = feet_converter(parsed['feet'],parsed['inches'])

#printo il risultato
print(f"{parsed['feet']} feet and {parsed['inches']} inches --> equals {result} meters")


#Verifico l'altezza
# problema: se vogliamo stampare l'altezza in feet e inches non possiamo farlo perchè sono variabili dentro la funzione

print(f"result: {result}")
print(f"type(result): {type(result)}")


check_high(result)