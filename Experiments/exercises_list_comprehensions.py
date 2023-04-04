print("Esercizio1")
names = ["john smith", "jay santi", "eva kuki"]
names_cap = [name.title() for name in names]
print (names_cap)


print("Esercizio2")
usernames = ["john 1990", "alberta1970", "magnola2000"]
lunghezze = [len(username) for username in usernames]
print(lunghezze)

print("Esercizio3")

user_entries = ['10', '19.1', '20']
decimali = [float(i) for i in user_entries]
print(decimali)


print("Esercizio4")
user_entries = ['10', '19.1', '20']

somma = sum([float(i) for i in user_entries])
print(somma)


