import random 
op = ['piedra' , 'papel ', 'tijeras']

jugar = input('quieres jugar ? \r\n') 
while jugar :

    compu = str(random.choices(op))
    yo = input ('piedra, papel o tijera ... elije \r\n ' ).upper()
    print(f'la computadora ha elegido:  "{compu}"')