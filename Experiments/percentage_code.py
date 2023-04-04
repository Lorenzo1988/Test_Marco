while True:
    try:
        try:
            total_value = float(input("Enter total value: "))
            value = float(input("Enter value: "))

            percentage = value / total_value * 100
            print(f"That is {percentage}%")
        except ValueError:
            print("You need to enter a number. Run the program again.")
            continue
        except ZeroDivisionError:
            print("Your total value cannot be zero.")
            continue
    except ValueError:
        print("Errore di valore")
        continue
    break