import datetime

def get_age(year_of_birth, current_year=datetime.date.today().year):
    year_of_birth = int(input("inserisci anno di nascita: "))
    anni = current_year - year_of_birth
    print(f"Sei nato nel {year_of_birth}. Hai {anni} anni")

a = get_age(1988)

