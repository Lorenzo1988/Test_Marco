while True:
    try:
        lunghezza = float(input("Inserisci lunghezza:"))
        altezza = float(input("Inserisci altezza: "))
        if lunghezza == altezza:
        # uso la funzione exit che printa e restituisce l'eccezione
            exit("Non è un rettangolo ma un quadrato")
        area= lunghezza*altezza
        print(f"L'area del rettangolo è: {area}")
    except ValueError:
        print("valori inseriti non validi! Riprova")
        continue

