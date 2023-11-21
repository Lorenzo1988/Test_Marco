def calcola_area_quadrato(lato):
    area = lato*lato
    return area

lato = float(input("inserisci lato: "))
area = calcola_area_quadrato(lato)
print(f"area quadrato di lato {lato}: {area}")