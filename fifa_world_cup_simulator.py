# Autor: Juan Manuel Hernández Solano 
# Date: It is not finished yet but soon

# FIFA WORLD CUP SIMULATOR

import random 

clasificados = [ 
grupoA = [
'QATAR 🇶🇦',
'ECUADOR 🇪🇨',
'SENEGAL 🇸🇳',
'PAÍSES BAJOS 🇳🇱'
],

grupoB = [
'INGLATERRA 🏴󠁧󠁢󠁥󠁮󠁧󠁿',
'IRAN 🇮🇷',
'ESTADOS UNIDOS 🇺🇲',
'GALES 🏴󠁧󠁢󠁷󠁬󠁳󠁿' 
],

grupoC = [
'ARGENTINA 🇦🇷',
'ARABIA SAUDITA 🇸🇦',
'MÉXICO 🇲🇽',
'POLONIA 🇵🇱'
],

grupoD = [
'FRANCIA 🇫🇷',
'AUSTRALIA 🇦🇺',
'DINAMARCA 🇩🇰',
'TÚNEZ 🇹🇳'
],

grupoE = [
'ESPAÑA 🇪🇦',
'COSTA RICA 🇨🇷',
'ALEMANIA 🇩🇪',
'JAPÓN 🇯🇵'
],

grupoF = [
'BÉLGICA 🇧🇪',
'CANADÁ 🇨🇦',
'MARRUECOS 🇲🇦',
'CROACIA 🇭🇷'
],

grupoG = [
'BRASIL 🇧🇷',
'SERBIA 🇷🇸',
'SUIZA 🇨🇭',
'CAMERÚN 🇨🇲'
],

grupoH = [
'PORTUGAL 🇵🇹',
'GHANA 🇬🇭',
'URUGUAY 🇺🇾',
'COREA DEL SUR 🇰🇷'
]
  
goles = list(range(1,6))

"""
////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                GRUPO A
///////////////////////////////////////////////////////////////////////////////////////////////////////

"""

grupoA = [
'QATAR 🇶🇦',
'ECUADOR 🇪🇨',
'SENEGAL 🇸🇳',
'PAÍSES BAJOS 🇳🇱'
]
puntosQatar = 0
golesQatar = 0

puntosEcuador = 0
golesEcuador = 0

puntosSenegal = 0
golesSenegal = 0

puntosPBajos = 0 
golesPBajos = 0

print('FASE DE GRUPOS GRUPO A\n')

for g in range(1,4):

    if grupoA[g] == 'ECUADOR 🇪🇨':
        golesQatar = random.choice(goles)
        golesEcuador = random.choice(goles)

        print(f'{grupoA[0]} {golesQatar} vs {grupoA[g]} {golesEcuador}')

        if golesQatar > golesEcuador:
            puntosQatar += 3
            print('\nGANA QATAR 🇶🇦\n')

        elif golesEcuador > golesQatar:
            puntosEcuador += 3
            print('\nGANA ECUADOR 🇪🇨\n')

        else:
            puntosQatar += 1
            puntosEcuador += 1
            print('\nEMPATE\n')


    elif grupoA[g] == 'SENEGAL 🇸🇳':
        golesQatar = random.choice(goles)
        golesSenegal = random.choice(goles)

        print(f'{grupoA[0]} {golesQatar} vs {grupoA[g]} {golesSenegal}')

        if golesQatar > golesSenegal:
            puntosQatar += 3
            print('\nGANA QATAR 🇶🇦\n')

        elif golesSenegal > golesQatar:
            puntosSenegal += 3
            print('\nGANA SENEGAL 🇸🇳\n')

        else:
            puntosQatar += 1
            puntosSenegal += 1
            print('\nEMPATE\n')

    elif grupoA[g] == 'PAÍSES BAJOS 🇳🇱':
        golesQatar = random.choice(goles)
        golesPBajos = random.choice(goles)

        print(f'{grupoA[0]} {golesQatar} vs {grupoA[g]} {golesPBajos}')

        if golesQatar > golesPBajos:
            puntosQatar += 3
            print('\nGANA QATAR 🇶🇦\n')

        elif golesPBajos > golesQatar:
            puntosPBajos += 3
            print('\nGANA PAÍSES BAJOS 🇳🇱\n')

        else:
            puntosQatar += 1
            puntosPBajos += 1
            print('\nEMPATE\n')

for g in range(2,4):

    if grupoA[g] == 'SENEGAL 🇸🇳':
        golesEcuador = random.choice(goles)
        golesSenegal = random.choice(goles)

        print(f'{grupoA[1]} {golesEcuador} vs {grupoA[g]} {golesSenegal}')

        if golesEcuador > golesSenegal:
            puntosEcuador += 3
            print('\nGANA ECUADOR 🇪🇨\n')

        elif golesSenegal > golesEcuador:
            puntosSenegal += 3
            print('\nGANA SENEGAL 🇸🇳\n')

        else:
            puntosEcuador += 1
            puntosSenegal += 1
            print('\nEMPATE\n')

    elif grupoA[g] == 'PAÍSES BAJOS 🇳🇱':
        golesEcuador = random.choice(goles)
        golesPBajos = random.choice(goles)

        print(f'{grupoA[1]} {golesEcuador} vs {grupoA[g]} {golesPBajos}')

        if golesEcuador > golesPBajos:
            puntosEcuador += 3
            print('\nGANA ECUADOR 🇪🇨\n')

        elif golesPBajos > golesEcuador:
            puntosPBajos += 3
            print('\nGANA PAÍSES BAJOS 🇳🇱\n')

        else:
            puntosEcuador += 1
            puntosPBajos += 1
            print('\nEMPATE\n')


for g in range(3,4):

    if grupoA[g] == 'PAÍSES BAJOS 🇳🇱':
        golesSenagal = random.choice(goles)
        golesPBajos = random.choice(goles)

        print(f'{grupoA[2]} {golesSenagal} vs {grupoA[g]} {golesPBajos}')

        if golesSenagal > golesPBajos:
            puntosSenegal += 3
            print('\nGANA SENEGAL 🇸🇳\n')

        elif golesPBajos > golesSenagal:
            puntosPBajos += 3
            print('\nGANA PAÍSES BAJOS 🇳🇱\n')

        else:
            puntosSenegal += 1
            puntosPBajos += 1
            print('\nEMPATE\n')

puntos_grupoA = {
'QATAR 🇶🇦':puntosQatar,
'ECUADOR 🇪🇨':puntosEcuador,
'SENEGAL 🇸🇳':puntosSenegal,
'PAÍSES BAJOS 🇳🇱':puntosPBajos}

sort_grupoA = sorted(puntos_grupoA.items(), key=lambda x: x[1], reverse=True)

pasa_GrupoA = [] 
print(f'\nTABLA GRUPO A\n')
for k,v in sort_grupoA:
    print(f'{k} : {v}   PUNTOS ')
    pasa_GrupoA.append(k)

print(f'\nAVANZAN {pasa_GrupoA[0]} Y {pasa_GrupoA[1]}\n')  
  
grupoB = [
'INGLATERRA 🏴󠁧󠁢󠁥󠁮󠁧󠁿',
'IRAN 🇮🇷',
'ESTADOS UNIDOS 🇺🇲',
'GALES 🏴󠁧󠁢󠁷󠁬󠁳󠁿' 
]
puntosInglaterra = 0
golesInglaterra = 0

puntosIran = 0
golesIran = 0

puntosEU = 0
golesEU = 0

puntosGales = 0 
golesGales = 0

goles = list(range(1,6))

print('FASE DE GRUPOS GRUPO B\n')

for g in range(1,4):

    if grupoB[g] == 'IRAN 🇮🇷':
        golesInglaterra = random.choice(goles)
        golesIran = random.choice(goles)

        print(f'{grupoB[0]} {golesInglaterra} vs {grupoB[g]} {golesIran}')

        if golesInglaterra > golesIran:
            puntosInglaterra += 3
            print('\nGANA INGLATERRA 🏴󠁧󠁢󠁥󠁮󠁧󠁿\n')

        elif golesIran > golesInglaterra:
            puntosIran += 3
            print('\nGANA IRAN 🇮🇷\n')

        else:
            puntosInglaterra += 1
            puntosIran += 1
            print('\nEMPATE\n')


    elif grupoB[g] == 'ESTADOS UNIDOS 🇺🇲':
        golesInglaterra = random.choice(goles)
        golesEU = random.choice(goles)

        print(f'{grupoB[0]} {golesInglaterra} vs {grupoB[g]} {golesEU}')

        if golesInglaterra > golesEU:
            puntosInglaterra += 3
            print('\nGANA INGLATERRA 🏴󠁧󠁢󠁥󠁮󠁧󠁿\n')

        elif golesEU > golesInglaterra:
            puntosEU += 3
            print('\nGANA ESTADOS UNIDOS 🇺🇲\n')

        else:
            puntosInglaterra += 1
            puntosEU += 1
            print('\nEMPATE\n')

    elif grupoB[g] == 'GALES 🏴󠁧󠁢󠁷󠁬󠁳󠁿':
        golesInglaterra = random.choice(goles)
        golesEU = random.choice(goles)

        print(f'{grupoB[0]} {golesInglaterra} vs {grupoB[g]} {golesGales}')

        if golesInglaterra > golesGales:
            puntosInglaterra += 3
            print('\nGANA INGLATERRA 🏴󠁧󠁢󠁥󠁮󠁧󠁿\n')

        elif golesGales > golesInglaterra:
            puntosGales += 3
            print('\nGANA GALES 🏴󠁧󠁢󠁷󠁬󠁳󠁿\n')

        else:
            puntosInglaterra += 1
            puntosEU += 1
            print('\nEMPATE\n')

for g in range(2,4):

    if grupoB[g] == 'ESTADOS UNIDOS 🇺🇲':
        golesIran = random.choice(goles)
        golesEU = random.choice(goles)

        print(f'{grupoB[1]} {golesIran} vs {grupoB[g]} {golesEU}')

        if golesIran > golesEU:
            puntosIran += 3
            print('\nGANA IRAN 🇮🇷\n')

        elif golesEU > golesIran:
            puntosEU += 3
            print('\nGANA ESTADOS UNIDOS 🇺🇲\n')

        else:
            puntosIran += 1
            puntosEU += 1
            print('\nEMPATE\n')

    elif grupoB[g] == 'GALES 🏴󠁧󠁢󠁷󠁬󠁳󠁿':
        golesIran = random.choice(goles)
        golesGales = random.choice(goles)

        print(f'{grupoB[1]} {golesIran} vs {grupoB[g]} {golesGales}')

        if golesIran > golesGales:
            puntosIran += 3
            print('\nGANA IRAN 🇮🇷\n')

        elif golesIran > golesGales:
            puntosGales += 3
            print('\nGANA GALES 🏴󠁧󠁢󠁷󠁬󠁳󠁿\n')

        else:
            puntosIran += 1
            puntosGales += 1
            print('\nEMPATE\n')


for g in range(3,4):

    if grupoB[g] == 'GALES 🏴󠁧󠁢󠁷󠁬󠁳󠁿':
        golesEU = random.choice(goles)
        golesGales = random.choice(goles)

        print(f'{grupoB[2]} {golesEU} vs {grupoB[g]} {golesGales}')

        if golesEU > golesGales:
            puntosEU += 3
            print('\nGANA ESTADOS UNIDOS 🇺🇲\n')

        elif golesGales > golesEU:
            puntosGales += 3
            print('\nGANA GALES 🏴󠁧󠁢󠁷󠁬󠁳󠁿\n')

        else:
            puntosEU += 1
            puntosGales += 1
            print('\nEMPATE\n')

puntos_grupoB = {
'INGLATERRA 🏴󠁧󠁢󠁥󠁮󠁧󠁿':puntosInglaterra,
'IRAN 🇮🇷': puntosIran,
'ESTADOS UNIDOS 🇺🇲': puntosEU,
'GALES 🏴󠁧󠁢󠁷󠁬󠁳󠁿':puntosGales }

sort_grupoB = sorted(puntos_grupoB.items(), key=lambda x: x[1], reverse=True)

pasa_GrupoB = [] 
print(f'\nTABLA GRUPO B\n')
for k,v in sort_grupoB:
    print(f'{k} : {v}   PUNTOS ')
    pasa_GrupoB.append(k)

print(f'\nAVANZAN {pasa_GrupoB[0]} Y {pasa_GrupoB[1]}\n')
  
grupoC = [
'ARGENTINA 🇦🇷',
'ARABIA SAUDITA 🇸🇦',
'MÉXICO 🇲🇽',
'POLONIA 🇵🇱'
]
puntosArgentina = 0
golesArgentina = 0

puntosArabia = 0
golesArabia = 0

puntosMex = 0
golesMex = 0

puntosPolonia = 0 
golesPolonia = 0

goles = list(range(1,6))

print('FASE DE GRUPOS GRUPO C\n')

for g in range(1,4):

    if grupoC[g] == 'ARABIA SAUDITA 🇸🇦':
        golesArgentina = random.choice(goles)
        golesArabia = random.choice(goles)

        print(f'{grupoC[0]} {golesArgentina} vs {grupoC[g]} {golesArabia}')

        if golesArgentina > golesArabia:
            puntosArgentina += 3
            print('\nGANA ARGENTINA 🇦🇷\n')

        elif golesArabia > golesArgentina:
            puntosArabia += 3
            print('\nGANA ARABIA SAUDITA 🇸🇦\n')

        else:
            puntosArgentina += 1
            puntosArabia += 1
            print('\nEMPATE\n')


    elif grupoC[g] == 'MÉXICO 🇲🇽':
        golesArgentina = random.choice(goles)
        golesMex = random.choice(goles)

        print(f'{grupoC[0]} {golesArgentina} vs {grupoC[g]} {golesMex}')

        if golesArgentina > golesMex:
            puntosArgentina += 3
            print('\nGANA ARGENTINA 🇦🇷\n')

        elif golesMex > golesArgentina:
            puntosMex += 3
            print('\nGANA MÉXICO 🇲🇽\n')

        else:
            puntosArgentina += 1
            puntosMex += 1
            print('\nEMPATE\n')

    elif grupoC[g] == 'POLONIA 🇵🇱':
        golesArgentina = random.choice(goles)
        golesPolonia = random.choice(goles)

        print(f'{grupoC[0]} {golesArgentina} vs {grupoC[g]} {golesPolonia}')

        if golesArgentina > golesPolonia:
            puntosArgentina += 3
            print('\nGANA ARGENTINA 🇦🇷\n')

        elif golesPolonia > golesArgentina:
            puntosPolonia += 3
            print('\nGANA POLONIA 🇵🇱\n')

        else:
            puntosArgentina += 1
            puntosPolonia += 1
            print('\nEMPATE\n')

for g in range(2,4):

    if grupoC[g] == 'MÉXICO 🇲🇽':
        golesArabia = random.choice(goles)
        golesMex = random.choice(goles)

        print(f'{grupoC[1]} {golesArabia} vs {grupoC[g]} {golesMex}')

        if golesArabia > golesMex:
            puntosArabia += 3
            print('\nGANA ARABIA SAUDITA 🇸🇦\n')

        elif golesMex > golesArabia:
            puntosMex += 3
            print('\nGANA MÉXICO 🇲🇽\n')

        else:
            puntosArabia += 1
            puntosMex += 1
            print('\nEMPATE\n')

    elif grupoC[g] == 'POLONIA 🇵🇱':
        golesArabia = random.choice(goles)
        golesPolonia = random.choice(goles)

        print(f'{grupoC[1]} {golesArabia} vs {grupoC[g]} {golesPolonia}')

        if golesArabia > golesPolonia:
            puntosArabia += 3
            print('\nGANA ARABIA SAUDITA 🇸🇦\n')

        elif golesIran > golesGales:
            puntosPolonia += 3
            print('\nGANA POLONIA 🇵🇱\n')

        else:
            puntosArabia += 1
            puntosPolonia += 1
            print('\nEMPATE\n')


for g in range(3,4):

    if grupoC[g] == 'POLONIA 🇵🇱':
        golesMex = random.choice(goles)
        golesPolonia = random.choice(goles)

        print(f'{grupoC[2]} {golesMex} vs {grupoC[g]} {golesPolonia}')

        if golesMex > golesPolonia:
            puntosMex += 3
            print('\nGANA MÉXICO 🇲🇽\n')

        elif golesPolonia > golesMex:
            puntosPolonia += 3
            print('\nGANA POLONIA 🇵🇱\n')

        else:
            puntosMex += 1
            puntosPolonia += 1
            print('\nEMPATE\n')

puntos_grupoC = {
'ARGENTINA 🇦🇷':puntosArgentina,
'ARABIA SAUDITA 🇸🇦':puntosArabia,
'MÉXICO 🇲🇽':puntosMex,
'POLONIA 🇵🇱':puntosPolonia }

sort_grupoC = sorted(puntos_grupoC.items(), key=lambda x: x[1], reverse=True)

pasa_GrupoC = [] 
print(f'\nTABLA GRUPO C\n')
for k,v in sort_grupoC:
    print(f'{k} : {v}   PUNTOS ')
    pasa_GrupoC.append(k)

print(f'\nAVANZAN {pasa_GrupoC[0]} Y {pasa_GrupoC[1]}\n')
 
# it will be finished soon hehe
