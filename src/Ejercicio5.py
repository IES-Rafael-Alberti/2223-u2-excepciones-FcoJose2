#Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!"

def comprobarContraseña(contraseña):
    if contraseña != "Contraseña":
        print("Incorrect Password!!")
        raise NameError
    else:
        return contraseña
    
def mensajeSalida(contraseña):
    return "La contraseña " + str(contraseña) + " es correcta."


if __name__ == "__main__":
    #Entrada
    contraseña = input("Introduzca la contraseña: ")
    #Proceso
    resultado = comprobarContraseña(contraseña)
    mensaje = mensajeSalida(contraseña)
    #Salida
    print(mensaje)





