import random
minimo = 1
maximo = 20
numero_secreto = random.randint(minimo,maximo)
adivinado = False
intentos = 5

print("\nBienvenido al juego de adivinar el número secreto!\n")
    
while not adivinado:
    if intentos == 0:
        print("\n********************************\n           Perdiste!\n********************************\n\nEl numero secreto era el ", numero_secreto)
        break
    print("----------------------------------------\n")
    print("Tienes ", intentos, " intentos\n")
    numero = input(f"Elige un número del {minimo} al {maximo}: ")
    numero = int(numero)
    while numero < minimo or numero > maximo:
        print("\n********************************\n    Numero fuera del rango\n********************************\n")
        numero = input(f"Elige un número del {minimo} al {maximo}: ")
        numero = int(numero)
    if numero == numero_secreto:
        print("\n********************************\n           Ganaste!\n********************************\n")
        adivinado = True
    elif numero < numero_secreto:
        print("\nMás alto!\n")
        intentos -= 1
    else:
        print("\nMás abajo!\n")
        intentos -= 1