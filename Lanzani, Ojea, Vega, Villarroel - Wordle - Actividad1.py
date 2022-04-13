from sys import flags
import time
from datetime import datetime
import random
from threading import Timer

print("")

print("¡Bienvenido a Wordle!")
time.sleep(2)
print("Tenés 120 segundos para adivinar la palabra de 5 letras")
time.sleep(3)
print("¡EMPECEMOS!")
time.sleep(1)
print("")

flagInterrupcion = 0

def ultimoIntento():
    global flagInterrupcion
    flagInterrupcion = 1
    print("\n")
    print("¡Última oportunidad!")
    print("")

t = Timer(120.0, ultimoIntento)
t.start()

arch = open("palabras.txt", "r")
diccionario = arch.readlines()
arch.close()

instanteInicial = datetime.now()

i = 0
for element in diccionario:
    diccionario[i] = element.replace("\n","")
    i += 1

palabraAcertar = random.choice(diccionario)
palabra = ""
x = 0
pistasLetras = ["  ", "  ", "  ", "  ", "  "]
pistasEscribir = ""
letrasRepetidas = []
mensajeCorrecto = "¡¡¡CORRECTO!!!"
mensajeSinTiempo = "¡Te quedaste sin tiempo!"

while (palabra != palabraAcertar) and (flagInterrupcion == 0):
    while len(palabra) != 5:
        palabra = str(input("Ingrese una palabra: "))
        if len(palabra) != 5:
            print("")
            print("¡La palabra tiene que ser de 5 letras!")
            print("")
    print(" ")
    for x in range (len(palabra)):
        print(palabra[x], end=" ")
    print(" ")
    for x in range (len(palabra)):
        if palabra[x] == palabraAcertar[x]:
            pistasLetras[x] = "= "
            letrasRepetidas.append(palabra[x])
    for x in range (len(palabra)):
        if (palabra[x] in palabraAcertar) and (letrasRepetidas.count(palabra[x]) < palabraAcertar.count(palabra[x])) and (pistasLetras[x] == "  "):
            pistasLetras[x] = "- "
            letrasRepetidas.append(palabra[x])
    for x in range (len(palabra)):
        pistasEscribir += pistasLetras[x]
    print(pistasEscribir)
    if palabra != palabraAcertar:
        palabra = ""
    else:
        flagInterrupcion = 1
    pistasLetras = ["  ", "  ", "  ", "  ", "  "]
    pistasEscribir = ""
    letrasRepetidas = []
    print("")

instanteFinal = datetime.now()
tiempo = instanteFinal - instanteInicial
segundos = tiempo.seconds

time.sleep(1)

if palabra == palabraAcertar:
    print("\n")
    for x in mensajeCorrecto:
        print(x, end=" ", flush=True)
        time.sleep(0.2)
    time.sleep(1)
    print("\n")
    print("Tardaste " + str(segundos) + " segundos")
    print("\n")
else:
    for x in mensajeSinTiempo:
        print(x, end=" ", flush=True)
        time.sleep(0.1)
    time.sleep(1)
    print("\n")