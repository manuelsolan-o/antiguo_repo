# Author: Juan Manuel Hernández Solano
# Date: 03/2021

mensaje = input("Introduce el mensaje ")
privada = input("Introduzca la clave privada (debe ser una letra del alfabeto) ")
cpriv = privada.upper()
clave = ord(cpriv)
mayus = mensaje.upper()
cifrado = 0
analisis = " "
palabras = [ ]
suma = 0
cifra = (clave % 26) #Es mod26 porque hay 25 caractéres; En este programa se tomarán las letras mayúsculas del código ASIIC, las cuales empiezan en 65 y terminan en 90

for letras in (mayus): 
  suma = (ord(letras) + cifra) 
  if suma > 90:
    cifra = suma % 90
    cifrado = cifra + 65
  else:
    cifrado = (ord(letras) + cifra) 
  palabras.append(cifrado)
  palabras = [i for i in palabras if i != (32 + cifra)] #Se usa este ciclo para eliminar los espacios

print("El mensaje cifrado es: ")
for valor in palabras:
  analisis = chr(valor) 
  print(analisis, end = "")
