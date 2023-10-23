#Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.

def pedirNumero():
    numeroCorrecto = False
    while not numeroCorrecto:
        try:
            numero = input("Introduce un numero positivo: ")
            numero = int(numero)
            numeroCorrecto = True
        except ValueError:
            print("La entrada no es correcta. Introduce un numero entero.")
            raise ValueError
    return numero

def mensajeSalida(numero):
    return "Su numero es: " + str(numero)


if __name__ == "__main__":
    #Entrada
    numero = pedirNumero()
    #Proceso
    mensaje = mensajeSalida(numero)
    #salida
    print(mensaje)
