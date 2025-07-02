try:
    hours_input = input("Que horas são? ")
    hours = int(hours_input)

    is_morning = hours >= 0 and hours <= 11
    is_afternoon = hours >= 12 and hours <= 17
    is_night = hours >= 18 and hours <= 23

    if is_morning:
        print("Olá! Tenha um bom-dia!")
    if is_afternoon:
        print("Olá! Tenha uma boa-tarde!")
    if is_night:
        print("Olá! Tenha uma boa-noite!")
except ValueError:
    print("Informe um número inteiro")
