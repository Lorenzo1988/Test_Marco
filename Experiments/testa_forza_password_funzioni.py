def controlla_lunghezza(password):
    if len(password) >= 8:
        return 1
    else:
        return 0


def controlla_uppercase(password):
    if password.islower():
        return 0
    else:
        return 1

def controlla_isdigit(password):
    digit = 0
    for i in password:
        if i.isdigit():
            digit = digit +1
    if digit >0:
        return 1
    else:
        return 0


password = input("Inserisci password: ")

a = controlla_uppercase(password)
b = controlla_isdigit(password)
c = controlla_lunghezza(password)

risultato = a+b+c

if risultato == 3:
    print("Strong Password")
else:
    print("Weak Password")
