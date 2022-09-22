# Autor : Juan Manuel Hernández Solano 
# Date: 10/20

# Variables
nombre = input('[+] Ingrese su nombre completo ')
peso = float(input('[+] Ingrese su peso en kg '))
altura = float(input('[+] Ingrese tu altura en m '))

print(f'¡Hola, {nombre}!')

print(f'Tu peso registrado es de: {peso} kgs ')

print(f'Tu estatura registrada es de: {altura} mts ')

# Variables
imc = round(peso / altura**2,2)
forma = ''

if imc < 18.4:
    forma = 'Peso bajo'
elif imc > 18.4 and imc < 24.9:
    forma = 'Peso normal'
elif imc > 24.9 and imc < 29.9:
    forma = 'Sobrepeso' 
else:
    forma = 'Obesidad'       
print(f'De acuerdo con estos datos tú IMC es de {imc} lo que indica: {forma} ')
