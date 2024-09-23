# Objetivo: Analizar la situación de los alojamientos tipo airbnb in madrid
            
import os   # Libreria para trabajar con metodos del sistema operativo

from os import system
system("cls")

carpeta = "C:/proyectos/airbnb"
fichero = "madrid-airbnb-listings.csv"

ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)

import pandas as pd
import matplotlib.pyplot as plt

# Creamos un DataFrame desde la url del fichero csv

alojamientos = pd.read_csv(ruta, sep=';', decimal=',')

alojamientos['precio_persona'] = alojamientos['precio_persona'].round(2).convert_dtypes()

alojamientos['distrito'] = alojamientos['distrito'].astype(str)


# Apartado 1: Función que dibuja un diagrama de barras con el número de alojamientos por distritos.


def barras_alojamientos_distritos(alojamientos):
    
    # Definimos la figura y los ejes del gráfico
    fig, ax = plt.subplots()
    # Contamos las frecuencias de alojamientos por distritos y dibujamos las barras.
    alojamientos.distrito.value_counts().plot(kind = 'bar')
    # Ponemos el título
    ax.set_title('Número de alojamientos por distrito', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
    # Ponemos una rejilla
    ax.grid(axis = 'y', color = 'lightgray', linestyle = 'dashed')
    # Mostramos y guardamos el gráfico.
    plt.savefig("c:/proyectos/ejercicio71/diagrama_apartado1.png")
    plt.show()
    return

# llamada a la función: 
barras_alojamientos_distritos(alojamientos)


# Apartado 2: Función que dibuja un diagrama de barras con los porcentajes acumulados de tipos de alojamientos por distritos.


def barras_tipos_alojamientos_distritos(alojamientos):
    
    # Definimos la figura y los ejes del gráfico
    fig, ax = plt.subplots()
    # Agrupamos el DataFrame por distritos y contamos las frecuencias de los tipos de alojamiento. Después pivotamos el índice de los tipos de alojamientos para pasarlos a columnas y dibujamos las barras acumuladas.
    (alojamientos.groupby('distrito').tipo_alojamiento.value_counts(normalize = True)*100).unstack().plot(kind = 'bar', stacked = True, ax = ax)
    # Ponemos el título
    ax.set_title('Tipos de alojamiento por distrito (%)', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
    # Eliminamos la etiqueta del eje x
    ax.set_xlabel('')
    # Ponemos una rejilla
    ax.grid(axis = 'y', color = 'lightgray', linestyle = 'dashed')
    # Reducimos el eje x un 30% para que quepa la leyenda
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.7, box.height])
    # Dibujar la leyenda fuera del área del gráfico
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
   # Mostramos y guardamos el gráfico.
    plt.savefig("c:/proyectos/ejercicio71/diagrama_apartado2.png")
    plt.show()
    return

# llamada a la función: 
barras_tipos_alojamientos_distritos(alojamientos)


# Apartado 3: Función que dibuja un diagrama de sectores con la distribución del número de alojamientos por anfitrión de unos tipos y en unos distritos dados.


def sectores_tipos_alojamientos_anfitrion(alojamientos, distritos, tipos):

    # Definimos la figura y los ejes del gráfico
    fig, ax = plt.subplots()
    # Filtramos los distritos y los tipos de alojamientos 
    alojamientos_filtrados = alojamientos[alojamientos.distrito.isin(distritos) & alojamientos.tipo_alojamiento.isin(tipos)]
    # Contamos la frecuencia de alojamientos por anfitrión y dibujamos el diagrama de sectores
    alojamientos_filtrados.anfitrion.value_counts(normalize = True).plot(kind = 'pie', ax = ax)
    # Ponermos el título
    ax.set_title('Distribución del número de alojamientos por anfitrión\nDistritos de ' + ', '.join(distritos) + '\nTipos de alojamiento' + ','.join(tipos), loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
    # Eliminamos la etiqueta del eje y
    ax.set_ylabel('')
   # Mostramos y guardamos el gráfico.
    plt.savefig("c:/proyectos/ejercicio71/diagrama_apartado3.png")
    plt.show()
    return

# llamada a la función: 
sectores_tipos_alojamientos_anfitrion(alojamientos, ['Villaverde', 'Vicálvaro'], ['Entire home/apt', 'Hotel room'])


# Apartado 4: Función que dibuja un diagrama de barras con los precios medios por persona y día de cada distrito.

# Apartado 5: Función que dibuja un diagrama de barras con la distribución de precios por persona y día.


def barras_precios_medios_persona(alojamientos):
  
    # Definimos la figura y los ejes del gráfico
    fig, ax = plt.subplots()
    # Agrupamos por distrito, calculamos la media de precio por persona y dibujamos las barras.
    alojamientos.groupby('distrito').precio_persona.mean().plot(kind = 'bar', ax = ax)
    # Ponemos el título
    ax.set_title('Precio medio por persona y noche', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
    # Eliminamos la etiqueta del eje x
    ax.set_xlabel('')
    # Ponemos una rejilla
    ax.grid(axis = 'y', color = 'lightgray', linestyle = 'dashed')
    # Mostramos y guardamos el gráfico.
    plt.savefig("c:/proyectos/ejercicio71/diagrama_apartado4_6.png")
    plt.show()
    return

# llamada a la función: 
barras_precios_medios_persona(alojamientos)




# Apartado 6: Función que dibuja un diagrama de dispersión con el precio por noche y persona y la puntuación en unos distritos dados.


def precios_puntuacion_distritos(alojamientos, distritos):

    # Definimos la figura y los ejes del gráfico
    fig, ax = plt.subplots()
    # Filtramos los distritos
    alojamientos_filtrados = alojamientos[alojamientos.distrito.isin(distritos)]
    # Creamos una nueva columna con el precio por persona multiplicando el precio diario por el número mínimo de noches, sumando los gastos de limpieza y finalmente dividiendo por el número mínimo de noches y el número de plazas.
    alojamientos['precio_persona'] = (alojamientos.precio * alojamientos.noches_minimas + alojamientos.gastos_limpieza) / (alojamientos.noches_minimas + alojamientos.plazas)
    # Dibujamos el diagrama de sipersión
    ax.scatter(alojamientos['precio_persona'], alojamientos['puntuacion'])
    # Ponemos el título
    ax.set_title('Precios vs Puntuación\nDistritos de ' + ', '.join(distritos), loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
    # Ponemos las etiquetas de los ejes
    ax.set_xlabel('Precio en €')
    ax.set_ylabel('Puntuación')
    # Mostramos y guardamos el gráfico.
    plt.savefig("c:/proyectos/ejercicio71/diagrama_apartado5.png")
    plt.show()
    return

# llamada a la función: 
precios_puntuacion_distritos(alojamientos, ['Arganzuela', 'Centro'])

#-------------------------------------------------Fin-------------------------------------------------#

