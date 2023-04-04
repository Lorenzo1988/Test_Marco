lanci =  []
conteggio = 0
progressivo = 0
rapporto = 0
with open(f"../files/testa_croce/testa_croce.txt","w") as file:
    while True:
        risultato_lancio = input("Inserire se è apparsa Testa (T) o croce (C): ")
        match risultato_lancio:
            case "T":
                conteggio=int(conteggio)+1
                progressivo = int(progressivo) +1
                rapporto =f"{float(conteggio/progressivo)*100}%"
                lanci.append(risultato_lancio)
                file.write(risultato_lancio + "\n")
                print("lanci è: "+ str(lanci))
                print("Il conteggio è: " + str(conteggio))
                print("Il progressivo è: " + str(progressivo))
                print("Il rapporto è: " + str(rapporto))
            case "C":
                conteggio=conteggio
                progressivo = int(progressivo) +1
                rapporto =f"{float(conteggio/progressivo)*100}%"
                file.write(risultato_lancio + "\n")
                lanci.append(risultato_lancio)
                print("lanci è: "+ str(lanci))
                print("Il conteggio è: " + str(conteggio))
                print("Il progressivo è: " + str(progressivo))
                print("Il rapporto è: " + str(rapporto))
            case _:
                print("Errore inserimento! Esco")
                break

