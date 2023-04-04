#nomi_fam = ["lorenzo","stefania", "giorgio", "paolo"]
#nomi_fam.sort()
#print(nomi_fam)

#for index, item in enumerate(nomi_fam):

#    print(f"{index+1}. {item.capitalize()}")
#    print(type(index))


ips = ['100.122.133.105', '100.122.133.111']
prompt = input("Enter the index of the IP you want")
for i,j in enumerate(ips):
    scelta=ips[int(prompt)]
print(f"Hai scelto {scelta}")


buttons = [('John', 'Sen', 'Morro'), ('Lin', 'Ajay', 'Filip')]
for first, second, third in buttons:
    print(first, second, third)