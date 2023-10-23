#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
def numImpares(numero:int) -> int:
    lista = []
    if numero < 1:
        raise ValueError("Introduce un numero positivo mayor que 0")
    
    for i in range(1, numero+1, 2):
        if 1 % 2 != 0:
            lista.append(i)
    return lista



def mensajeSalida(lista):
    return "Numeros impares: " + str(lista)


if __name__ == "__main__":
    #Entrada
    numeroCorrecto = False
    while not numeroCorrecto:
        try:
            numero = input("Introduce un numero positivo mayor qur 0: ")
            numero = int(numero)
            numeroCorrecto = True
        except ValueError:
            print("Introduce un numero.")
    #Proceso
    lista = numImpares(numero)
    mensaje = mensajeSalida(lista)
    #Salida
    print(mensaje)