import random

def generarContraseña(largo):
    caracteres = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"
    contraseña = ""

    for pop in range(largo):
        #La contraseña debe contener letras y números al azar.
        contraseña += random.choice(caracteres)
    
    return contraseña

#Se deberá solicitar al usuario la cantidad de caracteres que desea que tenga su contraseña.
cantidadCaracteres = int(input("Ingrese que tan larga quiere que sea su contraseña: "))

if cantidadCaracteres < 1:
    print("La contraseña debe al menos tener un caracter :/")
else:
    contraseñahecha = generarContraseña(cantidadCaracteres)
    print("Contraseña generada:", contraseñahecha)

'''
Crea un generador de contraseñas
#Se deberá solicitar al usuario la cantidad de caracteres que desea que tenga su contraseña.
#La contraseña debe contener letras y números al azar.
'''