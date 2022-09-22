# Autor : Juan Manuel Hernández Solano 
# Date: 10/20

nombre = input('Ingresa el nombre del alimento para calcular calorías: ')
carbohidratos = float(input('Ingresa la cantidad de carbohidratos en gramos: '))
lipidos = float(input('Ingresa la cantidad de lipidos en gramos: '))
proteinas = float(input('Ingresa la cantidad de proteínas en gramos: '))
calorias = (carbohidratos * 4) + (lipidos * 9) + (proteinas * 4) 

print(f'Las calorías proporcionadas por el alimento son: {calorias}')
