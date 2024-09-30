# Escribir un programa para gestionar las citas de una consulta médica. La base de datos de citas deberá
    # almacenarse en una base de datos de MySQL, y al final de la ejecución deberá guardarse una copia
    # en un fichero de nombre citas.csv. Cada cita contendrá los siguientes campos:
        # • Numero_cita: Autonumérico, clave primaria.
        # • Dni_Nie: Tamaño de 9 caracteres, campo obligatorio, con verificación de si es correcto o no el dato introducido.
        # • Fecha: Tipo Datetime, almacenando Año, Mes, Dia, Horas y Minutos. Campo obligatorio.
        # • Especialidad: tamaño de 25 caracteres, admitiendo solamente los siguientes valores:
                    # o Medicina.
                    # o Enfermería.
                    # o Analítica.
                    # o Vacunación.
                    # o Otras gestiones.
        # • Cita_activa: Booleana, campo obligatorio, con valor SI/NO o True/False para controlar si la cita está activa o no.
            # las citas por defecto serán activas.
    # Es necesario que la primera fila del csv de copia contenga los nombres de los campos. 


# meter preg 1 y 2 en un programa y luego 3,4,5 en otro programa todos metidos en la misma función. 


import os   # Libreria para trabajar con metodos del sistema operativo
from os import system

carpeta = "C:/proyectos/citas_medicas/"
fichero = "citas.csv"

ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)

from datetime import date                           # Para trabajar con fechas
from datetime import datetime                       # Para trabajar con horas
from datetime import timedelta                      # Para operar con dias
from dateutil.relativedelta import relativedelta    # Para trabajar con fechas

import pandas as pd 
import mysql.connector

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", db="")
cursor1=conexion1.cursor()      


# El programa debe incluir las siguientes funciones:
    # 1. Una función que permita generar la base de datos en MySQL y cargue, si existe, el fichero citas.csv.


def fc_dni_nie(dato):

    letras = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

    dato = dato.upper()

    if (len(dato) != 9):  
        print("Opción no válida. Repítelo.")        
        return False
    
    if (ord(dato[0]) >= 48) and (ord(dato[0]) <= 57):   

        testigo=True
    
        for i in range(8):
            if (ord(dato[i]) < 48) or (ord(dato[i]) > 57):     
                testigo=False

        if (testigo==False):
            print("Opción no válida. Repítelo.")
            return False
        else:
            letra = dato[8]
            numero = dato.replace(letra,"")
            numero = int(numero)
            resto = numero % 23
            if (letras[resto] == letra):
                return True
            else:
                print("Opción no válida. Repítelo.")
                return False
       
    else:                                               

        letraini = dato[0]
        letrafin = dato[8]

        numero = dato.replace(letraini,"")
        numero = numero.replace(letrafin,"")

        testigo=True

        for i in range(7):
            if (ord(numero[i]) < 48) or (ord(numero[i]) > 57):      
                testigo=False

        if (testigo==False):
            print("Opción no válida. Repítelo.")
            return False
        else:

            match letraini:

                case "X":
                
                    numero = int(numero)

                case "Y":
                
                    numero = int(numero) + 10000000

                case "Z":
        
                    numero = int(numero) + 20000000

                case _:     
                    return False
        
        resto = numero % 23
        if (letras[resto] == letrafin):
            return True
        else:
            print("Opción no válida. Repítelo.")
            return False



hoy = datetime.now()                                # Get the current date and time
                            # fecha_actual =   datetime.strptime(str(hoy), "%Y-%m-%d %H:%M") Print the current date and time without seconds

fecha = 0
def fecha_formato(fecha_hora, hoy):
    while True:
        fecha_hora = input("Introducir una fecha y una hora en formato 'año-mes-dia hh:mm': ")
        try:
            fecha_cita = datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M")

            if fecha_cita > hoy: 
                return fecha_cita
            else: 
                print("Opción no válida. Repítelo.")

        except ValueError:
            print("Opción no válida. Repítelo.")



    # conexion1.commit()


def db_a_fichero(cursor, carpeta, fichero):

    cursor1.execute('select c.numero_cita, c.dni_nie, c.fecha_cita, e.especialidad, c.cita_activa \
                    from citas c\
                    join especialidades e on e.id_especialidad = c.id_especialidad_citas; ')   

    with open(carpeta + fichero, mode="w") as mensaje: 

        mensaje.write("numero_cita;dni_nie;fecha_cita;especialidad;cita_activa\n")

        longitud = 0
        ancho = 0
        tabla = list()
        for fila in cursor1:
            # ancho = len(fila)
            tabla.append(fila)
            longitud += 1

        for i in range(longitud):
            linea = ""
            for j in range(ancho):
                linea = linea + str(tabla[i][j]) + ";"
            print(linea)
            mensaje.write(linea + "\n")

    
fichero_citas = db_a_fichero(cursor1, carpeta, fichero)


# 2. Una función que permita añadir una cita a la base de datos. 
    # Se deberá controlar que no existe una cita similar previa posterior a la fecha actual.
 

def fc_cita_nueva(cursor): 
    testigo = False
    while not testigo:   
        
        dni_nie = input("Introduce un valor de dni o NIE: ").upper()
        testigo = fc_dni_nie(dni_nie)

    fecha_cita = fecha_formato(fecha, hoy)
    print("la fecha de la cita es:", fecha_cita)

    serie_especialidades = ["medicina", "enfermeria", "analitica", "vacunacion", "otras gestiones"]
    print(serie_especialidades)
    especialidad = input('Introducir una especialidad: ').lower() 
    while especialidad not in serie_especialidades:
    
        print('Opción no válida')
        especialidad = input('Introducir una especialidad: ').lower()


    

    # usamos insert ignore para que que si existe una cita con el mismo dni, fecha y especialidad, no la inserte.
    cursor.execute("Use prueba_final;")
    cursor.execute("SELECT * FROM citas \
                   WHERE dni_nie = '" + dni_nie + "' \
                   AND fecha_cita = '" + str(fecha_cita) + "' \
                   AND id_especialidad_citas = (SELECT id_especialidad FROM especialidades WHERE especialidad = '" + especialidad + "'\
                    ) AND cita_activa = '1';")

    if cursor.fetchone() is None:                      # si el resultado del cursor es nulo, ejecutamos la inserción de la nueva cita
        cursor.execute("INSERT INTO citas \
                        (dni_nie, fecha_cita, id_especialidad_citas) \
                        SELECT '" + dni_nie + "'\
                        , '" + str(fecha_cita) + "', e.id_especialidad \
                        FROM especialidades e WHERE e.especialidad = '" + especialidad + "';")
        conexion1.commit()
    else:
        print("Ya existe un alinea con estas características.")    # si el cursor arroja 


    
cursor2=conexion1.cursor()
cita_nueva_no_duplicada = fc_cita_nueva(cursor2)


# The INSERT IGNORE statement allows you to insert a new row and ignore execution errors caused by the statement. 
    # This means that if a similar row already exists, the execution of your query won't be interrupted, 
    # and the new row won't be inserted.
        # INSERT IGNORE INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);

    # this works as long as you have defined a unique constraint on the combination of columns that should be unique. 
    # Once the unique constraint is in place, the ON DUPLICATE KEY UPDATE statement should work as intended.
    # ALTER TABLE citas ADD CONSTRAINT unique_citas_constraint UNIQUE (dni_nie, fecha_cita);

#Another way to achieve this is by using the ON DUPLICATE KEY UPDATE clause in the INSERT INTO statement. 
    #This clause allows you to specify what should happen if the new row conflicts with an existing row on a unique key.
        #INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...) 
                # ON DUPLICATE KEY UPDATE column1 = value1, column2 = value2, ...;

# cursor2.executemany(values(?,?), nuevos_datos) nuevos_datos = [(fulanito, 90); (menganito, 80)]
    

# 3. Una función que reciba un dni y devuelva una lista con las citas de ese paciente.


cursor3=conexion1.cursor() 
def fc_lista_citas_paciente(cursor): 

    testigo = False
    while not testigo:   
        
        dni_nie = input("Introduce un valor de dni o NIE: ").upper()
        testigo = fc_dni_nie(dni_nie)

    
    cursor.execute("select * from citas where dni_nie = '" + dni_nie + "';") 
    
    return
lista_citas_paciente = fc_lista_citas_paciente(cursor3)

with open(carpeta + 'fichero_lista_citas_paciente.csv', mode="w") as mensaje: 

    mensaje.write("numero_cita;dni_nie;fecha_cita;especialidad;cita_activa\n")

    longitud = 0
    tabla = list()
    for fila in cursor3:
        ancho = len(fila)
        tabla.append(fila)
        longitud += 1

    for i in range(longitud):
        linea = ""
        for j in range(ancho):
            linea = linea + str(tabla[i][j]) + ";"
        print(linea)
        mensaje.write(linea + "\n")
    
# 4. Una función que reciba un dni y una especialidad y permita modificar la fecha a una fecha posterior a la actual.
        
cursor4=conexion1.cursor() 
nueva_fecha = fecha_formato(fecha, hoy) 

def fc_fecha_modificada(cursor, nueva_fecha): 

    testigo = False
    while not testigo:   
        
        dni_nie = input("Introduce un valor de dni o NIE: ").upper()
        testigo = fc_dni_nie(dni_nie)

    serie_especialidades = ["medicina", "enfermeria", "analitica", "vacunacion", "otras gestiones"]
    print(serie_especialidades)

    especialidad = input('Introducir una especialidad: ').lower() 
    while especialidad not in serie_especialidades:
    
        print('Opción no válida')
        especialidad = input('Introducir una especialidad: ').lower()

    cursor.execute("Use prueba_final;")
    cursor.execute("UPDATE citas c \
                JOIN especialidades e ON c.id_especialidad_citas = e.id_especialidad \
                SET c.fecha_cita = '" + str(nueva_fecha) + "'\
                WHERE c.dni_nie = '" + dni_nie + "' \
                AND e.especialidad = '" + especialidad + "' \
                AND DATE(c.fecha_cita) < '" + str(nueva_fecha.date()) + "';")

    conexion1.commit()

    longitud = 0
    tabla = list()
    for fila in cursor:
        ancho = len(fila)
        tabla.append(fila)
        longitud += 1

    for i in range(longitud):
        linea = ""
        for j in range(ancho):
            linea = linea + str(tabla[i][j]) + ";"
        print(linea)
        

cita_fecha_modificada = fc_fecha_modificada(cursor4, nueva_fecha)



# 5. Una función que reciba un dni y una especialidad y permita anular la cita, siempre y cuando la fecha sea posterior a la actual.

cursor5=conexion1.cursor() 

def fc_cita_anulada(cursor): 

    testigo = False
    while not testigo:   
        
        dni_nie = input("Introduce un valor de dni o NIE: ").upper()
        testigo = fc_dni_nie(dni_nie)

    serie_especialidades = ["medicina", "enfermeria", "analitica", "vacunacion", "otras gestiones"]
    print(serie_especialidades)

    especialidad = input('Introducir una especialidad: ').lower() 
    while especialidad not in serie_especialidades:
    
        print('Opción no válida')
        especialidad = input('Introducir una especialidad: ').lower()

    cursor.execute("Use prueba_final;")
    cursor.execute("UPDATE citas c \
                JOIN especialidades e ON c.id_especialidad_citas = e.id_especialidad  \
                SET c.cita_activa = 0 \
                WHERE c.dni_nie = '" + dni_nie + "' \
                AND e.especialidad = '" + especialidad + "' ;")

    conexion1.commit()

    longitud = 0
    tabla = list()
    for fila in cursor:
        ancho = len(fila)
        tabla.append(fila)
        longitud += 1

    for i in range(longitud):
        linea = ""
        for j in range(ancho):
            linea = linea + str(tabla[i][j]) + ";"
        print(linea)
        

cita_anulada = fc_cita_anulada(cursor5)

conexion1.close()

