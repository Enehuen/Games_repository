

print("Bienvenido, Empezaremos el Quiz con preguntas de cultura general.")

conf = input("Si desea comenzar ingrese 'Si', en caso contrario ingrese 'No' ")
def resp_correcta(respu,respc):
    if respu.lower() == respc:
        return True
    else:
        return False



while conf == "Si":
    print("Pregunta 1: ¿Cuál es el país más grande del mundo por superficie?")
    resp1=input("Tu respuesta es: ")
    if  resp_correcta(resp1,"rusia") != False:
        print("Respuesta 1 correcta. \nPasemos a la siguiente pregunta.")
        resp2 = input("¿En qué año llegó el hombre a la luna?: ")
        while resp1 != True:
            if resp_correcta(resp2,"1969") != False:
                print("Respuesta 2 correcta. \nPasemos a la siguiente pregunta.")
                while resp2 != True:
                    resp3 = input("¿Cuál es la capital de Australia?")
                    if resp_correcta(resp3,"Canberra") != False:
                        print("Respuesta 3 correcta. \nPasemos a la siguiente pregunta.")
                        while resp3 != True:
                            resp4 = input("¿Qué vitamina se obtiene principalmente a través de la exposición al sol?")
                            if resp_correcta(resp4,"Vitamina D") != False:
                                print("Respuesta 4 correcta. \nPasemos a la siguiente pregunta.")
                                while resp4 != True:
                                    resp5 = input("¿Quién escribió 'Don Quijote de la Mancha'?")
                                    if resp_correcta(resp5,"Miguel de Cervantes") != False:
                                        print("Respuesta 5 correcta, Felicidades haz completado el Quiz")
                                    else:
                                        resp5 = input("Respuesta incorrecta, Vuelva a intentarlo. \n¿Quién escribió 'Don Quijote de la Mancha'?")
                            else: 
                                resp4 = input("Respuesta incorrecta, Vuelva a intentarlo. \n¿Qué vitamina se obtiene principalmente a través de la exposición al sol?")
                    else:
                        resp3 = input("Respuesta incorrecta, Vuelva a intentarlo. \n¿Cuál es la capital de Australia?")
            else:
                resp2 =input("Respuesta incorrecta, Vuelva a intentarlo. \n¿En qué año llegó el hombre a la luna?: ")
    else:
        resp1 = input("Respuesta incorrecta, Vuelva a intentarlo. \nPregunta 1: ¿Cuál es el país más grande del mundo por superficie?: ")
    