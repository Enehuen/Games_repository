

print("Bienvenido, Empezaremos el Quiz con preguntas de cultura general.")


def resp_correcta(respu,respc):
    if respu.lower() == respc:
        return True
    else:
        return False


print("Pregunta 1: ¿Cuál es el país más grande del mundo por superficie?")
resp1=input("Tu respuesta es: ")
while resp1 != True:
    if  resp_correcta(resp1,"rusia") != False:
        print("Respuesta 1 correcta. \nPasemos a la siguiente pregunta.")
        resp2 = input("¿En qué año llegó el hombre a la luna?: ")
        while resp2 != True:
            if resp_correcta(resp1,"1969") != False:
                print("Respuesta 2 correcta. \nPasemos a la siguiente pregunta.")
                break
            else:
                resp1 =input("Respuesta incorrecta, Vuelva a intentarlo. \n¿En qué año llegó el hombre a la luna?: ")
    else:
        resp1 = input("Respuesta incorrecta, Vuelva a intentarlo. \nPregunta 1: ¿Cuál es el país más grande del mundo por superficie?: ")
    