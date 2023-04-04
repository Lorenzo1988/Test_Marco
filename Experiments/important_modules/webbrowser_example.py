import webbrowser

#user_term = input("Inserisci la parola da cercare sul browser: ")
#versione più corretta che sostituisce gli spazi con i + della ricerca URL
user_term = input("Inserisci la parola da cercare sul browser: ").replace(" ","+")
webbrowser.open("https://google.com/search?q="+user_term)


