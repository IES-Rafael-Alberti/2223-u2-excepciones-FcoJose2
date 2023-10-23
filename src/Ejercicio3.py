#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto.









if __name__ == "__main__":
    #Entrada
    numeroCorrecto = False
    while not numeroCorrecto:
        try:
            numero = input("Introduce un numero positivo: ")
            numero = int(numero)
            numeroCorrecto = True
        except ValueError:
            print("Introduce un numero.")
    #Proceso
    lista = numImpares(numero)
    mensaje = mensajeSalida(lista)
    #Salida
    print(mensaje)