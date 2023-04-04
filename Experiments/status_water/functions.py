SOGLIA_GHIACCIO = 0
SOGLIA_GAS = 100

def status_water(temperature):
    try:
        if float(temperature) < SOGLIA_GHIACCIO:
            status = "Solid"
        elif float(temperature) < SOGLIA_GAS:
            status = "Liquid"
        elif float(temperature) > SOGLIA_GAS:
            status = "Gas"
        else:
            ("Error")
    except ValueError:
        print("Non hai inserito un numero!")
        status = ""
    return status


