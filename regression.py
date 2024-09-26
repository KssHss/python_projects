import os   # Libreria para trabajar con metodos del sistema operativo

from os import system
system("cls")

carpeta = "C:/proyectos/regression"
fichero = ""

ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)

import random
import pandas as pd 
import matplotlib.pyplot as plt 

# Definir dos listas de números aleatorios del mismo tamaño lista1 y lista2, 
    # con valores entre 1 y 20, y crear las siguientes funciones:
# Definir el tamaño de las listas
tamaño = 10

# Generar las listas de números aleatorios
lista1 = [random.randint(1, 20) for _ in range(tamaño)]
lista2 = [random.randint(1, 20) for _ in range(tamaño)]

print('Lista 1 es: ')
print(lista1)

print('Lista 2 es: ')
print(lista2)


# Una función para calcular la media de cada lista de números.
def calcular_media(lista):
    
    return f"la media es: {round(sum(lista) / len(lista),2)}"

media_1 = calcular_media(lista1)
media_2 = calcular_media(lista2)

cabecera_media = "\nMedia de cada lista.\n"
cabecera_lista1 = ('\n****************** lista1 ******************\n')
cabecera_lista2 = ('\n****************** lista2 ******************\n')

with open (carpeta + "ejercicio76.csv", mode="w") as mensaje:
    mensaje.write (cabecera_media)
    mensaje.write (cabecera_lista1)
    mensaje.write (media_1)
    mensaje.write (cabecera_lista2)
    mensaje.write (media_2)
    
# Una función para calcular la varianza de cada lista de números.
def calcular_varianza(lista):
    
    media = round(sum(lista) / len(lista),2)
    
    return f"la varianza es: {round(sum((x - media) ** 2 for x in lista) / len(lista),2)}"


varianza_1 = calcular_varianza(lista1)
varianza_2 = calcular_varianza(lista2)

cabecera_varianza = "\n\nVarianza de cada lista.\n"
cabecera_lista1 = ('\n****************** lista1 ******************\n')
cabecera_lista2 = ('\n****************** lista2 ******************\n')

with open (carpeta + "ejercicio76.csv", mode="a") as mensaje:
    mensaje.write (cabecera_varianza)
    mensaje.write (cabecera_lista1)
    mensaje.write (varianza_1)
    mensaje.write (cabecera_lista2)
    mensaje.write (varianza_2)

# Una función para calcular la covarianza de las dos listas de números.
def calcular_covarianza(lista1, lista2):
    media1 = round(sum(lista1) / len(lista1),2)
    media2 = round(sum(lista2) / len(lista2),2)
    return f"La CoVarianza entre lista 1 y lista 2 es : {round(sum((x - media1) * (y - media2) for x, y in zip(lista1, lista2)) / len(lista1),2)}"

co_varianza = calcular_covarianza(lista1, lista2)
cabecera_co_varianza = "\n\n******************************\n\n"

with open (carpeta + "regression.csv", mode="a") as mensaje:
    mensaje.write (cabecera_co_varianza)
    mensaje.write (co_varianza)
    

# Una función para calcular los coeficientes de la recta de regresión de lista2 sobre lista1.
def calcular_coeficientes_recta_regresion(lista1, lista2):
    media1 = round(sum(lista1) / len(lista1),2)
    media2 = round(sum(lista2) / len(lista2),2)
    covarianza = round(sum((x - media1) * (y - media2) for x, y in zip(lista1, lista2)) / len(lista1),2)
    varianza = round(sum((x - media1) ** 2 for x in lista1) / len(lista1),2)
    b = round(covarianza / varianza,2)
    a = round(media2 - b * media1,2)
    
    return f"Los coeficientes de la recta de regresión de lista 2 sobre lista 1 son: {a, b}"

coef_regresion = calcular_coeficientes_recta_regresion(lista1, lista2)
cabecera_coef_regresion = "\n\n******************************\n\n"

with open (carpeta + "ejercicio76.csv", mode="a") as mensaje:
    mensaje.write (cabecera_coef_regresion)
    mensaje.write (coef_regresion)

# Una función que devuelva el diagrama de dispersión y la recta de regresión 
def diagrama_dispersion_recta_regresion(lista1, lista2):
    media1 = round(sum(lista1) / len(lista1),2)
    media2 = round(sum(lista2) / len(lista2),2)
    covarianza = round(sum((x - media1) * (y - media2) for x, y in zip(lista1, lista2)) / len(lista1),2)
    varianza = round(sum((x - media1) ** 2 for x in lista1) / len(lista1),2)
    b = round(covarianza / varianza,2)
    a = round(media2 - b * media1,2)
    plt.scatter(lista1, lista2, color='b', label='Datos')
    plt.plot(lista1, [a + b * x for x in lista1], color='r', label='Recta de Regresión')
    plt.title('Diagrama de dispersión y Recta de regresión')
    plt.xlabel('Lista 1')
    plt.ylabel('Lista 2')
    plt.legend(bbox_to_anchor = (1.05, 1), loc = 'upper left')
    plt.savefig(carpeta + 'Diagrama de dispersión y Recta de regresión', bbox_inches = 'tight')              
    plt.show()
    return

dispersion_regresion = diagrama_dispersion_recta_regresion(lista1, lista2)