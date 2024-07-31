import random
jugador= input("El mundialmente conocido piedra, papel o tijera. cada victoria le otorga 2 puntos, cada empate 1 y cada derrota 0, lo mismo para la computadora Ingrese su nombre para comenzar: ")
puntos = 0
def asignacion(x):
    if x==0:
        x="tijera"
        return x
    elif x==1:
        x="piedra"
        return x
    else:
        x="papel"
        return x
while True:
    usuario = input("Ingrese su opcion, Piedra, Papel o Tijera. Para finalizar ingrese 'x': ").lower()
    compu = random.randrange(3)
    compu = asignacion(compu)
    if usuario !='x':
        if usuario == "tijera":
            if compu=="tijera":
                puntos +=1
                print(f"Empate, el jugador {jugador} suma 1 punto.")
            elif compu=="papel":
                puntos+=2
                print(f"El jugador {jugador} suma 2 puntos.")
            else:
                print(f"El jugador {jugador} no suma puntos.")
        elif usuario =="papel":
            if compu=="tijera":
                print(f"El jugador {jugador} no suma puntos.")
            elif compu=="papel":
                puntos+=1
                print(f"El jugador {jugador} suma 1 punto.")
            else:
                puntos+=2
                print(f"El jugador {jugador} suma 2 puntos.")
        elif usuario =="piedra":
            if compu=="tijera":
                puntos+=2
                print(f"El jugador {jugador} suma 2 puntos.")
            elif compu=="papel":
                print(f"El jugador {jugador} no suma puntos.")
            else:
                puntos+=1
                print(f"El jugador {jugador} suma 1 punto.")
    else:
        break
print(f"{jugador} a finalizado con {puntos}")
        