import random
def v_numero(x):
    if x.isdigit():
        return 1
    else:
        return 0
Num_Usuario = input("Bienvenido/a, Este juego es sencillo, vamos a generar un numero aleatorio entre 0 y 100. \nUsted va a intentar adivinarlo, si no lo adivina le vamos a tirar pistas para llegar a este numero. \nIngrese el numero que crea usted: ")

Num_Random = int(random.randrange(101))
intentos = 0

while Num_Usuario != Num_Random:
    if v_numero(Num_Usuario) is 1:
        Num_Usuario = int(Num_Usuario)
        while Num_Usuario != Num_Random:
            Num_Usuario = int(Num_Usuario)
            if Num_Usuario < Num_Random:
                intentos+=1
                Num_Usuario = input("Tu numero es más chico que el numero que intenta adivinar, intentelo nuevamente: ")
            elif Num_Random < Num_Usuario:
                intentos+=1
                Num_Usuario = input("Tu numero es más grande que el numero que intenta adivinar, intentelo nuevamente: ")
    else:
        Num_Usuario = input("Error al ingresar su numero. \ningrese un caracter numerico para empezar el juego: ")
print(f"Felicidades el numero es: {Num_Random}, solo te tomo {intentos} intentos.")