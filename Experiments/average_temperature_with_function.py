file_directory = "../lessons/files/temperatures"
file_name = "temperatures.txt"
file_temperature=file_directory+"/"+file_name
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def get_average(file):
    with (open(file, "r")) as file_local:
        print(f"Sto aprendo il file {file} in modalità lettura")
        data_local = file_local.readlines()
        print(f"type_data_local: {type(data_local)}")
        lista_numeri = [float(item.strip('\n')) for item in data_local if isfloat(item.strip('\n'))]
        average_local = sum(lista_numeri) / len(lista_numeri)
        print(f"La media calcolata è: {average_local}")
        return average_local

try:
    average = get_average(file=file_temperature)
except ZeroDivisionError:
    print("0 Temperature inserite. Non posso fare la media")

