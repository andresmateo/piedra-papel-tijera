nombre1 = input("JUGADOR 1: Ingresa tu nombre: ")
nombre2 = input("JUGADOR 2: Ingresa tu nombre: ")

jugador1 = input("JUGADOR 1 " + nombre1.upper() + ": ¿Qué elijes? ¿Piedra, papel o tijera?: ")
jugador2 = input("JUGADOR 2 " + nombre2.upper() + ": ¿Qué elijes? ¿Piedra, papel o tijera?: ")

condicion1 = jugador1 == "piedra" and jugador2 == "tijera"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijera" and jugador2 == "papel"

if jugador1 == jugador2:
    print("¡Es un empate!")
elif (condicion1) or (condicion2) or (condicion3):
    print("JUGADOR 1  " + nombre1.upper() + ": ¡Has ganado!")
else:
    print("JUGADOR 2  " + nombre2.upper() + ": ¡Has ganado!")