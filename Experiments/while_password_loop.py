password = input("Enter a password")
correct_password = "1234"

i = 1
while password != correct_password:
    password = input("Tentativo {}. Riprova a inserire la password".format(i))
    i = i + 1

print("Tentativo {}.Password corretta".format(i))