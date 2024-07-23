

name= input("Bienvenido/a, Empezaremos el Quiz con preguntas de cultura general.\n¿Podrias decirme tu nombre? ")

conf = input(f"Muy bien {name}. Cada respuesta correcta suma 2 puntos y cada incorrecta resta 1 punto \nSi desea comenzar ingrese 'Si', en caso contrario ingrese 'No': ")
def resp_correcta(respu,respc):
    if respu.lower() == respc:
        return True
    else:
        return False

puntaje=0

while conf.lower() == "si":
    resp1=input("Pregunta 1: ¿Cuál es el país más grande del mundo por superficie? \nTu respuesta es: ")
    if  resp_correcta(resp1,"rusia") != False:
        print(f"Respuesta correcta, {name} suma 2 puntos. \nPasemos a la siguiente pregunta.")
        puntaje += 2
        resp2 = input("¿En qué año llegó el hombre a la luna? \nTu respuesta es: ")
        while resp1 != True:
            if resp_correcta(resp2,"1969") != False:
                print(f"Respuesta correcta, {name} suma 2 puntos. \nPasemos a la siguiente pregunta.")
                puntaje += 2
                resp3 = input("¿Cuál es la capital de Australia? \nTu respuesta es: ")
                while resp2 != False:
                    if resp_correcta(resp3,"canberra") != False:
                        print(f"Respuesta correcta, {name} suma 2 puntos. \nPasemos a la siguiente pregunta.")
                        puntaje += 2
                        resp4 = input("¿Qué vitamina se obtiene principalmente a través de la exposición al sol? \nTu respuesta es: ")
                        while resp3 != True:
                            if resp_correcta(resp4,"vitamina d") != False:
                                print(f"Respuesta correcta, {name} suma 2 puntos. \nPasemos a la siguiente pregunta.")
                                puntaje += 2
                                resp5 = input("¿Quién escribió 'Don Quijote de la Mancha'? \nTu respuesta es: ")
                                while resp4 != True:
                                    if resp_correcta(resp5,"miguel de cervantes") != False:
                                        puntaje += 2
                                        print(f"Respuesta correcta, {name} suma 2 puntos. \nFelicidades haz completado el Quiz con una puntuación de {puntaje} puntos.")
                                        quit()
                                    else:
                                        puntaje -= 1
                                        resp5 = input(f"Respuesta incorrecta, {name} pierde 1 punto,. Vuelva a intentarlo. \n¿Quién escribió 'Don Quijote de la Mancha'? \nTu respuesta es: ")
                            else: 
                                puntaje -= 1
                                resp4 = input(f"Respuesta incorrecta, {name} pierde 1 punto,. Vuelva a intentarlo. \n¿Qué vitamina se obtiene principalmente a través de la exposición al sol? \nTu respuesta es: ")
                    else:
                        puntaje -= 1
                        resp3 = input(f"Respuesta incorrecta, {name} pierde 1 punto,. Vuelva a intentarlo. \n¿Cuál es la capital de Australia? \nTu respuesta es: ")
            else:
                puntaje -= 1
                resp2 =input(f"Respuesta incorrecta, {name} pierde 1 punto,. Vuelva a intentarlo. \n¿En qué año llegó el hombre a la luna? \nTu respuesta es: ")
    else:
        puntaje -= 1
        resp1 = input(f"Respuesta incorrecta, {name} pierde 1 punto,. Vuelva a intentarlo. \nPregunta 1: ¿Cuál es el país más grande del mundo por superficie? \nTu respuesta es:  ")
    