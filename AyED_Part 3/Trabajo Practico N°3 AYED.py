import os, pickle, os.path,sys,datetime,io
from datetime import date
from datetime import datetime
from colorama import init, Fore, Back, Style

class Productos():

    def __init__(self):
        self.Cod = -1
        self.Prod= ''
        self.Estado= 'A'
    
    def Alta(self):
        tmp=self.Busqueda(self.Cod,'Cod','')
        if(tmp=='I'):
            self.Busqueda(self.Cod,'Cod','A')
            return 1
        elif(tmp=='A'):
            return -1
        elif(tmp==-1):
            self.Formateo()
            pickle.dump(self, ArcLogProd)
            ArcLogProd.flush()
            return 1
    
    def Formateo(self):
        self.Prod = str(self.Prod)
        self.Prod = self.Prod.ljust(7, ' ')
        self.Estado = str(self.Estado)
        self.Estado = self.Estado.ljust(1)
        self.Cod = str(self.Cod)
        self.Cod = self.Cod.ljust(1)

    def Busqueda(self,p,x,e): # p= Lo que tiene que buscar / x= Si es 'Cod' o 'Prod' y e=Estado, se usa para cambiar u validar un estado
        global ArcLogProd

        t=os.path.getsize(ArcFisiProd)
        ArcLogProd.seek(0)
        while ArcLogProd.tell() < t:
            Puntero=ArcLogProd.tell()
            self=pickle.load(ArcLogProd)
            if(x=='Prod'):
                if(self.Prod.strip()==p):
                    if(e!=''):
                        self.Estado=e
                        self.Formateo()
                        ArcLogProd.seek(Puntero,0)
                        pickle.dump(self, ArcLogProd)
                        ArcLogProd.flush()
                    return self.Estado
            elif(x=='Cod'):
                if(self.Cod==p):
                    if(e!=''):
                        self.Estado=e
                        self.Formateo()
                        ArcLogProd.seek(Puntero,0)
                        pickle.dump(self, ArcLogProd)
                        ArcLogProd.flush()
                        return Puntero
                    else:
                        return self.Estado
        return -1

    def Valida_cod(self):
        Cod=input(f"[V - Para volver al menú anterior] Ingrese el código del producto a seleccionar: {Style.RESET_ALL}").upper()
        while (ValidarEnteros(Cod, 1, 5)) and (Cod!='V'):
            Cod=input(f"{Fore.CYAN+Style.BRIGHT}[V - Para volver al menú anterior] {Fore.RED+Style.BRIGHT} Error, el producto que seleccionó no es válido. <Intentelo nuevamente>: {Style.RESET_ALL}").upper()
        if(Cod=='V'):
            return Cod
        if(Cod == '1'):
            self.Prod='CEBADA'
        elif(Cod == '2'):
            self.Prod='GIRASOL'
        elif(Cod == '3'):
            self.Prod='MAÍZ'
        elif(Cod == '4'):
            self.Prod='SOJA'
        elif(Cod == '5'):
            self.Prod='TRIGO'
        self.Cod= str(Cod)

class Cupo():

    def __init__(self):
        self.Patente = ''
        self.Fecha_Cupo = ''
        self.Estado = ''
        self.Cod = -1
        self.Bruto = 0
        self.Tara= 0
    
    def Formateo_Cupo(self):
        self.Patente = str(self.Patente)
        self.Patente = self.Patente.ljust(7, ' ')
        self.Estado = str(self.Estado)
        self.Estado = self.Estado.ljust(1)
        self.Cod = str(self.Cod)
        self.Cod = self.Cod.ljust(1)
        self.Bruto = str(self.Bruto)
        self.Bruto = self.Bruto.ljust(5, ' ')
        self.Tara = str(self.Tara)
        self.Tara = self.Tara.ljust(5, ' ')
        if(isinstance(self.Fecha_Cupo,str)==False):
            self.Fecha_Cupo=self.Fecha_Cupo.strftime("%d/%m/%Y")
            self.Fecha_Cupo = self.Fecha_Cupo.ljust(12, ' ')

    def Busqueda_Cupos(self,Pat,Fecha_Cupo,Estado1,Estado2):
        global ArcFisiOp, ArcLogOp, Puntero

        t=os.path.getsize(ArcFisiOp)
        ArcLogOp.seek(0)
        while ArcLogOp.tell() < t:
            Puntero=ArcLogOp.tell()
            self=pickle.load(ArcLogOp)
            if(self.Patente.strip()==Pat):
                Fecha=datetime.strptime(self.Fecha_Cupo.strip(), "%d/%m/%Y")
                if(Fecha==Fecha_Cupo):
                    if(Estado1==''):
                        return -1 # Hay otro camión cargado
                    else:
                        if(self.Estado==Estado1):
                            if(Estado2!=''):
                                self.Estado=Estado2
                                self.Formateo_Cupo()
                                ArcLogOp.seek(Puntero,0)
                                pickle.dump(self, ArcLogOp)
                                ArcLogOp.flush()
                                return 2 # Todo ok y cambiado
                            else:
                                return 1 # Estado y fecha validados
                        else:
                            return -3 # Existe pero no es del estado que fue pasado como parametro
        return -2
    
    def Rechazados(self,Fecha_Dada):

        t=os.path.getsize(ArcFisiOp)
        ArcLogOp.seek(0)
        Lista_pat=[]
        while ArcLogOp.tell() < t:
            Puntero=ArcLogOp.tell()
            self=pickle.load(ArcLogOp)
            Fecha=datetime.strptime(self.Fecha_Cupo.strip(), "%d/%m/%Y")
            if(Fecha==Fecha_Dada) and (self.Estado=='R'):
                Lista_pat.append(self.Patente.strip())
        return Lista_pat
   
    def Conteo(self):
        global CantCupos,CantRec,ContCebada,ContGirasol,ContMaiz,ContSoja,ContTrigo,MayorDescCeb,MenorDescCeb,MayorDescGir,MenorDescGir,MayorDescMaiz,MenorDescMaiz,MayorDescSoja,MenorDescSoja,MayorDescTrigo,MenorDescTrigo,MenorDescTrigo,PromCamCeb,PromCamGir,PromCamMaiz,PromCamSoja,PromCamTrigo,AcumCeb,AcumGir,AcumMaiz,AcumSoja,AcumTrigo,PatMayCeb,PatMenCeb,PatMayGir,PatMenGir,PatMayMaiz,PatMenMaiz,PatMaySoja,PatMenSoja,PatMayTrigo,PatMenTrigo

        t=os.path.getsize(ArcFisiOp)
        ArcLogOp.seek(0)
        PatMayCeb = 'No fue cargado'
        PatMenCeb = 'No fue cargado'
        PatMayGir = 'No fue cargado'
        PatMenGir = 'No fue cargado'
        PatMayMaiz = 'No fue cargado'
        PatMenMaiz = 'No fue cargado'
        PatMaySoja = 'No fue cargado'
        PatMenSoja = 'No fue cargado'
        PatMayTrigo = 'No fue cargado'
        PatMenTrigo = 'No fue cargado'
        CantCupos=0
        CantRec=0
        ContCebada=0
        ContGirasol=0
        ContMaiz=0
        ContSoja=0
        ContTrigo=0
        MayorDescCeb=0
        MayorDescGir=0
        MayorDescMaiz=0
        MayorDescSoja=0
        MayorDescTrigo=0
        PromCamCeb=0
        PromCamGir=0
        PromCamMaiz=0
        PromCamSoja=0
        PromCamTrigo=0
        AcumCeb=0
        AcumGir=0
        AcumMaiz=0
        AcumSoja=0
        AcumTrigo=0
        while ArcLogOp.tell() < t:
            self=pickle.load(ArcLogOp)
            if(self.Estado!=''):
                CantCupos+=1
                if(self.Estado!='P'):
                    CantRec+=1
                    if(self.Estado=='R'):
                        pass
                    else:
                        if(self.Cod=='1'):
                            PnCamCeb= int(self.Bruto) - int(self.Tara)
                            AcumCeb=AcumCeb + PnCamCeb
                            ContCebada+=1
                            if(ContCebada==1):
                                MenorDescCeb= PnCamCeb
                                MayorDescCeb= PnCamCeb
                                PatMayCeb=self.Patente.strip()
                                PatMenCeb=self.Patente.strip()
                            else:
                                if(PnCamCeb<MenorDescCeb):
                                    MenorDescCeb= PnCamCeb
                                    PatMenCeb=self.Patente.strip()
                                if(PnCamCeb>MayorDescCeb):
                                    MayorDescCeb= PnCamCeb
                                    PatMayCeb=self.Patente.strip()
                        elif(self.Cod=='2'):
                            PnCamGir= int(self.Bruto) - int(self.Tara)
                            AcumGir=AcumGir + PnCamGir
                            ContGirasol+=1
                            if(ContGirasol==1):
                                MenorDescGir= PnCamGir
                                MayorDescGir= PnCamGir
                                PatMayGir=self.Patente.strip()
                                PatMenGir=self.Patente.strip()
                            else:
                                if(PnCamGir<MenorDescGir):
                                    MenorDescGir= PnCamGir
                                    PatMenGir=self.Patente.strip()
                                if(PnCamGir>MayorDescGir):
                                    MayorDescGir= PnCamGir
                                    PatMayGir=self.Patente.strip()
                        elif(self.Cod=='3'):
                            PnCamMaiz= int(self.Bruto) - int(self.Tara)
                            AcumMaiz=AcumMaiz + PnCamMaiz
                            ContMaiz+=1
                            MenorDescMaiz= PnCamMaiz
                            if(ContMaiz==1):
                                MenorDescMaiz= PnCamMaiz
                                MayorDescMaiz= PnCamMaiz
                                PatMayMaiz=self.Patente.strip()
                                PatMenMaiz=self.Patente.strip()
                            else:
                                if(PnCamMaiz<MenorDescMaiz):
                                    MenorDescMaiz= PnCamMaiz
                                    PatMenMaiz=self.Patente.strip()
                                if(PnCamMaiz>MayorDescMaiz):
                                    MayorDescMaiz= PnCamMaiz
                                    PatMayMaiz=self.Patente.strip()
                        elif(self.Cod=='4'):
                            PnCamSoja= int(self.Bruto) - int(self.Tara)
                            AcumSoja=AcumSoja + PnCamSoja
                            ContSoja+=1
                            if(ContSoja==1):
                                MenorDescSoja= PnCamSoja
                                MayorDescSoja= PnCamSoja
                                PatMaySoja=self.Patente.strip()
                                PatMenSoja=self.Patente.strip()
                            else:
                                if(PnCamSoja<MenorDescSoja):
                                    MenorDescSoja= PnCamSoja
                                    PatMenSoja=self.Patente.strip()
                                if(PnCamSoja>MayorDescSoja):
                                    MayorDescSoja= PnCamSoja
                                    PatMaySoja=self.Patente.strip()
                        elif(self.Cod=='5'):
                            PnCamTrigo= int(self.Bruto) - int(self.Tara)
                            AcumTrigo= AcumTrigo + PnCamTrigo
                            ContTrigo+=1
                            if(ContTrigo==1):
                                MenorDescTrigo= PnCamTrigo
                                MayorDescTrigo= PnCamTrigo
                                PatMayTrigo=self.Patente.strip()
                                PatMenTrigo=self.Patente.strip()
                            else:
                                if(PnCamTrigo<MenorDescTrigo):
                                    MenorDescTrigo= PnCamTrigo
                                    PatMenTrigo=self.Patente.strip()
                                if(PnCamTrigo>MayorDescTrigo):
                                    MayorDescTrigo= PnCamTrigo
                                    PatMayTrigo=self.Patente.strip()
        if(ContCebada!=0):
            PromCamCeb=AcumCeb/ContCebada
        if(ContGirasol!=0):
            PromCamGir=AcumGir/ContGirasol
        if(ContMaiz!=0):
            PromCamMaiz=AcumMaiz/ContMaiz
        if(ContSoja!=0):
            PromCamSoja=AcumSoja/ContSoja
        if(ContTrigo!=0):
            PromCamTrigo=AcumTrigo/ContTrigo

class Rubros():

    def __init__(self):
        self.CodR = -1
        self.Nombre = ''
    
    def Val_nombre(self):
        
        Nom=str(input(Fore.CYAN+Style.BRIGHT+'\n[V- Para volver al menú anterior] <Hasta 30 carácteres> Ingrese el nombre del rubro: ').capitalize())
        Carac=len(Nom)
        if(Nom=='V') or (Carac<30):
            return Nom
        else:
            os.system("cls")
            return True  

    def Alta(self,NombreR,CodR):
        pos=self.Busqueda(NombreR,CodR)
        if(pos==-1):
            ArcLogRubros.seek(0,2)
            self.Nombre=NombreR
            self.CodR=CodR
            self.Formateo()
            pickle.dump(self, ArcLogRubros)
            ArcLogRubros.flush()
            Ordenamiento()
            return -1 # No están en uso
        elif(pos==1):
            return 1 # Ya está cargado exactamente igual
        elif(pos==2):
            return 2 # Código en uso
        elif(pos==3):
            return 3 # Nombre en uso

    def Listado(self):

        os.system("cls")
        t = os.path.getsize(ArcFisiRubros)
        if t==0:
            input("[Enter para volver al menú anterior] - No hay productos cargados!")
        else:
            ArcLogRubros.seek(0,0)
            print("+--------------------+----------+")
            print("|Rubro               |Código    |")
            print("+--------------------+----------+")
            while ArcLogRubros.tell() < t:
                self=pickle.load(ArcLogRubros)
                Rubro = self.Nombre.strip()
                CodR = self.CodR.strip()
                Muestra = "|{:<20}|{:>10}|".format(Rubro, CodR)
                print(Muestra)
                print("+--------------------+----------+")

    def Formateo(self):
        self.Nombre = str(self.Nombre)
        self.Nombre = self.Nombre.ljust(30, ' ')
        self.CodR = str(self.CodR)
        self.CodR = self.CodR.ljust(1)

    def Busqueda(self,Nom,Cod):
        global ArcFisiRubros, Puntero
        t=os.path.getsize(ArcFisiRubros)
        ArcLogRubros.seek(0)
        while ArcLogRubros.tell() < t:
            Puntero=ArcLogRubros.tell()
            self=pickle.load(ArcLogRubros)
            if(self.CodR.strip() == Cod):
                if(self.Nombre.strip() == Nom):
                    return 1 # Nombre y código usados
                else:
                    return 2 # Código usado
            elif(self.Nombre.strip() == Nom):
                return 3 # Nombre usado

        return -1 #No hay coincidencias

    def Dico(self,CodR):
        CodR=int(CodR)
        ArcLogRubros.seek(0, 0)
        aux = pickle.load(ArcLogRubros)
        tamReg = ArcLogRubros.tell()
        cantReg = int(os.path.getsize(ArcFisiRubros) / tamReg)
        inferior = 0
        superior = cantReg-1
        medio = (inferior + superior) // 2
        ArcLogRubros.seek(medio*tamReg, 0)
        self = pickle.load(ArcLogRubros)
        while int(self.CodR) != CodR and (inferior < superior):
            if CodR < int(self.CodR):
                superior = medio - 1
            else:
                inferior = medio + 1
            medio = (inferior + superior) // 2
            ArcLogRubros.seek(medio*tamReg, 0)
            self = pickle.load(ArcLogRubros)
        if int(self.CodR) == CodR:
            return medio*tamReg
        else:
            return -1

class Silos():
    
    def __init__(self):
        self.CodS= 0
        self.Nombre=''
        self.CodP=0
        self.Stock=0

    def MayorStock(self):
        t=os.path.getsize(ArcFisiSilos)
        ArcLogSilos.seek(0)
        Acum=0
        MayorStock=''
        while ArcLogSilos.tell() < t:
            Puntero=ArcLogSilos.tell()
            self=pickle.load(ArcLogSilos)
            Stock=int(self.Stock.strip())
            if(Stock>Acum):
                Acum=Stock
                MayorStock=self.Nombre.strip()
        return MayorStock

    def Busqueda(self,CodS,CodP):
        global ArcFisiSilos, Puntero

        t=os.path.getsize(ArcFisiSilos)
        ArcLogSilos.seek(0)
        while ArcLogSilos.tell() < t:
            Puntero=ArcLogSilos.tell()
            self=pickle.load(ArcLogSilos)
            if(self.CodS.strip() == CodS):
                return self.Nombre # Código de silo usado
            elif(self.CodP==CodP):
                return 1 # Ya hay un silo con ese CodP

        return -1 #No hay coincidencias
    
    def Formateo(self):
        self.CodS = str(self.CodS)
        self.CodS = self.CodS.ljust(1)
        self.CodP = str(self.CodP)
        self.CodP = self.CodP.ljust(1)
        self.Stock = str(self.Stock)
        self.Stock = self.Stock.ljust(5)
        self.Nombre = str(self.Nombre)
        self.Nombre = self.Nombre.ljust(13, ' ')

class RubrosxProd(): # Revisar que esté bien
    
    def __init__(self):
        self.CodR = 0
        self.CodP = 0
        self.ValMin = 0.0
        self.ValMax = 100.0
    
    def Formateo_Rubrosxprod(self):

        self.CodR = str(self.CodR)
        self.CodR = self.CodR.ljust(1)
        self.CodP = str(self.CodP)
        self.CodP = self.CodP.ljust(1)
        self.ValMin = str(self.ValMin)
        self.ValMin = self.ValMin.ljust(5)
        self.ValMax = str(self.ValMax)
        self.ValMax = self.ValMax.ljust(5)

    def Busqueda(self,CodP,CodR):
        t=os.path.getsize(ArcFisiRubrosXProd)
        ArcLogRubrosXProd.seek(0,0)
        while ArcLogRubrosXProd.tell() < t:
            Puntero=ArcLogRubrosXProd.tell()
            self=pickle.load(ArcLogRubrosXProd)
            if(self.CodR.strip() == CodR):
                if(self.CodP.strip() == CodP):
                    return 1 #Existe
        return -1 #No existe

def ValidarEnteros(nro, min, max):
    try:
        nro = int(nro)
        if nro >= min and nro <= max:
            return False
        else:
            return True
    except:
        return True

def ValidarPat():
    print(f'''{Fore.CYAN+Style.BRIGHT}-------------INGRESE LA PATENTE DEL VEHÍCULO-------------
{Fore.RED+Style.BRIGHT}<Debe ser alfanumérica y tener entre 6 y 7 carácteres>
{Fore.CYAN+Style.BRIGHT}---------------------------------------------------------{Style.RESET_ALL}''')
    Patente=str(input(Fore.CYAN+Style.BRIGHT+'\nPatente del vehículo [V- Para volver al menú anterior]: ').upper())
    Carac=len(Patente)
    if(Patente=='V') or ((Patente.isalnum()==True) and (Carac==6) or (Carac==7)):
        return Patente
    else:
        os.system("cls")
        return True

def Pantalla():
	os.system('cls')
	print(f'''{Fore.CYAN+Style.BRIGHT}---------------MENÚ PRINCIPAL---------------''')
	print(f'''{Style.RESET_ALL}\n 1- Administraciones
 2- Entrega de cupos
 3- Recepción
 4- Registrar calidad
 5- Registrar peso bruto
 6- Registrar descarga
 7- Registrar tara
 8- Reportes
 9- Listado de silos y rechazos
 0- Fin del programa
{Fore.CYAN+Style.BRIGHT}--------------------------------------------{Style.RESET_ALL}''')

def Pantalla_Admin():
    os.system('cls')
    print(f'{Fore.CYAN+Style.BRIGHT}------------MENÚ ADMINISTRACIONES------------')
    print(f'''{Style.RESET_ALL}\nA- Titulares
B- Productos
C- Rubros
D- Rubros por producto
E- Silos
F- Sucursales
G- Producto por titular
V- Volver al MENU PRINCIPAL

{Fore.CYAN+Style.BRIGHT}---------------------------------------------{Style.RESET_ALL}''')

def Inicializar():
    global ArcFisiProd, ArcLogOp, ArcFisiOp, ArcLogRubros, ArcFisiRubros, ArcLogRubrosXProd, ArcFisiRubrosXProd, ArcLogSilos, ArcFisiSilos, ArcLogProd, Fecha_Actual

    init(autoreset=True)
    now=datetime.now()
    Fecha=(f"{now.day}/{now.month}/{now.year}")
    Fecha_Actual = datetime.strptime(Fecha, "%d/%m/%Y")
    ArcFisiOp = 'D:\Archivos_tp\OPERACIONES.DAT'
    if not os.path.exists(ArcFisiOp):
        ArcLogOp = open(ArcFisiOp, "w+b")
    else:
        ArcLogOp = open(ArcFisiOp, "r+b")
    
    ArcFisiProd = 'D:\Archivos_tp\PRODUCTOS.DAT'
    if not os.path.exists(ArcFisiProd):
        ArcLogProd = open(ArcFisiProd, "w+b")
    else:
        ArcLogProd = open(ArcFisiProd, "r+b")

    ArcFisiRubros = 'D:\Archivos_tp\RUBROS.DAT'
    if not os.path.exists(ArcFisiRubros):
        ArcLogRubros = open(ArcFisiRubros, "w+b")
    else:
        ArcLogRubros = open(ArcFisiRubros, "r+b")

    ArcFisiRubrosXProd = 'D:\Archivos_tp\RUBROS-X-PRODUCTOS.DAT'
    if not os.path.exists(ArcFisiRubrosXProd):
        ArcLogRubrosXProd = open(ArcFisiRubrosXProd, "w+b")
    else:
        ArcLogRubrosXProd = open(ArcFisiRubrosXProd, "r+b")
    
    ArcFisiSilos = 'D:\Archivos_tp\SILOS.DAT'
    if not os.path.exists(ArcFisiSilos):
        ArcLogSilos = open(ArcFisiSilos, "w+b")
    else:
        ArcLogSilos = open(ArcFisiSilos, "r+b")

    Menu()

def Menu():
    global ArcLogOp, ArcLogRubros, ArcLogRubrosXProd, ArcLogSilos

    os.system("cls")
    Opc = -1
    while (Opc != 0):
        os.system("cls")
        Pantalla()
        Opc=input(Fore.CYAN+Style.BRIGHT+'\nIngrese la opción que desea operar: ')
        while (ValidarEnteros(Opc, 0, 9)):
            Opc = input(Fore.RED+Style.BRIGHT+'Opción incorrecta - Entre 0 y 9: ')
        Opc = int(Opc)
        if (Opc == 1):
            Administraciones()
        elif (Opc == 2):
            Cupos()
        elif (Opc == 3):
            Recepción()
        elif (Opc == 4):
            Calidad()
        elif (Opc == 5):
            Peso_bruto()
        elif (Opc == 6):
            print('Proceso en construcción')
            input('<Enter para volver al menú principal>')
        elif (Opc == 7):
            Tara()
        elif (Opc == 8):
            Reportes()
        elif (Opc == 9):
            Listado()
        else:
            print(Style.RESET_ALL+'')
            print('¿Está seguro de que desea salir del programa?')
            print(Fore.RED+Style.BRIGHT+'\nRecuerde que esta acción NO se puede deshacer')
            print('S- Salir')
            print('C- Cancelar')
            Confirmación=str(input(Style.RESET_ALL+'').upper())
            while(Confirmación!='S' and Confirmación!='C'):
                print('')
                print(Fore.RED+Style.BRIGHT+'Opción incorrecta, intentalo nuevamente: ')
                Confirmación=str(input().upper())
            if(Confirmación=='S'):
                ArcLogOp.close()
                ArcLogRubros.close()
                ArcLogRubrosXProd.close()
                ArcLogSilos.close()
                input(Fore.CYAN+Style.BRIGHT+'\nGracias por usar este programa!')
            elif(Confirmación=='C'):
                Opc=-1

def Administraciones():
    
    Opci = ''
    while (Opci.upper() != 'V'):
        os.system("cls")
        Pantalla_Admin()
        Opci=str(input(Fore.CYAN+Style.BRIGHT+'\nIngrese la opción que desea operar: ').upper())
        while(Opci<'A' or Opci>'G') and (Opci!='V'):
            Opci = str(input(Fore.RED+Style.BRIGHT+'Opción incorrecta - Entre A y G [V para Volver]: ').upper())
        if(Opci == 'A') or (Opci == 'F') or (Opci == 'G'):
            print(Fore.RED+Style.BRIGHT+'Esta funcionalidad se encuentra en construcción!')
            Opci=input('V para volver: ').upper()
        elif(Opci == 'B'):
            Sub_menu_admin()
        elif(Opci == 'C'):
            Alta_rubro()
        elif(Opci == 'D'):
            Asign_rub()
        elif(Opci == 'E'):
            Alta_silo()

def Alta_rubro(): # Agregar bajas y modificaciones si queremos mejorarlo
    Opci=''
    while(Opci!='V'):
                os.system("cls")
                print(f'''{Fore.CYAN+Style.BRIGHT}----------------------------------
OPCION C - Alta de un rubro
----------------------------------{Style.RESET_ALL}''')
                Reg=Rubros()
                CodR=input("<Valor entero de hasta 2 cifras> - ¿Qué código desea asignarle al rubro?: ")
                while(ValidarEnteros(CodR,0,99)):
                    CodR=input("<Valor entero de hasta 2 cifras> - ¿Qué código desea asignarle al rubro?: ").upper()
                Nom=Reg.Val_nombre()
                while(Nom==True):
                    Nom=Reg.Val_nombre()
                if(Nom=='V'):
                    Opci='V'
                else:
                    res=Reg.Alta(Nom,CodR)
                    if(res==-1):
                        print()
                        print("Rubro cargado correctamente!")
                    elif(res==2):
                        ArcLogRubros.seek(Puntero,0)
                        Reg=pickle.load(ArcLogRubros)
                        print(f"El código que elegiste ya fue utilizado en el rubro \"{Reg.Nombre.strip()}\"")
                    elif(res==1) or (res==3):
                        print("El rubro que intentas cargar ya existe!")
                        input("<Enter para volver al menú anterior>")
                    print()
                    Confir=input("¿Desea cargar otro rubro? Y/N: ").upper()
                    while(Confir!='Y') and (Confir!='N'):
                        Confir=input("¿Desea cargar otro rubro? Y/N: ").upper()
                    if(Confir=='N'):
                        Opci='V'

def Asign_rub(): # Agregar bajas y modificaciones si queremos mejorarlo

    Opci=''
    while(Opci!='V'):
                os.system("cls")
                print(f'''{Fore.CYAN+Style.BRIGHT}----------------------------------
OPCION D - Asignación de un rubro a un producto
----------------------------------{Style.RESET_ALL}''')
                print()
                Reg=RubrosxProd()
                ArcLogRubrosXProd.seek(0)
                RegRub=Rubros()
                RegRub.Listado()
                print()
                CodR=input("Ingrese el código del rubro que desea asignar a un producto: ")
                if(CodR=='V'):
                    Opci='V'
                else:
                    res=RegRub.Busqueda('',CodR)
                    while(res==-1):
                        os.system("cls")
                        RegRub.Listado()
                        print()
                        CodR=input("El código ingresado no le pertenece a ningún rubro, inténtelo nuevamente: ")
                        res=RegRub.Busqueda('',CodR)
                    os.system("cls")
                    Listado_total()
                    print()
                    ArcLogRubros.seek(Puntero,0)
                    RegRub=pickle.load(ArcLogRubros)
                    print(f"A qué producto quiere asignarle el rubro {Fore.CYAN+Style.BRIGHT}\"{RegRub.Nombre.strip()}\"{Style.RESET_ALL}?: ")
                    print()
                    Producto=Productos()
                    Cod=Producto.Valida_cod()
                    if(Cod!='V'):
                        res=Reg.Busqueda(Producto.Cod,CodR)
                        if(res==1):
                            os.system("cls")
                            print(f"El rubro {Fore.CYAN+Style.BRIGHT}{RegRub.Nombre.strip()}{Style.RESET_ALL} ya fue asignado a {Fore.CYAN+Style.BRIGHT}{Producto.Prod}{Style.RESET_ALL}!")
                            input("<Enter para volver al menú anterior>")
                            Opci='V'
                        elif(res==-1):
                            os.system("cls")
                            Reg.CodP=Producto.Cod
                            Reg.CodR=CodR
                            print()
                            print(f"{Fore.CYAN+Style.BRIGHT}\"{RegRub.Nombre.strip()}\"{Style.RESET_ALL} esperará una respuesta de {Fore.CYAN+Style.BRIGHT}\"sí o no\"{Style.RESET_ALL} o un {Fore.CYAN+Style.BRIGHT}valor numérico{Style.RESET_ALL}?")
                            print(f"{Fore.CYAN+Style.BRIGHT}\"S\"{Style.RESET_ALL} para sí o no")
                            print(f"{Fore.CYAN+Style.BRIGHT}\"N\"{Style.RESET_ALL} para un valor numérico")
                            print()
                            tmp=input("").upper()
                            while(tmp!='S') and (tmp!='N'):
                                tmp=input("").upper()
                            if(tmp=='N'): # Num
                                os.system("cls")
                                ValMin=input(f"[De 0 a 100] - Ingrese el valor {Fore.RED+Style.BRIGHT}mínimo {Style.RESET_ALL}que aceptará ese rubro: ")
                                while(ValidarFloats(ValMin,0,100)):
                                    ValMin=input(f"[De 0 a 100] - Ingrese el valor {Fore.RED+Style.BRIGHT}mínimo {Style.RESET_ALL}que aceptará ese rubro: ")
                                Reg.ValMin=ValMin
                                print()
                                ValMax=input(f"[De {ValMin} a 100] - Ingrese el valor {Fore.RED+Style.BRIGHT}máximo {Style.RESET_ALL}que aceptará ese rubro: ")
                                while(ValidarFloats(ValMax,float(ValMin),100)):
                                    ValMax=input(f"[De {ValMin} a 100] - Ingrese el valor {Fore.RED+Style.BRIGHT}máximo {Style.RESET_ALL}que aceptará ese rubro: ")
                                Reg.ValMax=ValMax
                                os.system("cls")
                                print(f'''El rubro {Fore.CYAN+Style.BRIGHT}{RegRub.Nombre.strip()}{Style.RESET_ALL} ha sido asignado correctamente al producto {Fore.CYAN+Style.BRIGHT}{Producto.Prod}!{Style.RESET_ALL}
Aceptará valores entre {Fore.CYAN+Style.BRIGHT}{ValMin} {Style.RESET_ALL}y {Fore.CYAN+Style.BRIGHT}{ValMax}.
{Style.RESET_ALL}''')
                            else: # BOOLEANA
                                os.system("cls")
                                print(f"El producto será válido en caso de recibir una respuesta de sí o de no?{Fore.CYAN+Style.BRIGHT} S/N{Style.RESET_ALL}")
                                tmp=input().upper()
                                while(tmp!='S') and (tmp!='N'):
                                    print(f"El producto será válido en caso de recibir una respuesta de sí o de no?{Fore.CYAN+Style.BRIGHT} S/N{Style.RESET_ALL}")
                                    tmp=input().upper()
                                if(tmp=='N'):
                                    Reg.ValMax=0
                                    Reg.ValMin=-1
                                    os.system("cls")
                                    print(f'''El rubro {Fore.CYAN+Style.BRIGHT}{RegRub.Nombre.strip()}{Style.RESET_ALL} ha sido asignado correctamente al producto {Fore.CYAN+Style.BRIGHT}{Producto.Prod}!{Style.RESET_ALL}
Será aceptado en caso de recibir {Fore.CYAN+Style.BRIGHT}'No' {Style.RESET_ALL}y rechazado en caso de recibir {Fore.CYAN+Style.BRIGHT}'Sí'.
{Style.RESET_ALL}''')
                                else:
                                    Reg.ValMax=1
                                    Reg.ValMin=-1
                                    os.system("cls")
                                    print(f'''El rubro {Fore.CYAN+Style.BRIGHT}{RegRub.Nombre.strip()}{Style.RESET_ALL} ha sido asignado correctamente al producto {Fore.CYAN+Style.BRIGHT}{Producto.Prod}!{Style.RESET_ALL}
Será aceptado en caso de recibir {Fore.CYAN+Style.BRIGHT}'Sí' {Style.RESET_ALL}y rechazado en caso de recibir {Fore.CYAN+Style.BRIGHT}'No'.
{Style.RESET_ALL}''')
                            Reg.Formateo_Rubrosxprod()
                            ArcLogRubrosXProd.seek(0,2)
                            pickle.dump(Reg,ArcLogRubrosXProd)
                            ArcLogRubrosXProd.flush()
                            Opci=''
                            while(Opci!='V') and (Opci!='S'):
                                print(f'''
{Fore.CYAN+Style.BRIGHT}¿Qué desea hacer a continuación?

\'S\' para seguir
\'V\' para volver al menú anterior
{Style.RESET_ALL}''')
                                Opci=input("Ingrese una opción: ").upper()

def Alta_silo(): # Agregar bajas y modificaciones si queremos mejorarlo
    Opci=''
    while(Opci!='V'):
        os.system("cls")
        print(f'''{Fore.CYAN+Style.BRIGHT}----------------------------------
OPCION E - Alta de un silo
----------------------------------{Style.RESET_ALL}''')
        print('¿Qué producto almacenará el silo?')
        print()
        Listado_total()
        Producto=Productos()
        Silo=Silos()
        print()
        Opci=Producto.Valida_cod()
        if(Opci!='V'):
            tmp=Silo.Busqueda('',Producto.Cod)
            if(tmp==-1):
                Silo.Nombre=(f"Silo {Producto.Prod.capitalize()}")
                CodS=input(f"<Valor entero de hasta 2 cifras> - ¿Qué código desea asignarle a \"{Silo.Nombre}\"?: ")
                while(ValidarEnteros(CodS,0,99)):
                    CodS=input("<Valor entero de hasta 2 cifras> - ¿Qué código desea asignarle al silo?: ").upper()
                tmp=Silo.Busqueda(CodS,Producto.Cod)
                while(tmp!=-1):
                    print(f"El código seleccionado ya ha sido utilizado para \"{tmp.strip()}\".")
                    CodS=input(f"<Valor entero de hasta 2 cifras> - ¿Qué código desea asignarle a \"{Silo.Nombre}\"?: ")
                    while(ValidarEnteros(CodS,0,99)):
                        CodS=input("<Valor entero de hasta 2 cifras> - ¿Qué código desea asignarle al silo?: ").upper()
                    tmp=Silo.Busqueda(CodS,Producto.Cod)
                Silo.CodS=CodS
                Silo.CodP=Producto.Cod
                Silo.Formateo()
                ArcLogSilos.seek(0,2)
                pickle.dump(Silo,ArcLogSilos)
                ArcLogSilos.flush()
                print()
                print("Silo cargado correctamente!")
            elif(tmp==1):
                print("Ya hay un silo para ese producto!")
            print()
            Confir=input("¿Desea cargar otro silo? Y/N: ").upper()
            while(Confir!='Y') and (Confir!='N'):
                Confir=input("¿Desea cargar otro silo? Y/N: ").upper()
            if(Confir=='N'):
                Opci='V'

def Sub_menu_admin():
    global ArcFisiProd
    
    Opci=''
    while(Opci!='V'):
        os.system('cls')
        print(f'''{Fore.CYAN+Style.BRIGHT}--------------SUBMENÚ PRODUCTOS--------------
{Style.RESET_ALL}\nA- ALTA
B- BAJA
C- CONSULTA
M- MODIFICACION
V- VOLVER AL MENU ANTERIOR

{Fore.CYAN+Style.BRIGHT}---------------------------------------------
''')
        Opci=str(input().upper())
        while(Opci!='A') and (Opci!='B') and (Opci!='C') and (Opci!='M') and (Opci!='V'):
            Opci=input("[V Para volver al menú anterior] - Error, ingrese una opción válida: ").upper()
        if(Opci == 'A'):
            Alta_prod()
        elif(Opci == 'B'):
            Baja_prod()
        elif(Opci == 'C'):
            print(f'''{Fore.CYAN+Style.BRIGHT}------------------------------
OPCION C - Consulta de productos
------------------------------{Style.RESET_ALL}''')
            Consulta_Prod()
            input('<Enter para volver al menú anterior>')
        elif(Opci == 'M'):
            Modificar_prod()

def ValidarFloats(nro, min, max):
    try:
        nro = float(nro)
        if nro >= min and nro <= max:
            return False
        else:
            return True
    except:
        return True

def Listado_total():

    Productos = [
    {
        "Producto": "CEBADA",
        "Código": "1",
    },
    {
        "Producto": "GIRASOL",
        "Código": "2",
    },
    {
        "Producto": "MAÍZ",
        "Código": "3",
    },    {
        "Producto": "SOJA",
        "Código": "4",
    },    {
        "Producto": "TRIGO",
        "Código": "5",
    },
]

    print("+--------------------+----------+")
    print("|Producto            |Código    |")
    print("+--------------------+----------+")
    for p in Productos:
        Producto = p["Producto"]
        Cod = p["Código"]
        Muestra = "|{:<20}|{:>10}|".format(Producto, Cod)
        print(Muestra)
        print("+--------------------+----------+")

def Alta_prod():

    os.system("cls")
    print(f'''{Fore.CYAN+Style.BRIGHT}----------------------------------
OPCION A - Alta de un producto
----------------------------------{Style.RESET_ALL}''')
    Cod=''
    while(Cod!='V'):
        ArcLogProd.seek(0)
        Producto=Productos()
        Listado_total()
        Cod=Producto.Valida_cod()
        if(Cod!='V'):
            Cod=Producto.Alta()
            if(Cod==1):
                print()
                print("Producto cargado correctamente!")
                print()
            elif(Cod==-1):
                print()
                print("El producto ya se encuentra cargado!")
                print()
            Seguir=input("¿Desea cargar otro producto? Y/N: ").upper()
            while Seguir!='Y' and Seguir!='N':
                Seguir=input("¿Desea cargar otro producto? Y/N: ").upper()
            if(Seguir=='N'):
                Cod='V'
            os.system("cls")

def Baja_prod():
    
    os.system("cls")
    print(f'''{Fore.CYAN+Style.BRIGHT}-------------------------------
OPCION B - Baja de un producto
-------------------------------{Style.RESET_ALL}''')
    t = os.path.getsize(ArcFisiProd)
    if t==0:
        input("No hay productos cargados! <Enter para volver al menú anterior>")
    else:
        Cod=''
        while(Cod!='V'):
            Producto=Productos()
            print()
            Consulta_Prod()
            print()
            Cod = Producto.Valida_cod()
            if(Cod!='V'):
                Reg=Cupo()
                Reg.Conteo()
                if(Producto.Cod=='1') and (ContCebada>0):
                    print()
                    print(f"No puedes dar de baja {Fore.RED+Style.BRIGHT}Cebada{Style.RESET_ALL} si ya hay camiones cargados del producto!")
                elif(Producto.Cod=='2') and (ContGirasol>0):
                    print()
                    print(f"No puedes dar de baja {Fore.RED+Style.BRIGHT}Girasol{Style.RESET_ALL} si ya hay camiones cargados del producto!")
                elif(Producto.Cod=='3') and (ContMaiz>0):
                    print()
                    print(f"No puedes dar de baja {Fore.RED+Style.BRIGHT}Maíz {Style.RESET_ALL}si ya hay camiones cargados del producto!")
                elif(Producto.Cod=='4') and (ContSoja>0):
                    print()
                    print(f"No puedes dar de baja {Fore.RED+Style.BRIGHT}Soja{Style.RESET_ALL} si ya hay camiones cargados del producto!")
                elif(Producto.Cod=='5') and (ContTrigo>0):
                    print()
                    print(f"No puedes dar de baja {Fore.RED+Style.BRIGHT}Trigo{Style.RESET_ALL} si ya hay camiones cargados del producto!")
                else:
                    res=Producto.Busqueda(Producto.Cod,'Cod','I')
                    if(res == -1):
                        print("El producto no se encontró en la lista!")
                    else:
                        print("Producto dado de baja correctamente!")
                print()
                Cod=input("[V - Para volver al menú anterior] - Enter para dar de baja otro producto: ").upper()
                os.system("cls")

def Consulta_Prod():

    os.system("cls")
    t = os.path.getsize(ArcFisiProd)
    if t==0:
        input("[Enter para volver al menú anterior] - No hay productos cargados!")
    else:
        reg=Productos()
        ArcLogProd.seek(0,0)
        print("+--------------------+----------+")
        print("|Producto            |Código    |")
        print("+--------------------+----------+")
        while ArcLogProd.tell() < t:
            reg=pickle.load(ArcLogProd)
            if(reg.Estado=='A'):
                Producto = reg.Prod
                Cod = reg.Cod
                Muestra = "|{:<20}|{:>10}|".format(Producto, Cod)
                print(Muestra)
                print("+--------------------+----------+")

def Modificar_prod():

    os.system("cls")
    print(f'''{Fore.CYAN+Style.BRIGHT}----------------------------------------
OPCION M - Modificación de un producto
----------------------------------------{Style.RESET_ALL}''')
    t = os.path.getsize(ArcFisiProd)
    if t==0:
        print("No hay productos cargados!")
    else:
        Cod=''
        while(Cod!='V'):
            print()
            Consulta_Prod()
            print()
            Producto=Productos()
            Cod=Producto.Valida_cod()
            if(Cod!='V'):
                res=Producto.Busqueda(Producto.Cod,'Cod','')
                if(res == -1): # Verifica que no esté cargado
                    print("El producto no se encontró en la lista!")
                    Cod=input('[V para salir] - Enter para  intentarlo nuevamente: ')
                    os.system("cls")
                elif(res ==  'I'):
                    print("El producto seleccionado ha sido dado de baja!")
                else:
                    CodAux=Producto.Cod
                    ProdAux=Producto.Prod
                    print(f"A continuación, seleccione el producto por el cuál desea sustituir {Producto.Prod}")
                    print()
                    Listado_total()
                    Cod=Producto.Valida_cod()
                    if(Cod!='V'):
                        res=Producto.Busqueda(Producto.Cod,'Cod','')
                        if(res == -1): # Verifica que el segundo no esté cargado
                            Producto.Busqueda(CodAux,'Cod','I') # Da de baja el primer producto
                            # Ver si da de alta el segundo
                            Producto.Formateo()
                            pickle.dump(Producto, ArcLogProd)
                            ArcLogProd.flush()
                            print("Producto modificado correctamente!")
                            Cod=input("[V - Para volver al menú anterior] - Enter para modificar otro producto: ").upper()
                            os.system("cls")
                        elif(res=='I'):
                            Producto.Busqueda(Cod,'Cod','A')
                            Producto.Busqueda(CodAux,'Cod','I')
                        else:
                            print()
                            print(f"El producto por el que desea sustituir {ProdAux} ya se encuentra cargado.")
                            Cod=input("[V - Para volver al menú anterior] - Enter para modificar otro producto: ").upper
                            os.system("cls")

def Cupos(): #Para mejorar, podría haber opción de modificar el cupo en caso de equivocarse

    Patente=''
    while(Patente!='V'):
        os.system('cls')
        RegCup=Cupo()
        Patente=ValidarPat()
        while Patente==True:
            input('Error, la patente debe ser alfanumérica y tener entre 6 y 7 carácteres <Enter para intentarlo nuevamente>')
            os.system('cls')
            Patente=ValidarPat()
        if(Patente!='V'):
            Fecha_Cupo=Val_Fecha()
            if(RegCup.Busqueda_Cupos(Patente,Fecha_Cupo,'','')==-1):
                print()
                input(f"{Fore.RED+Style.BRIGHT}Cupo ya otorgado! {Style.RESET_ALL} <Enter para volver al menú principal>")
                Patente='V'
            else:
                os.system("cls")
                print("¿De qué producto será la carga del camión?")
                print()
                Consulta_Prod()
                print()
                CodP=input("[V - Para volver al menú principal] - Ingrese el código del producto que cargará: ").upper()
                Producto=Productos()
                res=Producto.Busqueda(CodP,'Cod','')
                while(res!='A'):
                    if(CodP=='V'):
                        Patente='V'
                        res='A'
                    else:
                        print("Error, el producto seleccionado no está cargado!")
                        CodP=input("[V - Para volver al menú principal] - Ingrese el código del producto que cargará: ").upper()
                        res=Producto.Busqueda(CodP,'Cod','')
                print()
                if(CodP!='V'):
                    Silo=Silos()
                    res=Silo.Busqueda('',CodP)
                    if(res==-1):
                        print()
                        print("No hay silos para ese producto en este momento!")
                        input("<Enter para volver al menú anterior>")
                        Patente='V'
                    elif(res==1):
                        Revisión_cupo_creado(Patente,CodP,Fecha_Cupo)
                        print()
                        RegCup.Patente=Patente
                        RegCup.Cod=CodP
                        RegCup.Fecha_Cupo = Fecha_Cupo
                        RegCup.Estado='P'
                        Confir=input("¿Desea confirmar la creación del cupo? Y/N: ").upper()
                        while(Confir!='Y') and (Confir!='N'):
                            Confir=input("¿Desea confirmar la creación del cupo? Y/N: ").upper()
                        if(Confir=='Y'):
                            RegCup.Formateo_Cupo()
                            ArcLogOp.seek(0,2)
                            pickle.dump(RegCup,ArcLogOp)
                            ArcLogOp.flush()
                            print()
                            print('--------------------------')
                            print("Cupo creado exitosamente!")
                            print('--------------------------')
                            print()
                            Confir=input("¿Desea pedir un cupo para otro camión? Y/N: ").upper()
                            while(Confir!='Y') and (Confir!='N'):
                                Confir=input("¿Desea pedir un cupo para otro camión? Y/N: ").upper()
                            if(Confir=='N'):
                                Patente='V'
                        else:
                            pass # Opción de modificar la carga?
                
def Revisión_cupo_creado(Patente,CodP,Fecha_Cupo):
    os.system("cls")
    Datos = [
    {
        "Dato": "Patente",
        "Valor": Patente,
    },
    {
        "Dato": "Carga",
        "Valor": CodP,
    },
    {
        "Dato": "Fecha",
        "Valor": Fecha_Cupo.strftime("%d/%m/%Y"),
    }
]

    print("+--------------------+----------+")
    print("|Dato                |Valor     |")
    print("+--------------------+----------+")
    for p in Datos:
        Dato = p["Dato"]
        Valor = p["Valor"]
        Muestra = "|{:<20}|{:>10}|".format(Dato, Valor)
        print(Muestra)
        print("+--------------------+----------+")

def Val_Fecha():

    os.system("cls")
    now= datetime.now()
    max=now.year + 1
    print(f"[Enter para seleccionar el año actual: {now.year}] - Ingrese el año de llegada del camión: ")
    Agno=input(f"<No se puede pedir cupos para una fecha más lejana al año {max}>.  Año: ")
    if(Agno==''):
        Agno=now.year
    while ValidarEnteros(Agno,now.year,max):
        Agno=input("Error, no puede solicitar un cupo con más de un año de diferencia a la fecha actual. Inténtelo nuevamente:")
        if(Agno==''):
            Agno=now.year
    Agno=int(Agno)
    if(Agno==now.year):
        min=now.month
        max=12
        Mes=input(f"[Enter para seleccionar el mes actual: {now.month}] Ingrese el Mes de llegada del camión: ")
        if(Mes==''):
            Mes=now.month
    else:
        max=now.month
        min=1
        Mes=input(f"[De {min} a {max}] Ingrese el Mes de llegada del camión: ")
    while ValidarEnteros(Mes,min,max):
        Mes=input(f"Error, ingrese un mes válido![Entre {min} y {max}]:")
    Mes=int(Mes)
    if(Mes==1) or (Mes==3) or (Mes==5) or (Mes==7) or (Mes==8) or (Mes==10) or (Mes==12):
        max=31
    elif(Mes==2):
        max=28
    else:
        max=30
    if(Mes==now.month):
        if(Agno==now.year):
            min=now.day
            Dia=input(f"[Enter para seleccionar el Día de hoy: {now.day}] Ingrese el Día de llegada del camión: ")
            if(Dia==''):
                Dia=now.day
        else:
            max=now.day
            min=1
            Dia=input(f"[De {min} a {max}] Ingrese el día de llegada del camión: ")
    else:
        min=1
    while ValidarEnteros(Dia,min,max):
        Dia=input(f"[De {min} a {max}] Error, ingrese el día de llegada del camión: ")
    Agno,Mes,Dia = str(Agno),str(Mes),str(Dia)
    Fecha=(f"{Dia}/{Mes}/{Agno}")
    Fecha_Cupo = datetime.strptime(Fecha, "%d/%m/%Y")
    return Fecha_Cupo

def Recepción():

    Reg=Cupo()
    Patente=''
    while(Patente!='V'):
        os.system('cls')
        Patente=ValidarPat()
        while Patente==True:
            input('Error, la patente debe ser alfanumérica y tener entre 6 y 7 carácteres <Enter para intentarlo nuevamente>')
            os.system('cls')
            Patente=ValidarPat()
        res=Reg.Busqueda_Cupos(Patente,Fecha_Actual,'P','A')
        if(res==2):
            print("Recepción realizada correctamente!")
            print()
            Confir=input("¿Desea recibir otro camión? Y/N: ").upper()
            while(Confir!='Y') and (Confir!='N'):
                Confir=input("¿Desea recibir otro camión? Y/N: ").upper()
            if(Confir=='N'):
                Patente='V'
        else:
            print("No hay ningún cupo guardado para este camión el día de hoy!")
            input("<Enter para volver al menú principal>").upper()
            Patente='V'

def Ordenamiento():

    t = os.path.getsize(ArcFisiRubros)
    if t!=0:    
        ArcLogRubros.seek(0, 0)
        aux = pickle.load(ArcLogRubros)
        Reg = ArcLogRubros.tell()
        cantReg = int(t / Reg)
        for i in range(0, cantReg-1):
            for j in range(i+1, cantReg):
                ArcLogRubros.seek(i*Reg, 0)
                auxi = pickle.load(ArcLogRubros)
                ArcLogRubros.seek(j*Reg, 0)
                auxj = pickle.load(ArcLogRubros)
                if int(auxi.CodR) > int(auxj.CodR):
                    ArcLogRubros.seek(i*Reg, 0)
                    pickle.dump(auxj, ArcLogRubros)
                    ArcLogRubros.seek(j*Reg, 0)
                    pickle.dump(auxi, ArcLogRubros)
                    ArcLogRubros.flush()

def Muestra_Calidad(CodP):
    global Rub_t

    Rubro=Rubros()
    RubrosxP=RubrosxProd()
    trp=os.path.getsize(ArcFisiRubrosXProd)
    ArcLogRubrosXProd.seek(0)
    Ordenamiento()
    Rub_t=[]
    print("+-----------------------------------------+")
    print("|   Rubros disponibles para el producto   |")
    print("+--------------------+--------------------+")
    print("| Nombre del rubro:  | Valores admitidos  |")
    print("+--------------------+--------------------+")
    while(ArcLogRubrosXProd.tell() < trp):
        RubrosxP=pickle.load(ArcLogRubrosXProd)
        if(RubrosxP.CodP==CodP):
            Pos=Rubro.Dico(RubrosxP.CodR)
            ArcLogRubros.seek(Pos,0)
            Rubro=pickle.load(ArcLogRubros)
            Nombre=Rubro.Nombre.strip()
            if(RubrosxP.ValMin.strip()=='-1'):
                if(RubrosxP.ValMax.strip()=='1'):
                    Valores=("Espera un \"Sí\"")
                else:
                    Valores=("Espera un \"No\"")
            else:
                Valores=(f"{RubrosxP.ValMin.strip()}-{RubrosxP.ValMax.strip()}")
            Rub=[Nombre,RubrosxP.ValMin.strip(),RubrosxP.ValMax.strip()]
            Rub_t.append(Rub)
            Muestra = "|{:<20}|{:<20}|".format(Nombre, Valores)
            print(Muestra)
            print("+--------------------+--------------------+")
    if Rub_t == []:
        Muestra = f"|{'No hay rubros cargados para el producto!'.center(40)} |"
        print(Muestra)
        print("+--------------------+--------------------+")

def Calidad():

    Reg=Cupo()
    Patente=''
    while(Patente!='V'):
        os.system('cls')
        Patente=ValidarPat()
        while Patente==True:
            input('Error, la patente debe ser alfanumérica y tener entre 6 y 7 carácteres <Enter para intentarlo nuevamente>')
            os.system('cls')
            Patente=ValidarPat()
        res=Reg.Busqueda_Cupos(Patente,Fecha_Actual,'A','')
        if(res==-3):
            print("El camión ingresado no puede acceder a control de calidad en este momento.")
        elif(res==-2):
            print(f"{Fore.RED+Style.BRIGHT}La patente ingresada no tiene cupos para el día de hoy!{Style.RESET_ALL}")
        elif(res==1):
            ArcLogOp.seek(Puntero,0)
            Reg=pickle.load(ArcLogOp)
            Muestra_Calidad(Reg.Cod)
            Acum=0
            if Rub_t != []:
                for rub in Rub_t:
                    if(rub[1]=='-1'): #Booleana
                        Val=input(f'El producto sufrió el rubro: \"{rub[0]}\"? (S/N) : ').upper()
                        while(Val!='S') and (Val!='N'):
                            Val=input(f'El producto sufrió el rubro: \"{rub[0]}\"? (S/N) : ').upper()
                        if rub[2]== '1' and Val=='N':
                            Acum+=1
                        elif rub[2]=='0' and Val=='S':
                            Acum+=1

                    else: #Numérica
                        Val=input(f'<Entre {rub[1]} y {rub[2]}> - Ingrese el valor para el rubro: \"{rub[0]}\": ')
                        if(ValidarEnteros(Val,int(rub[1]),int(rub[2]))):
                            Acum+=1
                if(Acum>1):
                    os.system('cls')
                    print(f"{Fore.RED+Style.BRIGHT}El producto fue rechazado!{Style.RESET_ALL}")
                    res=Reg.Busqueda_Cupos(Patente,Fecha_Actual,'A','R')
                else:
                    res=Reg.Busqueda_Cupos(Patente,Fecha_Actual,'A','C')
                    print('-------------------------------------')
                    print("El camión pasó el control de calidad!")
                    print('-------------------------------------')
        Confir=input("¿Desea controlar la calidad de otro camión? Y/N: ").upper()
        while(Confir!='Y') and (Confir!='N'):
            Confir=input("¿Desea controlar la calidad de otro camión? Y/N: ").upper()
        if(Confir=='N'):
            Patente='V'

def Peso_bruto():
    Reg=Cupo()
    os.system('cls')
    Patente=ValidarPat()
    while(Patente!='V'):
        while Patente==True:
            input('Error, la patente debe ser alfanumérica y tener entre 6 y 7 carácteres <Enter para intentarlo nuevamente>')
            os.system('cls')
            Patente=ValidarPat()
        res=Reg.Busqueda_Cupos(Patente,Fecha_Actual,'C','')
        if(res==-3):
            print("El camión ingresado no puede ingresar un peso bruto en este momento.")
        elif(res==-2):
            print(f"{Fore.RED+Style.BRIGHT}La patente ingresada no tiene cupos para el día de hoy!{Style.RESET_ALL}")
        elif(res==1):
            Pb=input("<Entre 2 y 50000> - Ingrese el peso bruto de la carga ingresada: ")
            while(ValidarEnteros(Pb,2,50000)):
                Pb=input("<Entre 2 y 50000> - Ingrese el peso bruto de la carga ingresada: ")
            ArcLogOp.seek(Puntero,0)
            Reg=pickle.load(ArcLogOp)
            Reg.Bruto = Pb
            Reg.Formateo_Cupo()
            ArcLogOp.seek(Puntero,0)
            pickle.dump(Reg,ArcLogOp)
            ArcLogOp.flush()
            Reg.Busqueda_Cupos(Patente,Fecha_Actual,'C','B')
            print('--------------------------------')
            print("Peso bruto cargado exitosamente!")
            print('--------------------------------')
        Confir=input("¿Desea cargar el peso bruto de otro camión? Y/N: ").upper()
        while(Confir!='Y') and (Confir!='N'):
            Confir=input("¿Desea cargar el peso bruto de otro camión? Y/N: ").upper()
        if(Confir=='N'):
            Patente='V'

def Tara():
    Reg=Cupo()
    os.system('cls')
    Patente=ValidarPat()
    while(Patente!='V'):
        while Patente==True:
            input('Error, la patente debe ser alfanumérica y tener entre 6 y 7 carácteres <Enter para intentarlo nuevamente>')
            os.system('cls')
            Patente=ValidarPat()
        res=Reg.Busqueda_Cupos(Patente,Fecha_Actual,'B','')
        if(res==-3):
            print("El camión ingresado no puede ingresar la tara en este momento.")
        elif(res==-2):
            print(f"{Fore.RED+Style.BRIGHT}La patente ingresada no tiene cupos para el día de hoy!{Style.RESET_ALL}")
        elif(res==1):
            ArcLogOp.seek(Puntero,0)
            Reg=pickle.load(ArcLogOp)
            Tara=input(f"<Entre 1 y {Reg.Bruto.strip()}> - Ingrese la tara del camión ingresado: ")
            while(ValidarEnteros(Tara,1,int(Reg.Bruto.strip()))):
                    Tara=input(f"<Entre 1 y {Reg.Bruto.strip()}> - Ingrese la tara del camión ingresado: ")
            Reg.Tara = Tara
            Reg.Formateo_Cupo()
            ArcLogOp.seek(Puntero,0)
            pickle.dump(Reg, ArcLogOp)
            ArcLogOp.flush()
            PesoN=int(Reg.Bruto.strip()) - int(Reg.Tara.strip())
            Silo=Silos()
            Silo.Busqueda('',Reg.Cod.strip())
            ArcLogSilos.seek(Puntero,0)
            Silo=pickle.load(ArcLogSilos)
            Silo.Stock= int(Silo.Stock.strip()) + PesoN
            Silo.Formateo()
            ArcLogSilos.seek(Puntero,0)
            pickle.dump(Silo,ArcLogSilos)
            ArcLogSilos.flush()
            Reg.Busqueda_Cupos(Patente,Fecha_Actual,'B','F')
            print('--------------------------')
            print("Tara cargada exitosamente!")
            print('--------------------------')
        Confir=input("¿Desea cargar la tara de otro camión? Y/N: ").upper()
        while(Confir!='Y') and (Confir!='N'):
            Confir=input("¿Desea cargar la tara de otro camión? Y/N: ").upper()
        if(Confir=='N'):
            Patente='V'

def PatentesReportes():
    os.system("cls")
    Arr=[['CEBADA',PatMayCeb,PatMenCeb],['GIRASOL',PatMayGir,PatMenGir],['MAÍZ',PatMayMaiz,PatMenMaiz],['SOJA',PatMaySoja,PatMenSoja],['TRIGO',PatMayTrigo,PatMenTrigo]]
    print("+-----------------------------------------------------+")
    print("|  Patentes que realizaron la mayor y menor descarga  |")
    print("+-------------+-------------------+-------------------+")
    print("|  Producto   |  Mayor descarga   |   Menor descarga  |")
    print("+-------------+-------------------+-------------------+")
    for p in Arr:
        Producto = p[0]
        Mayor = p[1]
        Menor = p[2]
        Muestra = f"|{Producto.center(13)}|{Mayor.center(19)}|{Menor.center(19)}|"
        print(Muestra)
        print("+-------------+-------------------+-------------------+")
    input("<Enter para volver al menú anterior>")

def MuestraReportes(Titulo, col1,xc,xg,xm,xs,xt):

    Productos = [
    {
        "Producto": "CEBADA",
        "Valor": xc,
    },
    {
        "Producto": "GIRASOL",
        "Valor": xg,
    },
    {
        "Producto": "MAÍZ",
        "Valor": xm,
    },    {
        "Producto": "SOJA",
        "Valor": xs,
    },    {
        "Producto": "TRIGO",
        "Valor": xt,
    },
]

    os.system("cls")
    print("+-----------------------------------------+")
    print(f"|{Titulo.center(41)}|")
    print("+---------------+-------------------------+")
    print(f"|{'Producto'.center(15)}|{col1.center(25)}|")
    print("+---------------+-------------------------+")
    for p in Productos:
        Producto = p["Producto"]
        Valor = p["Valor"]
        if(isinstance(Valor,float)==True):
            Valor = round(Valor,2)
        Muestra = f"|{Producto.center(15)}|{str(Valor).center(25)}|"
        print(Muestra)
        print("+---------------+-------------------------+")
    input("<Enter para volver al menú anterior>")

def Pantalla_Reportes():
    os.system('cls')
    print(f'{Fore.CYAN+Style.BRIGHT}-----------------------MENÚ REPORTES----------------------')
    print(f'''{Style.RESET_ALL}\nCantidad de cupos otorgados: {CantCupos}
Cantidad total de camiones recibidos: {CantRec}
A- Cantidad total de camiones de cada producto
B- Peso neto total de cada producto
C- Promedio del peso neto por camión de cada producto
D- Patentes mayor y menor descarga realizada
V- Volver al MENU PRINCIPAL

{Fore.CYAN+Style.BRIGHT}----------------------------------------------------------{Style.RESET_ALL}''')

def Reportes():
    Opci=""
    while(Opci!='V'):
        Reg=Cupo()
        Reg.Conteo()
        Pantalla_Reportes()
        Opci=input('[V para volver al menú principal] - Ingrese una opción: ').upper()
        while(Opci!='A') and (Opci!='B') and (Opci!='C') and (Opci!='D') and (Opci!='V'):
            Opci=input('[V para volver al menú principal] - Ingrese una opción: ').upper()
        if(Opci=='A'):
            MuestraReportes('Camiones recibidos por producto','Camiones recibidos',ContCebada,ContGirasol,ContMaiz,ContSoja,ContTrigo)
        elif(Opci=='B'):
            MuestraReportes('P/N total por producto','Peso neto total',AcumCeb,AcumGir,AcumMaiz,AcumSoja,AcumTrigo)
        elif(Opci=='C'):
            MuestraReportes('Promedio del P/N por camión','Promedio P/N',PromCamCeb,PromCamGir,PromCamMaiz,PromCamSoja,PromCamTrigo)
        elif(Opci=='D'):
            PatentesReportes()

def Listado():
    Opci=''
    Silo=Silos()
    Reg=Cupo()
    while(Opci!='V'):
        os.system('cls')
        Mayor=Silo.MayorStock()
        print(f'{Fore.CYAN+Style.BRIGHT}-------------------------Listado de Silos y Rechazados-------------------------')
        print(f'''{Style.RESET_ALL}\nEl silo con mayor stock es:{Fore.CYAN+Style.BRIGHT} {Mayor} {Style.RESET_ALL}
La fecha debe introducirse con el formato {Fore.CYAN+Style.BRIGHT}\"Dia/Mes/Año\"{Style.RESET_ALL}
<Enter para utilizar la fecha del día de hoy>        
''')
        Opci=input('[V para volver] - Ingrese una fecha para ver los camiones rechazados ese día: ').upper()
        if(Opci!='V'):
            try:
                if (Opci==''):
                    now = datetime.now()
                    Opci= f'{now.day}/{now.month}/{now.year}'
                Fecha_Dada = datetime.strptime(Opci, "%d/%m/%Y")
                Lista=Reg.Rechazados(Fecha_Dada)
                Fecha_Dada=Fecha_Dada.strftime("%d/%m/%Y")
                if(len(Lista)>0):
                    for i in Lista:
                        print()
                        print(f"Patentes rechazadas el día {Fecha_Dada}")
                        print()
                        print(i)
                        input("<Enter para ingresar otra fecha>")
                else:
                    print("No se rechazaron camiones ese día!")
                    input("<Enter para ingresar otra fecha>")
            except:
                print("El formato introducido no es válido!")
                input("<Enter para intentarlo nuevamente>")


### Programa Principal ###

Inicializar()