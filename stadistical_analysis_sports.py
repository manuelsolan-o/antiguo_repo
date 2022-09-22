# Author: Juan Manuel Hernández Solano 
# Date: 09 / 21

# Importamos librerías
import pandas as pd 
import matplotlib.pyplot as plt
import statistics as stat

# Inicializando variables
password = 'none'
re_password = ''
volver = 0

# Validación de contraseña
password = input('Para ingresar debe crear una contraseña ')
while password != re_password:
    re_password = input('Confirme la contraseña ')
    if password != re_password:
        print('Contraseña incorrecta, intentelo de nuevo')

# Comienza el ciclo principal
while volver != 2:
    print("""
    -----------------------------------------------------------------------
    |                                                                     |
    |                       Bienvenido usuario                            |
    |  En nuestro programa hemos ánalizado estadísticas de deportistas en |
    |                     artes marciales mixtas                          |
    |                                                                     |
    |---------------------------------------------------------------------|

    1. ¿Quién tiene más victorias?
    2. ¿Quién tiene más efectividad de golpeo?
    3. ¿Quién tiene más efectividad de grappling?
    """)
    programa = input("[+] ¿Qué programa desea usar? (Ingrese el número): ")
    
    tabla = pd.read_excel("Problematica de Programación_corregido.xlsx")

    if programa == '1':
        def victoria():
            tabla_uno = tabla.groupby(['Nombre'])['Victorias'].sum().reset_index()[:15] #creo q el pedo es con la otra tabla uno
            tabla_uno = tabla_uno.sort_values('Victorias', ascending = False)

            #Convertir columnas a lista
            nombre = tabla_uno['Nombre'].tolist()
            victorias = tabla_uno['Victorias'].tolist()

            plt.xlabel("Nombres")
            plt.ylabel("Victorias")
            plt.title("1. ¿Quién tiene más victorias?")
            plt.bar(nombre,victorias)
            plt.xticks(rotation = 45)
            plt.show()

            # Descriptores estadísticos
            tabla_uno = tabla.groupby(['Nombre'])['Victorias'].sum().reset_index()

            suma_victoria = sum(tabla_uno['Victorias'].tolist())
            media_victoria = sum(tabla_uno['Victorias'].tolist())/ len(tabla_uno)
            moda_victoria = stat.mode(tabla_uno['Victorias'].tolist())
            rango_victoria = max(tabla_uno['Victorias'].tolist()) - min(tabla_uno['Victorias'].tolist())

            print('Descriptores estadísticos: Victorias')
            print(f'La suma es de: {suma_victoria}')
            print(f'La media es de: {media_victoria}')
            print(f'La moda es de: {moda_victoria}')
            print(f'El rango es de: {rango_victoria}')
        victoria()
    elif programa == '2':
        def golpeo():
            tabla_dos = tabla.groupby(['Nombre'])['Efectividad de golpeo'].sum().reset_index()[:15]
            tabla_dos = tabla_dos.sort_values('Efectividad de golpeo', ascending = False)

            #Convertir columnas a lista
            nombre = tabla_dos['Nombre'].tolist()
            golpeo = tabla_dos['Efectividad de golpeo'].tolist()

            plt.xlabel("Nombres")
            plt.ylabel("Efectividad de golpeo")
            plt.title("2. ¿Quién tiene más efectividad de golpeo?")
            plt.bar(nombre,golpeo)
            plt.xticks(rotation = 45)
            plt.show()

            # Descriptores estadísticos
            tabla_dos = tabla.groupby(['Nombre'])['Efectividad de golpeo'].sum().reset_index()

            suma_golpeo = sum(tabla_dos['Efectividad de golpeo'].tolist())
            media_golpeo = sum(tabla_dos['Efectividad de golpeo'].tolist())/ len(tabla_dos)
            moda_golpeo = stat.mode(tabla_dos['Efectividad de golpeo'].tolist())
            dev_golpeo = stat.stdev(tabla_dos['Efectividad de golpeo'].tolist())

            print('Descriptores estadísticos: Efectividad de golpeo')
            print(f'La suma es de: {suma_golpeo}')
            print(f'La media es de: {media_golpeo}')
            print(f'La moda es de: {moda_golpeo}')
            print(f'La desviación estándar es de: {dev_golpeo}')
        golpeo()
    elif programa == '3':
        def grappling():
            tabla_tres = tabla.groupby(['Nombre'])['Efectividad de grappling'].sum().reset_index()[:15]
            tabla_tres = tabla_tres.sort_values('Efectividad de grappling', ascending = False)

            #Convertir columnas a lista
            nombre = tabla_tres['Nombre'].tolist()
            grappling = tabla_tres['Efectividad de grappling'].tolist()

            plt.xlabel("Nombres")
            plt.ylabel("Efectividad de grappling")
            plt.title("3. ¿Quién tiene más efectividad de grappling?")
            plt.bar(nombre,grappling)
            plt.xticks(rotation = 45)
            plt.show()

            # Descriptores estadísticos
            tabla_tres = tabla.groupby(['Nombre'])['Efectividad de grappling'].sum().reset_index()

            suma_grappling = sum(tabla_tres['Efectividad de grappling'].tolist())
            media_grappling = sum(tabla_tres['Efectividad de grappling'].tolist())/ len(tabla_tres)
            moda_grappling = stat.mode(tabla_tres['Efectividad de grappling'].tolist())
            mediana_grappling = stat.median(tabla_tres['Efectividad de grappling'].tolist())

            print('Descriptores estadísticos: Grappling')
            print(f'La suma es de: {suma_grappling}')
            print(f'La media es de: {media_grappling}')
            print(f'La moda es de: {moda_grappling}')
            print(f'La mediana es de: {mediana_grappling}')
        grappling()
    volver = int(input('Desea hacer otro programa\n1. Sí\n2.No\nIngrese el número '))
