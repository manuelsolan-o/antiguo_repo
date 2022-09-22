# Author: Juan Manuel Hernández Solano 
# Date: 11/2020

# Actividad decodificar mensaje

import pandas as pd

e=115 #Nuestra clave privada
n=1003

mensaje1 = 264
a1=(mensaje1**e)%n
c1=a1/27
d1=int(c1)
f1=a1-(d1*27)
 
mensaje2 = 702
a2=(mensaje2**e)%n
c2=a2/27
d2=int(c2)
f2=a2-(d2*27)

mensaje3 = 224
a3=(mensaje3**e)%n
c3=a3/27
d3=int(c3)
f3=a3-(d3*27)

mensaje4 = 329
a4=(mensaje4**e)%n
c4=a4/27
d4=int(c4)
f4=a4-(d4*27)

mensaje5 = 951
a5=(mensaje5**e)%n
c5=a5/27
d5=int(c5)
f5=a5-(d5*27)

datos={"Coeficiente": [d1,d2,d3,d4,d5], "Residuo": [f1,f2,f3,f4,f5]}
tabla = pd.DataFrame(datos)
print(tabla)

#Por los resultados obtenidos en este programa, se concluye que el mensaje es: RED_HORSE_
