import json

with (open("domande.json", "r")) as file_json:
    content = file_json.read()

data = json.loads(content)
print(f"data: {data}")

#print(f"il type(content) è: {type(content)}")
#print(f"il type(data) è: {type(data)}")

for domanda in data:
    print(domanda["contenuto_domanda"])
    for index,alternative in enumerate(domanda["possibili_risposte"]):
        print(index+1," - ", alternative)
    scelta_utente = int(input("Inserisci la risposta:\t"))
    #inserisco la risposta data dall'utente come ulteriore dizionario
    domanda["scelta_utente"] = scelta_utente

#printo le risposte date dall'utente

score = 0
for index,domanda in enumerate(data):
    if domanda["scelta_utente"] == domanda["risposta_corretta"]:
        score += 1
        risultato = "Risposta CORRETTA"
    else:
        risultato = "Risposta ERRATA"

    message = f"{index + 1}. {risultato}.\t \
    La risposta data è {domanda['scelta_utente']}.\t \
    La risposta corretta è {domanda['risposta_corretta']}"
    print(message)

print(f"\nIl punteggio finale è: {score} / {len(data)}")
