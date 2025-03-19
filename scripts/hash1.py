import random
from werkzeug.security import generate_password_hash #libreria para aplciar hash
minus = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
simbolos ="@$"

base = minus+numeros+simbolos #combinacion para la contraseña base
longitud = 6 #tamaño de contraseña
for n in range(20):
    muestra = random.sample(base, longitud) #crea una contraseña
    password ="".join(muestra) #union de cada caracter
    password_encriptado = generate_password_hash(password) #encriptacion hash de contraseña
    print("Contraseña {}: {} ► {}".format(n+1,password,password_encriptado))
    #imprime contraseña generada aleatoria y la encriptacion hash