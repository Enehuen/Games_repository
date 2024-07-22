

print("Bienvenido, Empezaremos el Quiz con preguntas de cultura general.")

print("Pregunta 1: ¿Cuál es el país más grande del mundo por superficie?")
resp1=input("Tu respuesta es: ")
while resp1 != True:
    if  resp1.lower() == "rusia":
        resp1 = True
        print("Respuesta 1 correcta. \n Pasemos a la siguiente pregunta.")
        
    else:
        resp1 = input(print("Respuesta incorrecta, Vuelva a intentarlo. Pregunta 1: ¿Cuál es el país más grande del mundo por superficie?:"))
        