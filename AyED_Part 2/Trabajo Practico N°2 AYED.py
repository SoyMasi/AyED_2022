

# Trabajo Práctico 2 - AyED Comisión 102
# Integrantes: Maximiliano Gomez, Axel Jurista, Godoy Valentin, Jeffrey Wetzel

# -----------------------------------------------------------------------------------------------------
# Librerias
import os

# -----------------------------------------------------------------------------------------------------
# Declaraciones
 
# Type 
# productos = array [0..2] of string 
# patentes = array [0..7] of string
# estados = array [0..7] of char
# cupos = array [0..7] of integer
# pesobruto = array [0..7] of integer
# tara = array [0..7] of integer
# pesoneto = array [0..7] of integer

# Variables 
# Pr = productos
# P = patentes
# E = estados
# C = cupos
# PB = pesobruto
# T = tara
# PN = pesoneto

#Dimensiones Array
TamPR = 3
TamP = 8
TamC = 8
TamE = 8
TamPB = 8
TamT = 8
TamPN = 8

#Arrays
Pr=['']* TamPR # productos
P = [''] * TamP # patente
E = [''] * TamE # estados
C = [0] * TamC # cupos
Pb = [0] * TamPB # peso bruto
T = [0] * TamT # tara
Pn = [0] * TamPN # peso neto

# Variables
opc,opcion,opcion1,opcion2,opcionp = True ,-1, '', '',''
acumCupo = 1
pat = ''
z,l = 0, 0

#Contadores
cantcam, cantcamsoja, cantcammaiz, cantcamtrigo, cantcamgirasol, cantcamcebada = 0, 0, 0, 0, 0, 0

pesopromsoja, pesoprommaiz, pesopromtrigo, pesopromgirasol, pesopromcebada = 1, 1, 1, 1, 1
pesonetosoja, pesonetomaiz, pesonetotrigo, pesonetogirasol, pesonetocebada = 0, 0, 0, 0, 0
pesonetototalsoja, pesonetototalmaiz, pesonetototaltrigo, pesonetototalgirasol, pesonetototalcebada = 0, 0, 0, 0, 0
pesonetominsoja , pesonetominmaiz , pesonetomintrigo, pesonetomingirasol, pesonetomincebada = 0, 0, 0, 0, 0
pesonetomaxsoja, pesonetomaxmaiz, pesonetomaxtrigo, pesonetomaxgirasol, pesonetomaxcebada = 0, 0, 0, 0, 0
patentemaxsoja, patentemaxmaiz, patentemaxtrigo, patentemaxgirasol, patentemaxcebada = '', '', '', '', ''
patenteminsoja, patenteminmaiz, patentemintrigo, patentemingirasol, patentemincebada = '', '', '', '', ''

# -----------------------------------------------------------------------------------------------------
# Menus

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

def menuOD(): # Alerta funcionalidades en desarrollo
    valor  = int(input('Esta funcionalidad está en desarrollo. Ingrese 0 para volver al menu anterior: '))
    while valor !=0:
        valor = int(input('Porfavor ingrese 0 para salir: '))


# -----------------------------------------------------------------------------------------------------
# Busquedas y Funciones Utiles

def buscaSec(W, e): #W - el array  # e - elemento a buscar
    for i in range(0,len(W)):
        if e == W[i]:
            return True
    return False

def ordenarDes(C, Tam):
    for i in range (0, Tam-1):
        for n in range (i+1, Tam):
            if (C[i]<C[n]):
                aux = C[i]
                C[i] = C[n]
                C[n] = aux


# -----------------------------------------------------------------------------------------------------
# Productos

def menuProd():
    global opcionp, opc  
    while opc == True:
        while True:
            print(f''' 
- PRODUCTOS -
A. ALTA
B. BAJA
C. CONSULTA
M. MODIFICACION
V. VOLVER AL MENU ANTERIOR\n''')
            opcionp = str(input('Ingrese una opción: '))
            opcionp = opcionp.upper()
            if (opcionp == 'A' or opcionp == 'B' or opcionp == 'C' or opcionp == 'M' or opcionp == 'V'):
                break
        if opcionp == 'A':
            altaProd(Pr)
            opc = True
        elif opcionp == 'B':
            bajaProd(Pr)
            opc = True
        elif opcionp  == 'C':
            consultaProd(Pr)
            opc = True
        elif opcionp == 'M': 
            modProd(Pr)
            opc = True
        elif opcionp == 'V':
            opc = False


def altaProd(C):
    global continuarProd, z
    print(C)
    continuarProd = 'S'
    X = False
    
    while z < 3 and continuarProd =='S':
        while True:
            print(f'''Los productos disponibles a ingresar son: T - Trigo / S - Soja / M - Maiz / G - Girasol / C - Cebada''')
            print(f'Los productos cargados son {C}\n') 
            try:
                prod = str(input('Ingrese la inicial del producto que quiere agregar: '))
                prod = prod.upper() 
            except: # Para que el programa no se rompa si ingresan un valor que no se encuentra en las opciones.
                print('Por favor ingrese un una letra de las opciones disponibles\n')
            if (prod == 'T' or prod == 'S' or prod == 'M' or prod == 'G' or prod == 'C'):
                X = buscaSec(C, prod) 
                break
        if (z < 3 and X == False):
            C[z] = prod
            z += 1
            continuarProd = str(input('¿Desea ingresar otro producto? - Ingrese S para continuar o N para volver al menu anterior: '))
            continuarProd = continuarProd.upper()
        elif (z < 3 and  X == True):
            print('El valor ingresado ya se encuentra registrado \n')
    else:
        print('Para ingresar un nuevo valor es necesario eliminar o modificar uno de los elementos, porfavor ingrese a las opciones correspondientes \n')


def bajaProd(C):
    global z 

    i = 0
    while i < len(C):
        print(f'Indice: {i}  Producto: {C[i]}')
        i+=1
    try:
        k = int(input('Ingrese el indice del producto a eliminar: '))
    except ValueError:
        print('Porfavor Ingrese un indice valido')
    if (C[k] == 'T' and cantcamtrigo!=0):
        print('No se puede eliminar el producto, debido a que ya hay un camión registrado con este producto')
    elif (C[k] == 'M' and cantcammaiz!=0):
        print('No se puede eliminar el producto, debido a que ya hay un camión registrado con este producto')
    elif (C[k] =='S' and cantcamsoja!=0):
        print('No se puede eliminar el producto, debido a que ya hay un camión registrado con este producto')
    elif (C[k] == 'C' and cantcamcebada!=0):
        print('No se puede eliminar el producto, debido a que ya hay un camión registrado con este producto')
    elif (C[k] == 'G' and cantcamgirasol!=0):
        print('No se puede eliminar el producto, debido a que ya hay un camión registrado con este producto')
    else: # C[k] == Cualquiera de los productos y cantcamiones de ese producto == 0
        C[k] = ' '
        ordenarDes(C, TamPR)
        z -= 1
        print(C)


def consultaProd(C):
    i = 0
    print(f'Productos: T - Trigo / S - Soja / M - Maiz / G - Girasol / C - Cebada \n')
    print(f'Productos cargados:')
    while i < len(C):
        print(f'Indice: {i}  Producto: {C[i]}')
        i+=1
    input('Pulse cualquier tecla para continuar: ')


def modProd(C):
    global h
    u = True
    i= 0

    while i < len(C):
        print(f'Indice: {i}  Producto: {C[i]}')
        i+=1
    while u == True:
        h = int(input('Ingrese el indice a modificar: '))
        if (h == 1 or h == 2 or h == 0):
            print(f'Productos: T - Trigo / S - Soja / M - Maiz / G - Girasol / C - Cebada \n')
            try:
                val = str(input('Ingrese la letra inicial del nuevo Producto: '))
                val = val.upper()
            except:
                print('Por favor ingrese un una letra de las opciones disponibles\n')
            if (val == 'T' or val == 'S' or val == 'M' or val == 'G' or val == 'C'):
                buscaVal = buscaSec(C, val)
                break
    if (buscaVal == False):
        C[h] = val
        u = False
    elif(buscaVal == True or buscaVal == None):
        print('Porfavor ingrese una opcion que no esa repetida')
        u = True


# -----------------------------------------------------------------------------------------------------
# Menu Terciario Administracion

def SubAdmin():
    global opcion2, opc
    while opc == True:
        while True: 
            menuOpSub1()
            opcion2 = str(input('Ingrese A para menu o V para salir al menu anterior: '))
            opcion2 = opcion2.upper()
            if (opcion2 == 'A' or opcion2 == 'B' or opcion2 == 'C' or opcion2 == 'M' or opcion2 == 'V'):
                break
        if opcion2 == 'A':
            menuOD()
            opc = True
        elif opcion2 == 'B':
            menuOD()
            opc = True
        elif opcion2 == 'C':
            menuOD()
            opc = True
        elif opcion2 == 'M':
            menuOD()
            opc = True
        elif opcion2 == 'V':
            opc = False


# -----------------------------------------------------------------------------------------------------
# Menu Secundario Administracion

def Administracion():
    global opcion1, opc
    while opc == True:
        while True:
            menuOP1()
            opcion1 = str(input('Ingrese A para menu o V para salir al menu anterior: '))
            opcion1 = opcion1.upper()
            if (opcion1 == 'A' or opcion1 == 'B' or opcion1 == 'C' or opcion1 == 'D' or opcion1 == 'E' or opcion1 == 'F' or opcion1 == 'G' or opcion1 == 'V'):
                break
        if opcion1 == 'A':
            os.system('cls')
            SubAdmin()
            opc = True
        elif opcion1 == 'B':
            os.system('cls') 
            menuProd()
            opc = True           
        elif opcion1 == 'C':
            os.system('cls') 
            SubAdmin()
            opc = True           
        elif opcion1 == 'D':
            os.system('cls') 
            SubAdmin()
            opc = True
        elif opcion1 == 'E':
            os.system('cls') 
            SubAdmin()
            opc = True
        elif opcion1 == 'F':
            os.system('cls') 
            SubAdmin()
            opc = True
        elif opcion1 == 'G':
            os.system('cls') 
            SubAdmin()
            opc = True
        elif opcion1 == 'V':
            os.system('cls')
            opc = False


# -----------------------------------------------------------------------------------------------------
# Reportes
def reportes():
    print(f'''
    REPORTES
- Cantidad de cupos otorgados: {acumCupo}
- Cantidad total de camiones recibidos: {cantcam}
- Cantidad total de camiones por producto:  Soja [{cantcamsoja}] / Maiz [{cantcammaiz}] / Trigo [{cantcamtrigo}] / Girasol [{cantcamgirasol}] / C[{cantcamcebada}]
- Peso neto total por producto:  Soja [{pesonetototalsoja}] / Maiz [{pesonetototalmaiz}] / Trigo [{pesonetototaltrigo}] / Girasol [{pesonetototalgirasol}] / Cebada [{pesonetototalcebada}]
- Promedio del Peso Neto de producto: Soja [{pesopromsoja}] / Maiz [{pesoprommaiz}] / Trigo [{pesopromtrigo}] / Girasol [{pesopromgirasol}] / Cebada [{pesopromcebada}]
- Patente del camion que mayor cantidad descargo por producto: Soja [{patentemaxsoja}] / Maiz [{patentemaxmaiz}] / Trigo [{patentemaxtrigo}] / Girasol [{patentemaxgirasol}] / Cebada [{patentemaxcebada}]
- Patente del camion que menor cantidad descargo por producot: Soja [{patenteminsoja}] / Maiz [{patenteminmaiz}] / Trigo [{patentemintrigo}] / Girasol [{patentemingirasol}] / Cebada [{patentemincebada}]
''')
    input('Toque cualquier tecla para salir: ')
    os.system('cls')
# -----------------------------------------------------------------------------------------------------
# Patentes Maximo y Minimo

def patmaxmaiz(pat2): # Patente del camion que más maiz descargo
    global pesonetomaiz, pesonetomaxmaiz, patentemaxmaiz

    if pesonetomaiz > pesonetomaxmaiz:
        pesonetomaxmaiz = pesonetomaiz
        patentemaxmaiz = pat2


def patminmaiz(pat2): # Patente del camion que menos maiz descargo
    global pesonetomaiz, pesonetominmaiz, patenteminmaiz

    if pesonetomaiz < pesonetominmaiz:
        pesonetominmaiz = pesonetomaiz
        patenteminmaiz = pat2


def patmaxsoja(pat2): # Patente del camion que más soja descargo
    global pesonetosoja, pesonetomaxsoja, patentemaxsoja 

    if pesonetosoja > pesonetomaxsoja:
        pesonetomaxsoja = pesonetosoja
        patentemaxsoja = pat2
        

def patminsoja(pat2): # Patente del camion que menos soja descargo
    global pesonetosoja, pesonetominsoja, patenteminsoja

    if pesonetosoja < pesonetominsoja:
        pesonetominsoja = pesonetosoja
        patenteminsoja = pat2


def patmaxtrigo(pat2): # Patente del camion que más trigo descargo
    global pesonetotrigo, pesonetomaxtrigo, patentemaxtrigo

    if pesonetotrigo > pesonetomaxtrigo:
        pesonetomaxtrigo = pesonetotrigo
        patentemaxtrigo = pat2


def patmintrigo(pat2): # Patente del camion que menos trigo descargo
    global pesonetotrigo, pesonetomintrigo, patentemintrigo

    if pesonetotrigo < pesonetomintrigo:
        pesonetomintrigo = pesonetotrigo
        patentemintrigo = pat2


def patmaxcebada(pat2): # Patente del camion que más cebada descargo
    global pesonetocebada, pesonetomaxcebada, patentemaxcebada

    if pesonetocebada > pesonetomaxcebada:
        pesonetomaxcebada = pesonetocebada
        patentemaxcebada = pat2


def patmincebada(pat2): # Patente del camion que menos  descargo
    global pesonetocebada, pesonetomincebada, patentemincebada

    if pesonetocebada < pesonetomincebada:
        pesonetomincebada = pesonetocebada
        patentemincebada = pat2


def patmaxgirasol(pat2): # Patente del camion que más  girasoldescargo
    global pesonetogirasol, pesonetomaxgirasol, patentemaxgirasol

    if pesonetogirasol > pesonetomaxgirasol:
        pesonetomaxgirasol = pesonetogirasol
        patentemaxgirasol = pat2


def patmingirasol(pat2): # Patente del camion que menos  descargo
    global pesonetogirasol, pesonetomingirasol, patentemingirasol

    if pesonetogirasol < pesonetomingirasol:
        pesonetomingirasol = pesonetogirasol
        patentemingirasol = pat2
# -----------------------------------------------------------------------------------------------------
# Registrar Tara

def regisTara():
    global pesonetomaiz, pesonetosoja, pesonetotrigo, pesonetocebada, pesonetogirasol , pesonetomaiztotal, pesonetosojatotal, pesonetotrigototal, pesonetocebadatotal, pesonetogirasoltotal
    global pesoprommaiz, pesopromsoja, pesopromtrigo, pesopromcebada, pesopromgirasol
    pat1 = ''

    while (pat1 != 'V'):
        pat1 = input('Ingrese su numero de patente o V para salir: ')
        pat1 = pat1.upper()
        tipo = pat1.isalnum()    
        X = buscaSec(P, pat1)
        if (tipo == True and X == True):
            I = P.index(pat1)
            e = E[I]
            pb = Pb[I]
            t = T[I]
            pr = Pr[I]
            if(e == 'E' and pb!=0 and t == 0):
                pesotara = int(input('Porfavor ingrese el Peso de la Tara en Kg: '))
                T[I] = pesotara
                E[I] = 'C' 
                if (pr == 'M'):
                    pesonetomaiz = pb - pesotara
                    pesonetomaiztotal = pesonetomaiztotal + pesonetomaiz
                    pesoprommaiz = pesonetomaiztotal/ cantcammaiz
                    patmaxmaiz(pat1)
                    patminmaiz(pat1)             
                elif (pr == 'S'):
                    pesonetosoja = pb - pesotara
                    pesonetosojatotal = pesonetosojatotal + pesonetosoja
                    pesopromsoja = pesonetosojatotal/ cantcamsoja
                    patmaxsoja(pat1)
                    patminsoja(pat1)
                elif (pr == 'T'):
                    pesonetotrigo = pb - pesotara
                    pesonetotrigototal = pesonetotrigototal + pesonetotrigo
                    pesopromtrigo = pesonetotrigototal/ cantcamtrigo
                    patmaxtrigo(pat1)
                    patminsoja(pat1)
                elif (pr == 'C'):
                    pesonetocebada = pb - pesotara
                    pesonetocebadatotal = pesonetocebadatotal + pesonetocebada
                    pesopromcebada = pesonetocebadatotal/ cantcamcebada
                    patmaxcebada(pat1)
                    patmincebada(pat1)
                elif (pr == 'G'):
                    pesonetogirasol = pb - pesotara
                    pesonetogirasoltotal = pesonetogirasoltotal + pesonetogirasol
                    pesopromgirasol = pesonetogirasoltotal / cantcamgirasol
                    patmaxcebada(pat1)
                    patmincebada(pat1)
            elif(e == 'C' and pb!=0 and t != 0):
                print(f'Esta patente ya tiene una tara registrada de [{t}] Kg y su estado es [{e}]')
            else:
                print('Porfavor ingrese una patente valida')
        elif (tipo == True and X == False and pat1 == 'V'):
            os.system('cls')
        elif (tipo == True and X == False):
            print('Patente Inexistente, por favor ingrese una nueva patente')


# -----------------------------------------------------------------------------------------------------
# Registrar Peso Bruto

def regisPesoBruto():
    pat1 = ''
    while (pat1 != 'V'):
        pat1 = input('Ingrese su numero de patente o V para salir: ')
        pat1 = pat1.upper()
        tipo = pat1.isalnum()    
        X = buscaSec(P, pat1)
        if (tipo == True and X == True):
            I = P.index(pat1)
            e = E[I]
            pb = Pb[I]
            if (e == 'E' and pb == 0):
                pesobruto= int(input('Porfavor ingrese el Peso Bruto en Kg: '))
                Pb[I] = pesobruto
            elif(e == 'E' and pb != 0):
                print(f'Esta patente ya tiene un peso bruto registrado de [{pb}] Kg, porfavor ingrese a registrar Tara.')
            else:
                print(f'La patente ingresada tiene un estado [{e}] porfavor ingrese una patente valida.')
        elif (pat1 == 'V' and X == False and tipo == True):
            os.system('cls')
        elif (tipo == True and X == False):
            print('Patente Inexistente, por favor ingrese una nueva patente')


# -----------------------------------------------------------------------------------------------------
# Recepcion

def recepcion():
    global cantcam,cantcamcebada,cantcamgirasol,cantcamsoja,cantcamtrigo,cantcammaiz
    pat1 = ''
    produc = ''

    while (pat1 != 'V' and produc !='V'):
        pat1 = input('Ingrese su numero de patente o V para salir: ')
        pat1 = pat1.upper()
        tipo = pat1.isalnum()
        X = buscaSec(P, pat1)
        if (tipo == True and X == True):
            I = P.index(pat1)
            e = E[I]
            if e == 'P':
                print(f'La lista de productos disponibles es {Pr}')
                produc = str(input('Porfavor ingrese el producto de su camion o V para salir: '))
                produc = produc.upper()
                buscaProd = buscaSec(Pr, produc)
                if (buscaProd == True):
                    if produc == 'T':
                        E[I] = 'E'
                        cantcam +=1
                        cantcamtrigo +=1
                    elif produc == 'S':
                        E[I] = 'E'
                        cantcam +=1
                        cantcamsoja +=1
                    elif produc == 'M':
                        E[I] = 'E'
                        cantcam +=1
                        cantcammaiz +=1
                    elif produc == 'G':
                        E[I] = 'E'
                        cantcam +=1
                        cantcamgirasol +=1
                    elif produc == 'C':
                        E[I] = 'E'
                        cantcam +=1
                        cantcamcebada+=1
                else:
                    print('Porfavor ingrese uno de los productos previamente cargados')
            else:
                print(f'La patente fue encontrada en la posición {I} y su estado es {e}')
        elif (pat1 == 'V' or produc =='V' and X == False and tipo == True):
            os.system('cls')
        elif (tipo == True and X == False):
            print('Patente Inexistente, por favor ingrese una nueva patente')
            
        
# -----------------------------------------------------------------------------------------------------
# Entrega de Cupos

def entregaCupo():
    global l, pat, acumCupo

    print(P)
    print(C)
    print(E)
    
    while (acumCupo <=8):
        pat = input('Ingrese su patente o V para volver al menu: ')
        pat = pat.upper()
        if pat == 'V':
            break
        else:
            caracteres = len(pat)
            tipo = pat.isalnum()
            X = buscaSec(P, pat)
            if tipo == True and X == False and acumCupo <= 8:
                if caracteres > 7:
                        print('Ingrese una patente valida.')
                elif caracteres < 6:
                    print('Ingrese una patente valida.')
                else: 
                    P[l] = pat
                    C[l] = acumCupo
                    E[l] = 'P'
                    l +=1
                    acumCupo +=1
                    print(P)
                    print(C)
                    print(E)
            elif tipo == True and X == True:
                print('La patente ya ha sido ingresada, porfavor ingrese una nueva patente')
    else:
        print('No hay más cupos disponibles')
       
                    
            
# -----------------------------------------------------------------------------------------------------
# Menu Principal

def menuPrincipal():
    global opc, opcion

    while opc == True:
        while True:
            menuOP()
            try:
                opcion = int(input('Ingrese unas de las opciones 1/8 o ingrese 0 para salir: '))
            except ValueError:
                print('Por favor ingrese un número entero de las opciones\n')
            if (opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5 or opcion == 6 or opcion == 7 or opcion == 8 or opcion == 0):
                break
        if opcion == 4 or opcion == 6:
            menuOD() # Menu indicando que las funciones esta en desarollo
        elif opcion ==1:
            os.system('cls') # Borra la terminal
            Administracion() # Ingresa a Administración
            opc = True
        elif opcion == 2:  
            os.system('cls') # Borra la terminal
            entregaCupo()
            opc = True
        elif opcion == 3:
            os.system('cls') # Borra la terminal
            recepcion() 
        elif opcion == 5:
            os.system('cls') # Borra la terminal
            regisPesoBruto() 
        elif opcion == 7:
            os.system('cls') # Borra la terminal
            regisTara() 
        elif opcion == 8:
            os.system('cls')
            reportes()
        elif opcion == 0:
            opc = False


# -----------------------------------------------------------------------------------------------------

    
#main
menuPrincipal()

