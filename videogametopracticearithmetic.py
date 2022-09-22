# Author: Juan Manuel Hernández Solano 
# Date: 10 / 21

# Importamos librerías
import random
import math

banco_respuestas = [[12]] # Matriz 1
pronombres = [['Viajero', 'elegido'], ['Viajera', 'elegida'], ['Viajere', 'elegide']] # Matriz 2
niveles_pasados = [] # Lista 1
scores = [] # Lista 2
paz = [] # Lista 3
datos = [] # Lista 4

nombre = input('Ingrese su nombre completo ')
datos.append(nombre)
genero = input('Hola, ¿Con qué género te identificas?\n1.Hombre\n2.Mujer\n3.No binario\nIngrese el número ')
ge = 0
if genero == '1':
    ge = 0
    datos.append('Hombre')
elif genero == '2':
    ge = 1
    datos.append('Mujer')
elif genero == '3':
    ge = 2
    datos.append('No binario')
else:
    print('Haz ingresado un número no válido, así que te identificaremos como no binario ')
    ge = 2
    datos.append('Se le identificó como No binario')

print(f'''
              _,._      
  .||,       /_ _\\     
 \.`',/      |'L'| |    
 = ,. =      | -,| L    
 / || \    ,-'\"/,'`.   
   ||     ,'   `,,. `.  
   ,|____,' , ,;' \| |  
  (3|\    _/|/'   _| |  
   ||/,-''  | >-'' _,\\ 
   ||'      ==\ ,-'  ,' 
   ||       |  V \ ,|   
   ||       |    |` |   
   ||       |    |   \  
   ||       |    \    \ 

Hola {pronombres[ge][0]}, haz sido {pronombres[ge][1]} para iniciar una busqueda hacia el tesoro de Moctezuma

Deberás recolectar varias pistas para llegar al tesoro

La primera de ellas está en el Valle de Texcoco
Suerte {pronombres[ge][0]}
''')

# NIVEL 01
def nivel01():
    print('''
    Haz llegado al Valle

     O                                ~)
    º|--                              .(_/^\           ~)       ~)        ~)
    l l                               ./|~|\   ~)    .'(_/^\'..'(_/^\'..'(_/^\. ~) 
                                        /'/'/'|''(_/^\'   /|~|\    /|~|\    /|~|\''(_/^\       |PISTA|

    Pero hay una manada de 6 Aves Salvajes...
    Pero no te preocupes, en tu mochila tienes croquetas para aves
    ''')

    while True: # Ciclo hasta que el usuario ya no quiera responder
        ans_nivel01 = int(input('Si para tranquilizar a las aves tienes que darles 2 croquetas a cada una\n¿Cuántas croquetas les debes dar? '))

        if ans_nivel01 == banco_respuestas[0][0]:
            print('Bien hecho viajero\nLa segunda parada es al bosque del Búho Cósmico')
            niveles_pasados.append('NIVEL01')
            scores.append(100)
            break
        else:
            intento02 = input(f'Respuesta incorrecta\n{pronombres[ge][0]} ¿Quieres volver a intentarlo?\n1.Sí\n2.Si NO, pulsa cualquier otra tecla ')
            if intento02 != '1':
                print(f'Lo lamento {pronombres[ge][0]}, las aves te han sacado las tripas\nLa respuesta correcta era {banco_respuestas[0][0]} ')
                scores.append(0)
                break
nivel01()

# NIVEL 02
def nivel02():
    print('''
    Haz llegado y el Búho te dice un una frase de sabiduría
    -- "Primero se hacen las multiplicaciones y divisiones y luego las sumas y restas"
                                    /\ /\ 
      O                            ((ovo))
     º|--                          ():::() |PISTA|
     l l                             VVV

    Para que el Búho te de la segunda pista y sigamos con tu camino
    tienes que resolver las siguientes operaciones:
    ''')
    # Valores númericos aleatorios
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    c = random.randint(1, 20)
    d = random.randint(1, 5)

    score02 = 0
    op1 = a * b - c / d

    while True: # Ciclo hasta que el usuario ya no quiera responder
        re1 = float(input(f'Ingresa el resultado correcto\n({a} * {b}  - {c} / {d}) '))

        if op1 == re1:
            print('Bien wuachin, ese es el resultado correcto\nLa pista indica que la próxima parada es...\nEl barrio chino ')
            score02 += 1
            niveles_pasados.append('NIVEL01')
            scores.append(score02*100/1)
            break
        else:
            intento02 = input(f'Respuesta incorrecta\n{pronombres[ge][0]} ¿Quieres volver a intentarlo?\n1.Sí\n2.Si NO, pulsa cualquier otra tecla ')
            if intento02 != '1':
                print(f'El resultado correcto era {op1} ')
                scores.append(0)
                break
    return
nivel02()

# NIVEL 03
def nivel03():
    print(f'''
    {pronombres[ge][0]} haz llegado al barrio Chino...
             .
         |
    .   ]#[   .
     \_______/
  .    ]###[    .
   \___________/
.     ]#####[     .
 \___]#.---.#[___/
  |__|_|   |_|__|
  |__|_|___|_|__|
  #####/___\#####
      |_____|
     /_______\

    y encuentras el siguiente mensaje:

    🀄 🀀 🀀 🀂 🀃 🀅 🀆 🀇 🀈 🀉 🀊 🀋 🀌 🀍 🀎 🀏 🀐 🀑 🀒 🀓 🀔 🀕 
                        |PISTA|
    🀖 🀗 🀘 🀙 🀚 🀛 🀜 🀝 🀞 🀟 🀠 🀡 🀢 🀣 🀤 🀥 🀦 🀧 🀨 🀩 🀪 🀫
    ''')
    print("Para decifrar el mensaje debes resolver estos 6 ejercicios correctamente ")
    divisor=0
    dividendo=0
    division=0
    resp3=0

    while True: # Ciclo hasta que el usuario ya no quiera responder
        score03 = 0
        for divisiones in range (6):
            divisor=random.randrange(2,10)
            dividendo=2*random.randrange(2,10)
            division = round(dividendo/divisor,2)
            print("¿Cual es el resultado de la siguiente division? ", dividendo, "/", divisor)
            resp3 = float(input("Su respuesta es: (Ingrese su respuesta redondeando con 2 decimales, si es que tiene claro) "))
            if resp3 == division:
                print("RESPUESTA CORRECTA")
                score03 += 1
            else:
                print("INCORRECTO")
                print(f'El resultado correcto es {division} ')
                
        if score03 != 6:
            intento03 = input(f'Respondiste {score03} respuestas correctas\n{pronombres[ge][0]} ¿Quieres volver a intentarlo?\n1.Sí\n2.Si NO, pulsa cualquier otra tecla ')
            if intento03 != '1':
                print(f'Una lastima {pronombres[ge][0]} solo te faltaron {6 - score03}')
                scores.append((6 - score03)*100/6)
                break
        else:
            print(f'Felicidades {pronombres[ge][0]}, todo parece indicar que la siguiente pista estará en el puerto de acapulco')
            scores.append(score03*100/6)
            break
    return
nivel03()

#NIVEL 04
def nivel4():
    print(f'''
    {pronombres[ge][0]} después de un largo viaje en barco haz llegado al puerto de acapulco

    ░░▄▀▀▀▄░▄▄░░░░░░╠▓░░░░
    ░░░▄▀▀▄█▄░▀▄░░░▓╬▓▓▓░░
    ░░▀░░░░█░▀▄░░░▓▓╬▓▓▓▓░
    ░░░░░░▐▌░░░░▀▀███████▀
    ▒▒▄██████▄▒▒▒▒▒▒▒▒▒▒▒▒

    La pista la tiene un acapulqueño en una botella
       _____
      (.....)
       |...|
       |...|
       |...|
      /.....\

     |.......|
     |.......|
     ||PISTA||
     |.......|
     (_______)

    ''')
    print("Para que te de la pista el acapulqueño debes resolver estos 6 ejercicios correctamente ")
    numerador1=0
    numerador2=0
    denominador=0
    sumafrac=0
    respfrac=0
    while True: # Ciclo hasta que el usuario ya no quiera responder
        score04 = 0
        for questions in range (6):
                numerador1= random.randrange(2,15)
                numerador2= random.randrange(2,15)
                denominador= random.randrange(2,15)
                sumnum=numerador1+numerador2
                print("¿Cual es la suma de la siguientes fracciones? ", numerador1,"/",denominador,"+", numerador2,"/",denominador)
                respuesta04 = input("Inserte el resultado en forma de fracción (a/b) ")
                ans04 = str(sumnum) + '/' + str(denominador)
                if respuesta04 == ans04:
                    print("CORRECTO")
                    score04 += 1
                else:
                    print("INCORRECTO")
                    print(f'El resultado correcto es {sumnum}/{denominador} ')

        if score04 != 6:
            intento04 = input(f'Respondiste {score04} respuestas correctas\n{pronombres[ge][0]} ¿Quieres volver a intentarlo?\n1.Sí\n2.Si NO, pulsa cualquier otra tecla ')
            if intento04 != '1':
                print(f'Una lastima {pronombres[ge][0]} solo te faltaron {6 - score04}')
                scores.append((6 - score04)*100/6)
                break
        else:
            print(f'Bien hecho {pronombres[ge][0]}, siguiente parada: Las pirámides de Tenochtitlan ')
            scores.append(score04*100/6)
            break
nivel4()

# NIVEL 05
def nivel05():
    print('''Frente a ti, la pirámide mayor...

      ..  ...  ...  ...  ..      .        ..  ....  .....  .....
    ...  .... .... .....     .%/\      .. ....  .....  .....  .
    .  ...  ...  ... ..     .%./  &.     ....  ......  ....  ...
    ..  ....  ..  ...     .%**/     \        .....  .....  ....
    ....  ....  ..      .%***/       &.     .....  .....  ...  .
    ......  .... .    .%.***/  .   _  \      . ......  ... ....
    .......       .%*****/ -'      `'.&.     .....  ... .....
    ..     ..     .%******/  ._."""'~::,  \      . ... .....   .
    .......     .%*******/._'` .'"^':,  :.,&.     . ....  .....
    ...       .%********/',_-^{  ( )  }    :.\       ........ ..
    ..     .%*********/%^    '.     .'     ;.&.     .  ... ....
    .     .%**********/;        ".,."        ;#.\     .  . .....
        .%***********/  ~'.,,.          ,.-'^    &.     . ... ..
      .%************/         ""-.,.-""~           \     . . ..
    .%*************/                                &.     .. ..
   %**************/                                   \     ...
    
    
    ''' )
    print("Para obtener de la pirámide la pista, debes responder las 2 preguntas correctamente ")

    while True:
        score05 = 0
        for i in range (2):
            numerador15=random.randrange(1,15)
            denominador15=random.randrange(2,15)
            numerador25=random.randrange(1,15)
            denominador25=random.randrange(2,15)
            multinum5=numerador15*numerador25
            multiden5=denominador15*denominador25
            divinumerador=numerador15*denominador25
            dividenominador=denominador15*numerador25

            print("Calcule la multiplicación y division de estas dos fracciones: ", numerador15,"/",denominador15, "&", numerador25,"/",denominador25)

            respuno5 = input("Inserte el resultado de la multiplicación de forma de fracción (a/b) ")
            ansuno5 = str(multinum5) + '/' + str(multiden5)
            
            if respuno5 == ansuno5:
                print("CORRECTO")
                score05 += 0.5
                print(score05)
            else:
                print("INCORRECTO")
                print(f'El resultado correcto es {ansuno5} ')

            respdos5 = input("Inserte el resultado de la división de forma de fracción (a/b) ")
            ansdos5 = str(divinumerador) + '/' + str(dividenominador)

            if respdos5 == ansdos5:
                print("CORRECTO")
                score05 += 0.5
                print(score05)

            else:
                print("INCORRECTO")
                print(f'El resultado correcto es {ansdos5} ')
        if score05 != 2:
            intento05 = input(f'Respondiste {score05} respuestas correctas\n{pronombres[ge][0]} ¿Quieres volver a intentarlo?\n1.Sí\n2.Si NO, pulsa cualquier otra tecla ')
            if intento05 != '1':
                print(f'Una lastima {pronombres[ge][0]} solo te faltaron {2 - score05} puntos')
                scores.append((2 - score05)*100/2)
                break
        else:
            print(f'''Felicidades {pronombres[ge][0]}, es momento de llegar al lugar donde obtendras la última pista
            
            ███████╗██╗░░░░░  ██████╗░███████╗░██████╗██╗███████╗██████╗░████████╗░█████╗░  ██████╗░███████╗
            ██╔════╝██║░░░░░  ██╔══██╗██╔════╝██╔════╝██║██╔════╝██╔══██╗╚══██╔══╝██╔══██╗  ██╔══██╗██╔════╝
            █████╗░░██║░░░░░  ██║░░██║█████╗░░╚█████╗░██║█████╗░░██████╔╝░░░██║░░░██║░░██║  ██║░░██║█████╗░░
            ██╔══╝░░██║░░░░░  ██║░░██║██╔══╝░░░╚═══██╗██║██╔══╝░░██╔══██╗░░░██║░░░██║░░██║  ██║░░██║██╔══╝░░
            ███████╗███████╗  ██████╔╝███████╗██████╔╝██║███████╗██║░░██║░░░██║░░░╚█████╔╝  ██████╔╝███████╗
            ╚══════╝╚══════╝  ╚═════╝░╚══════╝╚═════╝░╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░  ╚═════╝░╚══════╝

            ░██████╗░█████╗░███╗░░██╗░█████╗░██████╗░░█████╗░
            ██╔════╝██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔══██╗
            ╚█████╗░██║░░██║██╔██╗██║██║░░██║██████╔╝███████║
            ░╚═══██╗██║░░██║██║╚████║██║░░██║██╔══██╗██╔══██║
            ██████╔╝╚█████╔╝██║░╚███║╚█████╔╝██║░░██║██║░░██║
            ╚═════╝░░╚════╝░╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝ 
            ''')
            scores.append(100)
            break
    return
nivel05()

print('''

Haz llegado, lo único que tienes que hacer ahora es resolver el siguiente problema de la vida real

             .
          \  :  / 
           ' _ '
       -= ( (_) ) =-
           .   .
          /  :  \
      .-.    '
      |.|
    /)|`|(\
   (.(|'|)`)
~~~~`\`'./'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      |.|           ~~
      |`|                            ~~
     ,|'|.      (_)          ~~
      "'"        \"\
           ~~     ^~^

''')
# NIVEL 06
def nivel06():
    print("NIVEL 6 \n ---PROBLEMA DE LA VIDA COTIDIANA---")
    print("Dios les da a sus mejores guerreros sus peores batallas, así que preparate para este desafio. \n Este ejercicio es el más complicado de todos, así que no te des por vencido y busca ese tesoro. (El ejercico consta de una sola pregunta) ).")
    edadx=18
    edada=24
    print("¿En el verano del 96', mi amigo es mayor que su xoloitzcuintle y la suman de sus edades es 42, cual es la edad de cada uno sabiendo que mi amigo tiene 5/3 la edad del xoloitzcuintle, menos 6 años?")
    while True:
        amigo=int(input("¿Cual es la edad de mi amigo?"))
        xolo=int(input("¿Cual es la edad del xoloitzcuintle?"))
        if amigo!=edada or edadx!=xolo:
            print("SU RESPUESTA ES INCORRECTA, SIGA INTENTANDO")
            scores.append(100)
        else:
            print("CORRECTO... ve por el tesoro ")
            scores.append(0)
            break
nivel06()
print('''
OH NO
A pesar de que eres el elegido, no eres el único que esta buscando el tesoro... 
        ___
     __|___|__
      ('o_o')
      _\~-~/_    ______.
     //\__/\ \ ~(_]---'
    / )O  O( .\/_)
    \ \    / \_/
    )/_|  |_\

   /_/      \_\
  
    \| |__| |/
     | |  | |
     | |  | |
     |_|  |_|
     /_\  /_\

''')

while True:
    pelea = input('¿Desear batallar de forma armada para conseguir el tesoro?\n1.Sí\n2.No (Ingresa el número) ')
    if pelea == '1':
        break
    else:
        print('No seas cobarde, elige pelear ')
        paz.append('El usuario eligió la paz')

print(f'''
Comienza la batalla*

(҂`_´)
<,︻╦╤─ ҉ - -======░ ▒▓▓█D
_/﹋\_
(҂`_´)
<,︻╦╤─ ҉ - - ======░ ▒▓▓█D
_/﹋\_


██████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░░░░░▄▀░░█░░▄▀░░█
█░░▄▀░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█
█░░▄▀░░██░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░█
█░░▄▀░░░░░░▄▀░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░█
█░░▄▀░░░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░░░░░██░░▄▀░░█░░░░░░█
█░░▄▀░░████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██████████░░▄▀░░████████
█░░▄▀░░░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██████████░░▄▀░░█░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░█
█░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░█
██████████████████████████████████████████████████████████████████████████████

░░░_/﹋\_
░░░(҂`_´)
░░░<,︻╦╤─ ҉ - - ======D
░░░███ ]▄▄▄▄▄▄▄▄
▂▄▅██████▅▄▃▂
Il██████████████].
..◥⊙▲⊙▲⊙▲⊙▲⊙◤ 
.
.....(\_/)
.....( '_')
..../""""""""""""\======┣▇▇▇▇═─
/"""""""""""""""""""\
\@_@_@_@_@_/


         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
     %%%%

Después de mucho pelear, haz ganado {pronombres[ge][0]} aka {nombre} encontraste que el tesoro era...


███████╗██╗░░░░░  ██████╗░░█████╗░██████╗░███████╗██████╗░  ██████╗░███████╗  ██╗░░░░░░█████╗░
██╔════╝██║░░░░░  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗  ██╔══██╗██╔════╝  ██║░░░░░██╔══██╗
█████╗░░██║░░░░░  ██████╔╝██║░░██║██║░░██║█████╗░░██████╔╝  ██║░░██║█████╗░░  ██║░░░░░███████║
██╔══╝░░██║░░░░░  ██╔═══╝░██║░░██║██║░░██║██╔══╝░░██╔══██╗  ██║░░██║██╔══╝░░  ██║░░░░░██╔══██║
███████╗███████╗  ██║░░░░░╚█████╔╝██████╔╝███████╗██║░░██║  ██████╔╝███████╗  ███████╗██║░░██║
╚══════╝╚══════╝  ╚═╝░░░░░░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝  ╚═════╝░╚══════╝  ╚══════╝╚═╝░░╚═╝

░█████╗░███╗░░░███╗██╗░██████╗████████╗░█████╗░██████╗░
██╔══██╗████╗░████║██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
███████║██╔████╔██║██║╚█████╗░░░░██║░░░███████║██║░░██║
██╔══██║██║╚██╔╝██║██║░╚═══██╗░░░██║░░░██╔══██║██║░░██║
██║░░██║██║░╚═╝░██║██║██████╔╝░░░██║░░░██║░░██║██████╔╝
╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░

Tu promedio fue de {sum(scores)/6}

''')
