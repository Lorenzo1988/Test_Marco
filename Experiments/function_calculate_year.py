def calcola_eta(year_of_birth, current_year=None):
    if current_year is None:
        today = datetime.date.today()
        year = int(today.year)

    else:
        year = current_year
    year_birth= int(year_of_birth)
    age= year-year_birth
    return age

import datetime
today = datetime.date.today()
year = int(today.year)

eta = calcola_eta(1988,2000)
print(f"la mia età è : {eta}")


