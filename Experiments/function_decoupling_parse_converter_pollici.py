feet_inches =input("Inserisci piedi e pollici:")

def feet_parse(feet_inches):
    parti = feet_inches.split(" ")
    feet = float(parti[0])
    inches = float(parti[1])
    return {"feet": feet, "inches":inches}

def feet_convert(feet,inches):
    meters = (feet * 0.3048) +( inches * 0.0254)
    return meters

#Parso il valore passato
parsed = feet_parse(feet_inches)

#Converto le due parti del valore parsato

result = feet_convert(parsed['feet'],parsed['inches'])

#printo il risultato
print(f"{parsed['feet']} feet and {parsed['inches']} inches --> equals {result} meters")


#Verifico l'altezza
# problema: se vogliamo stampare l'altezza in feet e inches non possiamo farlo perchè sono variabili dentro la funzione
if result < 1:
    print("Altezza troppo bassa per scivolo")
else:
    print ("Altezza ok per scivolo")

