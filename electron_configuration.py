# Author: Juan Manuel Hernández Solano 
# Date: 08/21

""" 
La configuración electrónica del último elemento es:
1s²/2s²2p⁶/3s²3p⁶/4s²3d¹⁰4p⁶/5s²4d¹⁰5p⁶/6s²4f¹⁴5d¹⁰6p⁶/7s²5f¹⁴6d¹⁰7p⁶
2 10 18 36 56 88 120

Si el último nivel de energía es:
s,p:está en el grupo A
d,f:está en el grupo B
y el número de grupo está determinado por sus electrones de valencia

Su peridiodo es el último nivel
"""

numerales = ['¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹','¹⁰']
num = int(input('[+] Ingrese el número atómico (Z) '))

def configuracion(num):
    print(f'\nLa configuración electrónica del número atómico {num} es: ')
    subnivel = 0
    if num <= 2: # Nivel 1
        print(f'1s{numerales[num-1]} ') #1s
        print(f'\nEste elemento se encuentra en el Grupo {num}A y en el Periodo 1')

    elif num > 2 and num <= 10: # Nivel 2
        if num - 2 <= 2:
            subnivel = num - 2 #2s
            print(f'1s²/2s{numerales[subnivel-1]}')
            print(f'\nEste elemento se encuentra en el Grupo {subnivel}A y en el Periodo 2')
        else:
            subnivel = num - 4 #2p
            print(f'1s²/2s²2p{numerales[subnivel-1]}')
            print(f'\nEste elemento se encuentra en el Grupo {subnivel+2}A y en el Periodo 2')

    elif num > 10 and num <= 18: # Nivel 3
        if num - 10 <= 2:
            subnivel = num - 10 #3s
            print(f'1s²/2s²2p⁶/3s{numerales[subnivel-1]}')
            print(f'\nEste elemento se encuentra en el Grupo {subnivel}A y en el Periodo 3')
        else:
            subnivel = num - 12 #3p
            print(f'1s²/2s²2p⁶/3s²3p{numerales[subnivel-1]}')
            print(f'\nEste elemento se encuentra en el Grupo {subnivel+2}A y en el Periodo 3')

    elif num > 18 and num <= 36: # Nivel 4
        if num - 18 <= 2:
            subnivel = num - 18 #4s
            print(f'1s²/2s²2p⁶/3s²3p⁶/4s{numerales[subnivel-1]}')
            print(f'\nEste elemento se encuentra en el Grupo {subnivel}A y en el Periodo 4')
        elif num - 18 > 2 and num <= 30 :
            subnivel = num - 20 #3d
            print(f'1s²/2s²2p⁶/3s²3p⁶/4s²3d{numerales[subnivel-1]}')
            print(f'\nEste elemento se encuentra en el Grupo {subnivel}B y en el Periodo 4')
        else:
            subnivel = num - 30 #4p
            print(f'1s²/2s²2p⁶/3s²3p⁶/4s²3d¹⁰4p{numerales[subnivel-1]}')
            print(f'\nEste elemento se encuentra en el Grupo {subnivel+2}A y en el Periodo 4')

    elif num > 36 and num <= 56: # Nivel 5
        if num - 36 <= 2:
            subnivel = num - 36 #5s
            print(f'1s²/2s²2p⁶/3s²3p⁶/4s²3d¹⁰4p⁶/5s{numerales[subnivel-1]}') 
            print(f'\nEste elemento se encuentra en el Grupo {subnivel}A y en el Periodo 5')
        elif num - 36 > 2 and num <= 50 :
            subnivel = num - 38 #4d
            print(f'1s²/2s²2p⁶/3s²3p⁶/4s²3d¹⁰4p⁶/5s²4d{numerales[subnivel-1]}')
            print(f'\nEste elemento se encuentra en el Grupo {subnivel+2}B y en el Periodo 5')
        else:
            subnivel = num - 50 #5p
            print(f'1s²/2s²2p⁶/3s²3p⁶/4s²3d¹⁰4p⁶/5s²4d¹⁰5p{numerales[subnivel-1]}')
            print(f'\nEste elemento se encuentra en el Grupo {subnivel+2}A y en el Periodo 5')

    elif num > 56 and num <= 88: # Nivel 6
        if num - 56 <= 2:
            subnivel = num - 56 #6s
            print(f'1s²/2s²2p⁶/3s²3p⁶/4s²3d¹⁰4p⁶/5s²4d¹⁰5p⁶/6s{numerales[subnivel-1]}')
            print(f'\nEste elemento se encuentra en el Grupo {subnivel}A y en el Periodo 6')
        elif num - 56 > 2 and num <= 72 :
            subnivel = num - 58 #4f
            print(f'1s²/2s²2p⁶/3s²3p⁶/4s²3d¹⁰4p⁶/5s²4d¹⁰5p⁶/6s²4f{numerales[subnivel-1]}')
            print(f'\nEste elemento se encuentra en el Grupo {subnivel}B y en el Periodo 6')  
        elif num > 72 and num <= 82 :
            subnivel = num - 68 #5d
            print(f'1s²/2s²2p⁶/3s²3p⁶/4s²3d¹⁰4p⁶/5s²4d¹⁰5p⁶/6s²4f¹⁴5d{numerales[subnivel-1]}')
            print(f'\nEste elemento se encuentra en el Grupo {subnivel+2}B y en el Periodo 6')
        else:
            subnivel = num - 82 #6p
            print(f'1s²/2s²2p⁶/3s²3p⁶/4s²3d¹⁰4p⁶/5s²4d¹⁰5p⁶/6s²4f¹⁴5d¹⁰6p{numerales[subnivel-1]}')
            print(f'\nEste elemento se encuentra en el Grupo {subnivel+2}A y en el Periodo 6')

    elif num > 88 and num <= 120: # Nivel 7
        if num - 88 <= 2:
            subnivel = num - 88 #7s
            print(f'1s²/2s²2p⁶/3s²3p⁶/4s²3d¹⁰4p⁶/5s²4d¹⁰5p⁶/6s²4f¹⁴5d¹⁰6p⁶/7s{numerales[subnivel-1]}')
            print(f'\nEste elemento se encuentra en el Grupo {subnivel}A y en el Periodo 7')
        elif num - 88 > 2 and num <= 104 :
            subnivel = num - 90 #5f
            print(f'1s²/2s²2p⁶/3s²3p⁶/4s²3d¹⁰4p⁶/5s²4d¹⁰5p⁶/6s²4f¹⁴5d¹⁰6p⁶/7s²5f{numerales[subnivel-1]}')
            print(f'\nEste elemento se encuentra en el Grupo {subnivel}A y en el Periodo 7')  
        elif num > 104 and num <= 114 :
            subnivel = num - 100 #6d
            print(f'1s²/2s²2p⁶/3s²3p⁶/4s²3d¹⁰4p⁶/5s²4d¹⁰5p⁶/6s²4f¹⁴5d¹⁰6p⁶/7s²5f¹⁴6d{numerales[subnivel-1]}')
            print(f'\nEste elemento se encuentra en el Grupo {subnivel}A y en el Periodo 7')
        else:
            subnivel = num - 114 #7p
            print(f'1s²/2s²2p⁶/3s²3p⁶/4s²3d¹⁰4p⁶/5s²4d¹⁰5p⁶/6s²4f¹⁴5d¹⁰6p⁶/7s²5f¹⁴6d¹⁰7p{numerales[subnivel-1]}')
            print(f'\nEste elemento se encuentra en el Grupo {subnivel+2}A y en el Periodo 7')
    else:
        print('Aún no hemos descubierto un elemento con ese número atómico, pero tal vez algún día :) ')      
    return 
configuracion(num)
