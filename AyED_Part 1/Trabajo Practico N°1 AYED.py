
# Trabajo Práctico 1 - AyED Comisión 102
# Integrantes: Maximiliano Gomez, Axel Jurista, Godoy Valentin, Jeffrey Wetzel

# Librerias
import os 

# Variables
opcion, opcion1, opcion2, continuar = -1, '', '', ''
patente, patenteminsoja, patentemaxsoja, patenteminmaiz, patentemaxmaiz, cantcam, cantcamsoja, cantcammaiz, tipodeproducto = '','','','','', 0, 0, 0, ''
pesonetosoja, pesonetominsoja, pesonetomaxsoja, pesonetosojatotal, pesopromsoja = 0, 500000, 0, 0, 0
pesonetomaiz, pesonetominmaiz, pesonetomaxmaiz, pesonetomaiztotal, pesoprommaiz = 0, 500000, 0, 0, 0

# Funciones

def menuOP(): # Menu Opciones Principal
    print(f'''
--- Menu Principal ---
1 - ADMINISTRACIONES
2 - ENTREGA DE CUPOS
3 - RECEPCION
4 - REGISTRAR CALIDAD
5 - REGISTRAR PESO BRUTO
6 - REGISTRAR DESCARGA
7 - REGISTRAR TARA
8 - REPORTES
0 - Fin del Programa''')


def menuOP1(): # Menu Opcion Administraciones
    print(f'''
--- ADMINISTRACIONES ---
A - TITULARES
B - PRODUCTOS 
C - RUBROS
D - RUBROS x PRODUCTO
E - SILOS
F - SUCURSALES
G - PRODUCTO POR TITULAR
V - Volver al Menu Principal''')


def menuOpSub1(): # SubMenu Opciones Administraciones
    print(f''' 
- SUB MENU -
A. ALTA
B. BAJA
C. CONSULTA
M. MODIFICACION
V. VOLVER AL MENU ANTERIOR''')


def subAdmin(): # SubMenu Opciones Administraciones
    while True:
        menuOpSub1()
        opcion2 = str(input('Ingrese una opcion: '))
        opcion2 = opcion2.upper() # Se usa .upper() para asegurarnos de que sea un caracterer en mayuscula
        while (opcion2 == 'A' or opcion2 == 'B' or opcion2 == 'C' or opcion2 == 'M' or opcion2 == 'V'):
            
            if opcion2 == 'A':
                menuOD()
                menuOpSub1()
                opcion2 = str(input('Ingrese una opcion: ')) # Volvemos a pedir que lea la opcion 
            elif opcion2 == 'B':
                menuOD()
                menuOpSub1()
                opcion2 = str(input('Ingrese una opcion: '))
            elif opcion2 == 'C':
                menuOD()
                menuOpSub1()
                opcion2 = str(input('Ingrese una opcion: '))
            elif opcion2 == 'M':
                menuOD()
                menuOpSub1()
                opcion2 = str(input('Ingrese una opcion: '))
            elif opcion2 == 'V':
                salidaAdmin()


def menuOD(): # Alerta funcionalidades en desarrollo
    valor  = int(input('Esta funcionalidad está en desarrollo. Ingrese 0 para volver al menu anterior: '))
    while valor !=0:
        valor = int(input('Porfavor ingrese 0 para salir: '))


def salidaAdmin(): # ADMINISTRACIONES
    while True:
        menuOP1()
        opcion1 = str(input('Ingrese una opcion: '))
        opcion1 = opcion1.upper() # Se usa .upper() para asegurarnos de que sea un caracterer en mayuscula
        while (opcion1 == 'A' or opcion1 == 'B' or opcion1 == 'C' or opcion1 == 'D' or opcion1 == 'E' or opcion1 == 'F' or opcion1 == 'G' or opcion1 == 'V'):

         if opcion1 == 'A':
            os.system('cls') 
            subAdmin()           
         elif opcion1 == 'B':
            os.system('cls') 
            subAdmin()           
         elif opcion1 == 'C':
            os.system('cls') 
            subAdmin()           
         elif opcion1 == 'D':
            os.system('cls') 
            subAdmin()
         elif opcion1 == 'E':
            os.system('cls') 
            subAdmin()
         elif opcion1 == 'F':
            os.system('cls') 
            subAdmin()
         elif opcion1 == 'G':
            os.system('cls') 
            subAdmin()
         elif opcion1 == 'V':
            os.system('cls') 
            menuPrincipal()


def producto(): # Producto
    global tipodeproducto 

    tipodeproducto = str(input('Ingrese el tipo de producto (S para soja o M para maiz) : '))
    tipodeproducto = tipodeproducto.upper() # Se usa .upper() para asegurarnos de que sea un caracterer en mayuscula
    while tipodeproducto != 'S' and tipodeproducto !='M':
        print('Opcion inexistente\n')
        tipodeproducto = str(input('Porfavor ingrese nuevamente el tipo de producto (S para Soja) o (M para Maiz): '))


def patmaxsoja(): # Patente del camion que más soja descargo
    global pesonetosoja, pesonetomaxsoja, patente, patentemaxsoja # global sirve para modificar el valor de una variable global

    if pesonetosoja > pesonetomaxsoja:
        pesonetomaxsoja = pesonetosoja
        patentemaxsoja = patente
        

def patminsoja(): # Patente del camion que menos soja descargo
    global pesonetosoja, pesonetominsoja, patente, patenteminsoja

    if pesonetosoja < pesonetominsoja:
        pesonetominsoja = pesonetosoja
        patenteminsoja = patente


def menuproductosoja(): # Opción producto Soja
    global pesonetosoja, pesonetosojatotal

    pesobruto = int(input('Ingrese el peso bruto del camión en Kg: '))
    tara = int(input('Ingrese el peso del camión vacío en Kg: '))
    pesonetosoja = pesobruto - tara 
    print(f'El peso neto son {pesonetosoja} Kg')
    pesonetosojatotal = pesonetosojatotal + pesonetosoja
    patmaxsoja()
    patminsoja()


def patmaxmaiz(): # Patente del camion que más maiz descargo
    global pesonetomaiz, pesonetomaxmaiz, patente, patentemaxmaiz

    if pesonetomaiz > pesonetomaxmaiz:
        pesonetomaxmaiz = pesonetomaiz
        patentemaxmaiz = patente


def patminmaiz(): # Patente del camion que menos maiz descargo
    global pesonetomaiz, pesonetominmaiz, patente, patenteminmaiz

    if pesonetomaiz < pesonetominmaiz:
        pesonetominmaiz = pesonetomaiz
        patenteminmaiz = patente


def menuproductomaiz(): # Opción producto maiz
    global pesonetomaiz, pesonetomaiztotal

    pesobruto = int(input('Ingrese el peso bruto del camión en Kg: '))
    tara = int(input('Ingrese el peso del camión vacío en Kg: '))
    pesonetomaiz = pesobruto - tara 
    print(f'El peso neto son {pesonetomaiz} Kg')
    pesonetomaiztotal = pesonetomaiztotal + pesonetomaiz
    patmaxmaiz()
    patminmaiz()


def cantcamproductos(): # Contador de camiones de cada producto
    global cantcammaiz, cantcamsoja

    if tipodeproducto == 'S':
        cantcamsoja += 1
        menuproductosoja()
    elif tipodeproducto == 'M':
        cantcammaiz += 1
        menuproductomaiz()
        

def otrocamion(): # Bucle para ingresar más camiones
    global continuar

    continuar = str(input(f'¿Desea ingresar otro camión? - Ingrese S para continuar o N para volver al menu principal: '))
    continuar = continuar.upper() # Se usa .upper() para asegurarnos de que sea un caracterer en mayuscula
    while (continuar != 'S' and continuar !='N'):
        print('Porfavor ingrese un caracter valido\n')
        continuar = str(input('¿Desea ingresar otro camión? - Ingrese S para continuar o N para volver al menu principal: '))
    if continuar == 'S':
        recepcion()


def recepcion(): # RECEPCION
    global patente, cantcam, pesopromsoja, pesoprommaiz

    patente = str(input('Ingrese el numero de patente: '))
    producto()
    cantcamproductos()
    cantcam += 1 # Suma 1 a cantidad de camiones
    otrocamion()
    pesopromsoja = pesonetosojatotal/cantcamsoja # Divide el peso neto total con la cantidad de camiones para obtener el promedio
    pesoprommaiz = pesonetomaiztotal/cantcammaiz # Divide el peso neto total con la cantidad de camiones para obtener el promedio


def reportes(): # REPORTES
    print(f''' 
  REPORTES 
- Cantidad total de camiones que llegaron: {cantcam}
- Cantidad total de camiones de Soja ingresados: {cantcamsoja}
- Cantidad total de camiones de Maiz ingresados: {cantcammaiz}
- Peso neto total de soja: {pesonetosojatotal} Kg
- Peso neto total de maiz: {pesonetomaiztotal} Kg
- Promedio del peso neto de soja por camion: {pesopromsoja} Kg
- Promedio del peso neto de maiz por camion: {pesoprommaiz} Kg
- Patente del camión de soja que mayor cantidad descargo: {patentemaxsoja}
- Patente del camión de soja que menor cantidad descargo: {patenteminsoja}
- Patente del camión de maiz que mayor cantidad descargo: {patentemaxmaiz}
- Patente del camión de maiz que menor cantidad descargo: {patenteminmaiz}''')
    salida1 = int(input('Ingrese 0 para volver al menu principal: '))
    while salida1 != 0:
        print('Caracter Invalido')
        salida1 = int(input('Ingrese 0 para volver al menu principal: '))
    menuPrincipal()


def menuPrincipal(): # Inicio
    global opcion 
    
    while True:
        menuOP()
        while True: #Bucle infinito con condicion de salida, simula un Do While - (Hacer Mientras)
            try:
                opcion = int(input('Ingrese unas de las opciones 1/8 o ingrese 0 para salir: '))
            except ValueError: # Para que el programa no se rompa si ingresan un valor que no se puede convertir a entero.
                print('Por favor ingrese un número entero de las opciones\n')
            if ( opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5 or opcion == 6 or opcion == 7 or opcion == 8 or opcion == 0): # Condicion de salida del bucle
                break

        if opcion == 2 or opcion == 4 or opcion == 5 or opcion == 6 or opcion == 7:
            menuOD() # Menu indicando que las funciones esta en desarollo
        elif opcion == 1:
            os.system('cls') # Borra la terminal
            salidaAdmin() # Ingresa a Administraciones
        elif opcion == 3:
            os.system('cls') # Borra la terminal
            recepcion() # Ingresa a Recepcion
        elif opcion == 8:
            os.system('cls') # Borra la terminal
            reportes() # Ingresa a Reportes
        elif opcion == 0:
            raise SystemExit # Cierra el programa
    

# Main
menuPrincipal()
