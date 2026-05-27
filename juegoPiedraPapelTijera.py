termino = False

print("\nBienvenidos al Piedara, Papel o Tijeras!\n")
print("--------------------------------------------------------------------")

nombre1 = input("¿Cómo se llama el Jugador 1?\n")
nombre2 = input("\n¿Cómo se llama el Jugador 2?\n")

while not termino:
    jugador1 = input(f"\nHola {nombre1}. ¿Qué eliges? Piedra, Papel o Tijera: ")
    jugador1 = jugador1.strip().lower()
    while (jugador1 != "piedra") and (jugador1 != "papel") and (jugador1 != "tijera"):
        jugador1 = input("\nNo te entendí. Elige entre: Piedra, Papel o Tijera: ")
        jugador1 = jugador1.strip().lower()
    jugador2 = input(f"\nHola {nombre2}. ¿Qué eliges? Piedra, Papel o Tijera: ")
    jugador2 = jugador2.strip().lower()
    while (jugador2 != "piedra") and (jugador2 != "papel") and (jugador2 != "tijera"):
        jugador2 = input("\nNo te entendí. Elige entre: Piedra, Papel o Tijera: ")
        jugador2 = jugador2.strip().lower()

    if jugador1 == jugador2:
        print("\n********************************\n            Empate!\n********************************\n\nVuelvan a intentar\n")
    elif (jugador1 == "tijera" and jugador2 == "papel") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "piedra" and jugador2 == "tijera"):
        print(f"\n********************************\n      Ganó {nombre1}!\n********************************\n")
        termino = True
    else:
        print(f"\n********************************\n      Ganó {nombre2}!\n********************************\n")
        termino = True
