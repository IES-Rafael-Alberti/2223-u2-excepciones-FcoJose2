#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).



def contarEdad(edad:int) -> int:
    lista = []
    if edad < 1:
        raise ValueError("No puedes tener edad negativa.")
    for i in range(1, edad+1):
        lista.append(i)
    return lista




if __name__ == "__main__":
    numeroCorrecto = False
    while not numeroCorrecto:
        try:
            edad = input("Introduzca su edad: ")
            edad = int(edad)
            numeroCorrecto = True
        except ValueError:
            print("Introduce un numero.")

    mensaje = contarEdad(edad)
    print(mensaje)