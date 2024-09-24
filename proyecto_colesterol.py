MatPlotLib y SciPy

# El fichero “control_colesterol.csv" tiene la información anónima de un estudio de 60 pacientes donde
    # se indica su edad, peso, estatura y niveles de colesterol. 
    # Crear un programa que realice las siguientes operaciones utilizando las librerías NumPy, Pandas, SciPy y Matplotlib:

import os   # Libreria para trabajar con metodos del sistema operativo

from os import system
system("cls")

carpeta = "C:/proyectos/ejercicio_77/"          # Indicar carpeta de destino de los ficheros que se vayan generando
fichero = ""

ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)

import numpy as np                              # Importar resto de librerias 
import pandas as pd 
import scipy.stats as ss
import matplotlib.pyplot as plt


# 1. Crear un DataFrame indexado por ID de cliente 
    # y ajustar los valores numéricos a formato decimal con dos decimales. Guardarlo en el fichero apartado4_1.csv.


# ************************************* PASO1: importar datos del fichero a un dataframe pandas *************************************

df_colesterol = pd.read_csv(carpeta + "control_colesterol.csv", sep=';', decimal=',')       
print(df_colesterol)
df_colesterol.info()

# ****************************************** PASO2: Indexacion y Conversión Numérica ******************************************

df_colesterol = df_colesterol.set_index('id')                   # Indexacion 

df_colesterol['edad'] = round(df_colesterol['edad'].astype(float),2)        # Conversión Numérica
df_colesterol['peso'] = round(df_colesterol['peso'].astype(float),2)
df_colesterol['altura'] = round(df_colesterol['altura'].astype(float),2)
df_colesterol['colesterol'] = round(df_colesterol['colesterol'].astype(float),2)
df_colesterol.info()

df_colesterol.to_csv(carpeta + "apartado4_1.csv", index=True, sep=';', decimal=',')       # carga a fichero .csv, marcando decimales com comas

# 2. Calcular la media, mediana, moda, los percentiles 30, 60 y 90, el rango, IQR, coeficiente de variación, 
    # varianza y desviación típica de la edad, peso, altura y nivel de colesterol para todo el estudio redondeando los cálculos a 2 decimales. 
    # Mostrar los datos por terminal y guardar la información en el fichero apartado4_2_3.csv.

# **************** PASO1: Creación de variables para los resultados referentes a cada columna (edad, peso, altura, colesterol) ****************


edad = df_colesterol['edad']
peso = df_colesterol['peso']
altura = df_colesterol['altura']
colesterol = df_colesterol['colesterol']

# ****************************************** PASO2: Creación de la función cálculos ******************************************

def calculos(df, variable, nombre_variable):       


    print('\n\n' + '*************************Cálculos de la columna edad*************************' + '\n\n')

    media_variable = f"\nla media de {nombre_variable} es: {round(variable.mean(),2)}"
    print(media_variable)

    mediana_variable = f"\nla mediana de {nombre_variable} es: {variable.median()}"
    print(mediana_variable)

    moda_variable = f"\nla moda de {nombre_variable} es: {variable.mode().values[0]}"
    print(moda_variable)

    variable_p30 = f"\nel percentil 30 de {nombre_variable} es: {variable.quantile(0.3)}"
    print(variable_p30)

    variable_p60 = f"\nel percentil 60 de {nombre_variable} es: {variable.quantile(0.6)}"
    print(variable_p60)

    variable_p90 = f"\nel percentil 90 de {nombre_variable} es: {variable.quantile(0.9)}"
    print(variable_p90)

    rango_variable = f"\nel rango de {nombre_variable} es: {round(variable.max() - variable.min(), 2)}"
    print(rango_variable)

    iqr_variable = f"\nel rango intercuartílico de {nombre_variable} es: {round(variable.quantile(0.75) - variable.quantile(0.25), 2)}"
    print(iqr_variable)

    variacion_variable = f"\nel coeficiente de variación de {nombre_variable} es: {round(ss.variation(df['edad']),2)}"
    print(variacion_variable)

    varianza_variable = f"\nLa varianza de {nombre_variable} es: {round(variable.var(ddof=0),2)}"
    print(varianza_variable)

    std_variable = f"\nla desviación estándar de {nombre_variable} es: {round(variable.std(ddof=0),2)}"
    print(std_variable)

    resultado_variable = ('\n'+ media_variable + ';' + '\n'+  mediana_variable + ';' + '\n'+ moda_variable + '\n' +  variable_p30  + ';' + variable_p60 + ';' 
                    + variable_p90 + '\n' + ';' + rango_variable + ';' + iqr_variable + '\n' + variacion_variable + ';' + varianza_variable + ';' + std_variable
                    + '\n')         # una concatenación de todos los cálculos solicitados
                     

    

    return(resultado_variable)


# ****************************************** PASO3: Llamada a la función para cada columna ******************************************

resultado_edad= calculos(df_colesterol, edad, 'edad')       
resultado_peso= calculos(df_colesterol, peso, 'peso')      
resultado_altura= calculos(df_colesterol, altura, 'altura')      
resultado_colesterol= calculos(df_colesterol, colesterol, 'colesterol')      


cabecera_general = "\nCálculos estadísticos de la columan edad, peso, altura y colesterol.\n"  

cabecera_edad = ('\n****************** EDAD ******************\n')
cabecera_peso = ('\n\n****************** PESO ******************\n')
cabecera_altura = ('\n\n****************** ALTURA ******************\n')
cabecera_colesterol = ('\n\n****************** COLESTEROL ******************\n')

with open (carpeta + "apartado4_2_3.csv", mode="w") as mensaje:
    mensaje.write (cabecera_general)

    mensaje.write (cabecera_edad)
    mensaje.write (resultado_edad)

    mensaje.write (cabecera_peso)
    mensaje.write (resultado_peso)

    mensaje.write (cabecera_altura)
    mensaje.write (resultado_altura)

    mensaje.write (cabecera_colesterol)
    mensaje.write (resultado_colesterol)


# 3. Repetir los cálculos del apartado anterior diferenciando por sexo (H / M). 
    # Mostrar los datos por terminal y añadir todos estos cálculos con los anteriores en el fichero de salida apartado4_2_3.csv.

# ******************************** PASO1: Creación de dataframe para Hombres y dataframe para Mujeres ********************************
    
df_hombres = df_colesterol.loc[(df_colesterol['sexo'] == 'H')]
df_mujeres = df_colesterol.loc[(df_colesterol['sexo'] == 'M')]
    





# *********************************** PASO2: Llamada a la función calculos con cada dataframe   ***********************************

resultado_edad_hombres = calculos(df_hombres, df_hombres['edad'], 'edad')       
resultado_peso_hombres = calculos(df_hombres, df_hombres['peso'], 'peso')      
resultado_altura_hombres = calculos(df_hombres, df_hombres['altura'], 'altura')      
resultado_colesterol_hombres = calculos(df_hombres, df_hombres['colesterol'], 'colesterol')     


resultado_edad_mujeres = calculos(df_mujeres, df_mujeres['edad'], 'edad')        
resultado_peso_mujeres = calculos(df_mujeres, df_mujeres['peso'], 'peso')      
resultado_altura_mujeres = calculos(df_mujeres, df_mujeres['altura'], 'altura')      
resultado_colesterol_mujeres = calculos(df_mujeres, df_mujeres['colesterol'], 'colesterol')   

# *********************************** PASO3: Diseño y Ejecución de fichero de salida para cada dataframe ***********************************

cabecera_hombres = "\nCálculos estadísticos de la columan edad, peso y colesterol en hombres.\n"        # Fichero Hombres

with open (carpeta + "apartado4_2_3.csv", mode="a") as mensaje:
    mensaje.write (cabecera_hombres)

    mensaje.write (cabecera_edad)
    mensaje.write (resultado_edad_hombres)

    mensaje.write (cabecera_peso)
    mensaje.write (resultado_peso_hombres)

    mensaje.write (cabecera_altura)
    mensaje.write (resultado_altura_hombres)

    mensaje.write (cabecera_colesterol)
    mensaje.write (resultado_colesterol_hombres)


cabecera_mujeres = "\nCálculos estadísticos de la columan edad, peso y colesterol en mujeres.\n"        # Fichero Mujeres

with open (carpeta + "apartado4_2_3.csv", mode="a") as mensaje:
    mensaje.write (cabecera_mujeres)

    mensaje.write (cabecera_edad)
    mensaje.write (resultado_edad_mujeres)

    mensaje.write (cabecera_peso)
    mensaje.write (resultado_peso_mujeres)

    mensaje.write (cabecera_altura)
    mensaje.write (resultado_altura_mujeres)

    mensaje.write (cabecera_colesterol)
    mensaje.write (resultado_colesterol_mujeres)



# 4. El riesgo de que una persona sufra enfermedades coronarias depende de su edad y su índice de masa corporal (IMC). 
    # El índice de masa corporal es la división entre el peso del individuo en kilos y el cuadrado de su estatura en metros:
    # Añadir al DataFrame dos columnas, IMC y Riesgo, y rellenarlas a partir de los datos de estatura, el peso y la edad de una persona. 
    # Generar un fichero apartado4_4.csv con el DataFrame incluyendo las nuevas columnas.

# *********************************** PASO1: Cálculo del Indice de Masa Corporal ***********************************
    
df_colesterol['IMC'] = round(df_colesterol['peso'] / df_colesterol['altura'] ** 2,2)        # columna nueva de IMC 

# *********************************** PASO2: Función de Cálculo del Riesgo Coronario ***********************************

def riesgo_coronario(edad, imc):
    if edad < 45: 
        if imc < 25:
            return "Bajo"
        else: 
            return "medio"
    if edad >= 45:
        if imc < 25:
            return "medio"
        else:
            return "alto"
 
df_colesterol['riesgo_coronario'] = df_colesterol.apply(lambda row:                  # columna nueva de riesgo_coronario
                                                        riesgo_coronario(row['edad'], 
                                                                         row['IMC']), axis=1)      

print(df_colesterol)            # comprobar el dataframe resultante con las 2 nuevas columnas 


# *********************************** PASO3: Carga a fichero de salida .csv ***********************************

df_colesterol.to_csv(carpeta + "apartado4_4.csv", index=True, sep=';', decimal=',')

# 5. Para establecer la relación entre el nivel de colesterol y el IMC 
    # vamos a realizar una función a la que se le pase el Dataframe anterior y realice los siguientes cálculos diferenciando por sexos:
        # • Covarianza de los valores de colesterol y el IMC.
        # • Coeficientes de la recta de regresión de IMC sobre los valores de colesterol. 
        # • Diagramas de dispersión y la recta de regresión de ambas variables.

# Guardar los datos en los ficheros apartado5_5.csv, incluyendo los datos calculados para Hombres y para Mujeres.
# Generar y guardar dos diagramas con la dispersión y recta de regresión apartado5_5H.png y apartado5_5M.png incluyendo título, leyenda, etc…


# *********************************** PASO1: Creación de la función ***********************************

def fc_covar_regresion(df):

                # *********************************** PASO1.1: Cálculo de la CoVarianza ***********************************
    media_imc = round(df['IMC'].mean(),2)
    media_colesterol = round(df["colesterol"].mean(),2)
    covarianza = round(df['colesterol'].cov(df['IMC']),2)

    co_var = f"La CoVarianza de los valores de colesterol y el IMC es : {covarianza}"

                # **** PASO1.2: Cálculo de los coeficientes de la recta de regresión de IMC sobre los valores del colesterol ****
    
    varianza_colesterol = round(df["colesterol"].var(ddof=0),2)
    b = round(covarianza / varianza_colesterol,2)
    a = round(media_imc - b * media_colesterol,2)

    coefc_regresion = f"Los coeficientes de la recta de regresión de IMC sobre los valores de colesterol : {a,b}"

                # *********** PASO1.3: Adición de variable letra y genero para marcar los diagramas resultantes ***********

    if df is df_hombres: 
        letra = 'H'
        genero = 'en Hombres'
    elif df is df_mujeres: 
        letra = 'M'
        genero = 'en Mujeres'

                # ******************* PASO1.4: Dibujo del diagrama de dispersión y recta de regresión *******************   
         
    plt.scatter(df['colesterol'], df['IMC'], color='b', label='Dispersión')
    plt.plot(df['colesterol'], [a + b * x for x in df['colesterol']], color='r', label='Recta de Regresión')
    plt.title('Diagrama de dispersión y Recta de regresión' + genero)
    plt.xlabel('Nivel de Colesterol')
    plt.ylabel('Índice de Masa Corporal')
    plt.legend(bbox_to_anchor = (1, 1), loc = 'upper left')
    plt.savefig(carpeta + 'apartado5_5' + letra, bbox_inches = 'tight')              
    plt.show()

    resultado_final = co_var + ';' + '\n' + coefc_regresion + ';' + '\n'
    return(resultado_final)


# *********** PASO2: Creación de dataframes para hombres y mujeres con las nuevas columnas IMC y riesgo_coronario ***********


df_hombres = df_colesterol.loc[(df_colesterol['sexo'] == 'H')]
df_mujeres = df_colesterol.loc[(df_colesterol['sexo'] == 'M')]  

# *********************************** PASO3: Llamada a la función para cada dataframe ***********************************
calculos_hombres = fc_covar_regresion(df_hombres)
calculos_mujeres = fc_covar_regresion(df_mujeres)


# *********************************** PASO3: Diseño y Ejecución de fichero de salida para cada dataframe ***********************************

cabecera_calculos_imc = "\n\n**************** Cálculos de la relación entre el nivel de colesterol y el IMC.  **************\n\n"
cabecera_hombres = "\n**************** Covarianza y Coeficientes de regresión en hombres. ****************\n"
cabecera_mujeres = "\n**************** Covarianza y Coeficientes de regresión en mujeres. ****************\n"

with open (carpeta + "apartado5_5.csv", mode="w") as mensaje:
    mensaje.write (cabecera_calculos_imc)

    mensaje.write (cabecera_hombres)
    mensaje.write (calculos_hombres)

    mensaje.write (cabecera_mujeres)
    mensaje.write (calculos_mujeres)

# ************************************************************ FIN  ************************************************************ 
    



