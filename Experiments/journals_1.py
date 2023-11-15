import os.path

path = '../files/journals_1/'

data = input("Inserisci la data: ")

mood = input("assegna un voto alla giornata di oggi: ")

pensiero_del_giorno = input("metti un pensiero del giorno: ")

with open(f"{path}{data}.txt",mode="a+") as file:
    file.write(f"{mood}: ")
    file.write(pensiero_del_giorno + 2*"\n")
    print("Chase")
    linee = file.readlines()
    nuova_linea = [item.strip('\n') for item in linee]

    for index, item in enumerate(nuova_linea):
        item = item.strip('\n').title()
        row = f"{index + 1}-{item}"
        print(row)





