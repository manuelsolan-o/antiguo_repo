# author: Juan Manuel Hernández Solano A00572208
# Date: 02 / 2021

#Inicializo las variables que utilizaré en el programa
lista = [ ]
num1 = 0
num2 = 0
a = 0
b = 1


#Aquí organizo los números en una lista para tener un registro e imprimirlo al final del programa 
num1 = int(input("Introduzca el primer número "))
num2 = int(input("Introduzca el segundo número "))
lista.append(num1)
lista.append(num2)
lista.sort(reverse = True)

#Comienza el ciclo utilizando el algoritmo de Euclides para obtener el gcd
if num1 > num2:
    while b != 0:

        a = num1 % num2
        if a == 0:
            print(f"\n El máximo común divisor de los números {lista} es {num1} ")
            break
        else:
            if num2 % a == 0:
                print(f"\n El máximo común divisor de los números {lista} es {a} ")
                a = 0
            else:
                b = num2 % a
                num1 = a
                num2 = b
                print(f"\n El máximo común divisor de los números {lista} es {num2} ")
