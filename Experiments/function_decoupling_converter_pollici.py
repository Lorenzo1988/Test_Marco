feet_inches =input("Inserisci piedi e pollici:")

def feet_converter(feet_inches):
    parti=feet_inches.split(" ")
    feet=float(parti[0])
    inches=float(parti[1])
    meters = (feet * 0.3048) +( inches * 0.0254)
    return meters
    # per il concetto di disaccoppiamento il return deve essere il più atomico possibile
    # quindi no stringhe ma valore
        # NO: return f"{feet} feet e {inches} inches equivalgono a: {meters} meters"

print(feet_converter(feet_inches))

result = feet_converter(feet_inches)

# problema: se vogliamo stampare l'altezza in feet e inches non possiamo farlo perchè sono variabili dentro la funzione
if result < 1:
    print("Altezza troppo bassa per scivolo")
else:
    print ("Altezza ok per scivolo")

