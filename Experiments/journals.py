date= input("Inserisci la data di oggi: ")
mood = input("Come ti senti oggi da 1 a 10? ")
pensieri = input("Appunti del giorno: \n")

with open(f"../files/journals/{date}.txt","w") as file:
    file.write(date + "\n")
    file.write(mood + "\n")
    file.write(pensieri + "\n")
