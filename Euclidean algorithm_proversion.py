# Author: Juan Manuel Hernández Solano
# Date: 02/21

#Inicializo las variables que utilizaré en el programa
lista = [ ]
num1 = 0
num2 = 0
a = 1
b = 1

#Crearé una nueva lista para tener registro de los números que se usaron en el proceso: números introducidos y los residuos
residuos = [ ] 

#Aquí organizo los números en una lista para tener un registro e imprimirlo al final del programa 
num1 = int(input("\nIntroduzca el primer número "))
num2 = int(input("Introduzca el segundo número "))
lista.append(num1)
lista.append(num2)
lista.sort(reverse = True)

#Se añaden los números introducidos al registro
residuos.append(num1) 
residuos.append(num2) 

#Se deberán iniciar variables para saber cuál fue la variable con el resultado para fines de la solucion de ax + by = c
uno = 0
dos = 0 
aa = 0
original1 = num1
original2 = num2

#Comienza el ciclo utilizando el algoritmo de Euclides para obtener el gcd
""" En el algoritmo de Euclides se utiliza la operación mod sobre el mod del número más pequeño, es por esta razón que 
hay una condicional para acomodar esos números """

if num1 > num2:

    while a or b != 0:
        a = num1 % num2
        residuos.append(a) #Residuos
        if a == 0:
            print(f"\nEL máximo común divisor (gcd) de los números {lista} es {num2}")
            if num2 == 1:
                print(f"Los números {lista} son coprimos")
            break
        b= num2 % a
        residuos.append(num2)
        residuos.append(b) #Residuos
        if b == 0:
            print(f"\nEL máximo común divisor (gcd) de los números {lista} es {a}")
            if a == 1:
                print(f"Los números {lista} son coprimos")
            break
        num1 = a
        num2 = b
        residuos.append(num1)
        residuos.append(num2)

#Hay una segunda condicional que se activara si los números introducidos son los mismos

elif num1 == num2:
    print(f"\nEl máximo común divisor (gcd) de los números {lista} es {num1} ")

else:

    while a or b != 0:
        a = num2 % num1
        residuos.append(a) #Residuos
        if a == 0:
            print(f"\nEL máximo común divisor (gcd) de los números {lista} es {num1}")
            if num1 == 1:
                print(f"Los números {lista} son coprimos")
            break
        b = num1 % a
        residuos.append(num1)
        residuos.append(b) #Residuos
        if b == 0:
            print(f"\nEL máximo común divisor (gcd) de los números {lista} es {a}")
            if a == 1:
                print(f"Los números {lista} son coprimos")
            break
        num1 = b
        num2 = a
        residuos.append(num1)
        residuos.append(num2) 

print(f"El registro de los números introducidos y los residuos fueron {residuos} ")

#Empieza el código para encontrar la solución ax + by = c
ecuacion = input(f"""\n
Desea encontrar las soluciones a ax + by = c\nSi su respuesta es sí escriba S/s\nSi su respuesta es no escriba N/n """)

if ecuacion == "S" or "s":
    numero1 = 0
    numero2 = 0

    for evidencia in residuos:
        if num1 == evidencia:
            numero1 += 1
        elif num2 == evidencia:
            numero2 += 1

        solucion1 = (num1*numero1)+(num2*numero2)
        solucion2 = (num1*numero1)-(num2*numero2)
        solucion3 = -(num1*numero1)+(num2*numero2)

        if uno == 1:
            if solucion1 == num1:
                print(f"La solución es {original1}*{numero1} + {original2}*{numero2} = a {num1} por lo que x = {numero1} y = {numero2} ")
            elif solucion2 == num1:
                print(f"La solución es {original1}*{numero1} + {original2}*-{numero2} = a {num1} por lo que x = {numero1} y = -{numero2} ")
            elif solucion3 == num1:
                print(f"La solución es {original1}*-{numero1} + {original2}*-{numero2} = a {num1} por lo que x = -{numero1} y = {numero2} ")

        if dos == 1:
            if solucion1 == num2:
                print(f"La solución es {original1}*{numero1} + {original2}*{numero2} = a {num2} por lo que x = {numero1} y = {numero2} ")
            elif solucion2 == num1:
                print(f"La solución es {original1}*{numero1} + {original2}*-{numero2} = a {num2} por lo que x = {numero1} y = -{numero2} ")
            elif solucion3 == num1:
                print(f"La solución es {original1}*-{numero1} + {original2}*-{numero2} = a {num2} por lo que x = -{numero1} y = {numero2} ")

        if aa == 1:
            if solucion1 == num1:
                print(f"La solución es {original1}*{numero1} + {original2}*{numero2} = a {num1} por lo que x = {numero1} y = {numero2} ")
            elif solucion2 == num1:
                print(f"La solución es {original1}*{numero1} + {original2}*-{numero2} = a {num1} por lo que x = {numero1} y = -{numero2} ")
            elif solucion3 == num1:
                print(f"La solución es {original1}*-{numero1} + {original2}*-{numero2} = a {num1} por lo que x = -{numero1} y = {numero2} ")
elif ecuacion == "N" or "n":
    print(f"\nFin del programa ")

else:
    print(f"\nIngrese una respuesta válida ")

print(solucion1)
print(solucion2)
print(solucion3)
