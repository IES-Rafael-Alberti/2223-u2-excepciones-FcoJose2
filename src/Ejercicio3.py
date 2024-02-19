#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto.

def cuentaAtras(numero):
    
    if numero < 1:
        raise ValueError("Introduce un numero positivo mayor que 0")
    lista = []
    for i in range(numero, -1, -1):
        lista.append(i)
    return lista

def mensajeSalida(lista):
    return "Cuenta atrás de los numeros: " + str(lista)


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
    lista = cuentaAtras(numero)
    mensaje = mensajeSalida(lista)
    #Salida
    print(mensaje)