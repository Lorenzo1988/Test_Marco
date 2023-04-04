# almeno 8 caratteri
# almeno 1 numero
# almeno una lettera maiuscola

# se tutte vere strong password
# se 2 vere medium password
# se 1 vera soft password
# se 0 vere PASSWORD NOT OK

#ok
while True:

    password_inserita = input("Inserisci una password: ")
# usiamo i dizionari
    result= {}

    leng=0
    if len(password_inserita) >7:
        result["condizione_lunghezza"]=1
    else:
        result["condizione_lunghezza"]=0

    for i in password_inserita:
        if i.isdigit():
            result["condizione_numero"] = 1
        if i.isupper():
            result["condizione_upper"] = 1

    print(result)

    j= sum(result.values())
    if j ==3:
        print("Password forte")
        break
    elif j==2:
        print("Password media")
    elif j==1:
        print("Password debole")
    else:
        print("Errore")