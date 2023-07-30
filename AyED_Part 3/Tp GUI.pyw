import tkinter as tk
import tkinter.ttk as ttk
from tkinter import Entry, messagebox
import os, pickle, os.path,sys,datetime,io
from datetime import date
from colorama import init, Fore, Back, Style
from notifypy import Notify
import requests
from PIL import ImageTk, Image
import sqlite3
from tkcalendar import Calendar,DateEntry
from datetime import datetime
from tkinter.messagebox import showinfo

def darkstyle(root):
   
    style = ttk.Style(root)
    root.tk.call('source', 'azure dark/azure dark.tcl')
    style.theme_use('azure')
    style.configure("Accentttk.Button", foreground='white')
    style.configure("Togglettk.Button", foreground='white')
    return style
# - Animacion de carga - #

w=Tk()
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
w.overrideredirect(1)
	
Frame(w, width=427, height=250, bg='#f5f2f2').place(x=0,y=0)
label1=Label(w, text='Cargando', fg='#272727', bg='#f5f2f2') 
label1.configure(font=("Game Of Squids", 24, "bold"))   
label1.place(x=140,y=90)

label2=Label(w, text='Loading...', fg='#272727', bg='#f5f2f2') 
label2.configure(font=("Calibri", 11))
label2.place(x=10,y=215)

image_a=ImageTk.PhotoImage(Image.open('c2.png'))
image_b=ImageTk.PhotoImage(Image.open('c1.png'))

    
for i in range(3): #3 loops
    l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    label2=Label(w, text='Cargando silos...                ', fg='#272727', bg='#f5f2f2').place(x=10,y=215)
    w.update_idletasks()
    time.sleep(0.9)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    label2=Label(w, text='Agendando Cupos...        ', fg='#272727', bg='#f5f2f2').place(x=10,y=215)
    w.update_idletasks()
    time.sleep(0.9)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    label2=Label(w, text='Descargando Camiones...', fg='#272727', bg='#f5f2f2').place(x=10,y=215)
    w.update_idletasks()
    time.sleep(0.9)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
    label2=Label(w, text='Registrando Productos...     ', fg='#272727', bg='#f5f2f2').place(x=10,y=215)
    w.update_idletasks()
    time.sleep(0.9)
    
label2=Label(w, text='Iniciando Programa...     ', fg='#272727', bg='#f5f2f2').place(x=10,y=215)
w.update_idletasks()
time.sleep(0.9)

# - #

def conn_bbdd():
	global conn, cursor

	if not os.path.exists(Rutabbdd):

		conn = sqlite3.connect(Rutabbdd)
		cursor = conn.cursor()
		
		cursor.execute('''CREATE TABLE PRODUCTOS 
			(COD_PRODUCTO INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE_PRODUCTO VARCHAR(10) UNIQUE NOT NULL,
			ESTADO VARCHAR(1) NOT NULL)''')

		cursor.execute('''CREATE TABLE CUPOS 
			(NUM_CUPO INTEGER PRIMARY KEY AUTOINCREMENT,
			PATENTE VARCHAR(7) NOT NULL,
			COD_PROD INTEGER NOT NULL,
			ESTADO VARCHAR(1) NOT NULL,
			FECHA DATE NOT NULL,
			PESO_BRUTO DECIMAL(5,2) NOT NULL,
			TARA DECIMAL(5,2) NOT NULL,
			FOREIGN KEY(COD_PROD) REFERENCES PRODUCTOS(COD_PRODUCTO))''')

		cursor.execute('''CREATE TABLE RUBROS 
			(COD_RUBRO INTEGER PRIMARY KEY NOT NULL CHECK (LENGTH(COD_RUBRO)>=1),
			NOMBRE_RUBRO VARCHAR(30) NOT NULL CHECK (LENGTH(NOMBRE_RUBRO)>=1))''')

		cursor.execute('''CREATE TABLE RUBROS_ASIGNADOS 
			(COD_RUB INTEGER NOT NULL,
			COD_PROD INTEGER NOT NULL,
			TIPO VARCHAR(7) NOT NULL,
			VALORES VARCHAR(6) NOT NULL,
			FOREIGN KEY(COD_RUB) REFERENCES RUBROS(COD_RUBRO)
			FOREIGN KEY(COD_PROD) REFERENCES PRODUCTOS(COD_PRODUCTO))''')

		cursor.execute('''CREATE TABLE SILOS 
			(COD_SILO INTEGER PRIMARY KEY NOT NULL CHECK (LENGTH(COD_SILO)>=1),
			COD_PROD INTEGER UNIQUE NOT NULL,
			NOMBRE_SILO VARCHAR(30) UNIQUE NOT NULL CHECK (LENGTH(NOMBRE_SILO)>=1),
			STOCK_SILO DECIMAL(7,2) NOT NULL,
			FOREIGN KEY(COD_PROD)REFERENCES PRODUCTOS(COD_PRODUCTO))''')

		Lista_productos = [
		('CEBADA','I'),
		('GIRASOL','I'),
		('MAÍZ','I'),
		('SOJA','I'),
		('TRIGO','I')
		]

		cursor.executemany('INSERT INTO PRODUCTOS VALUES(NULL,?,?)', Lista_productos)
		conn.commit()

	else:
		conn = sqlite3.connect(Rutabbdd)
		cursor = conn.cursor()

def Enviar(origen):
	global Listado, Listado2

	Prod_seleccionado = Listado.get()
	if origen == 'Alta':
		cursor.execute(f'UPDATE PRODUCTOS SET ESTADO="A" WHERE NOMBRE_PRODUCTO="{Prod_seleccionado}"')
		Alta_prod()
		messagebox.showinfo("Alta correcta", "Producto dado de alta correctamente!")
	elif origen == 'Baja':
		cursor.execute(f'UPDATE PRODUCTOS SET ESTADO="I" WHERE NOMBRE_PRODUCTO="{Prod_seleccionado}"')
		Baja_prod()
		messagebox.showinfo("Alta correcta", "Producto dado de baja correctamente!")
	elif origen == 'Mod':
		Prod_seleccionado2 = Listado2.get()
		cursor.execute(f'UPDATE PRODUCTOS SET ESTADO="A" WHERE NOMBRE_PRODUCTO="{Prod_seleccionado2}"')
		cursor.execute(f'UPDATE PRODUCTOS SET ESTADO="I" WHERE NOMBRE_PRODUCTO="{Prod_seleccionado}"')
		Modifica_prod()
		messagebox.showinfo("Modificación correcta", "Producto modificado correctamente!")
	conn.commit()


def Alta_prod():
	global root, Menu_p, Packed, Alta_p, Listado

	Unpack()
	Alta_p=tk.Frame(root)
	Alta_p.pack(fill="both", expand=True)
	Packed="Alta_p"
	Alta_p.config(width=800, height=500, padx=5, pady=5)
	Alta_p.pack_propagate(0)
	ttk.Label(Alta_p, text="ALTA DE PRODUCTOS", font=("arial",20)).pack(padx=10, pady=20)

	cursor.execute('SELECT NOMBRE_PRODUCTO FROM PRODUCTOS WHERE ESTADO="I"')
	Productos_inactivos = cursor.fetchall()
	if Productos_inactivos == []:
		messagebox.showwarning("Aviso", "No hay productos por cargar!.")
	else:
		Frame_interior = tk.Frame(Alta_p)
		Frame_interior.pack(side='top')
		Listado = ttk.Combobox(
			master=Frame_interior,
			state="readonly",
			values=Productos_inactivos
			)
		Listado.pack(padx=5, pady=5, side='left')

		botonaceptar=ttk.Button(Frame_interior, text="Aceptar", width=10, command=lambda:Enviar('Alta'))
		botonaceptar.pack(padx=5, pady=5, side='right')

	botonv=ttk.Button(Alta_p, text="VOLVER AL MENÚ ANTERIOR", width=29, command=Submenu_Prod)
	botonv.pack(padx=5, pady=50, side= 'bottom')

def Baja_prod():
	global root, Menu_p, Packed, Baja_p, Listado

	Unpack()
	Baja_p=tk.Frame(root)
	Baja_p.pack(fill="both", expand=True)
	Packed="Baja_p"
	Baja_p.config(width=800, height=500, padx=5, pady=5)
	Baja_p.pack_propagate(0)
	ttk.Label(Baja_p, text="BAJA DE PRODUCTOS", font=("arial",20)).pack(padx=10, pady=20)

	cursor.execute('SELECT COD_PRODUCTO, NOMBRE_PRODUCTO FROM PRODUCTOS WHERE ESTADO="A"')
	Productos_cargados = cursor.fetchall()

	if Productos_cargados == []:
		messagebox.showwarning("Aviso", "No hay productos cargados!.")
	else:
		cursor.execute('SELECT DISTINCT NOMBRE_PRODUCTO FROM PRODUCTOS LEFT JOIN CUPOS WHERE PRODUCTOS.ESTADO="A" AND COD_PRODUCTO<>(COD_PROD)')
		Productos_cargados = cursor.fetchall()

		Frame_interior = tk.Frame(Baja_p)
		Frame_interior.pack(side='top')
		Listado = ttk.Combobox(
			master=Frame_interior,
			state="readonly",
			values=Productos_cargados
			)
		Listado.pack(padx=5, pady=5, side='left')

		botonaceptar=ttk.Button(Frame_interior, text="Aceptar", width=10, command=lambda:Enviar('Baja'))
		botonaceptar.pack(padx=5, pady=5, side='right')
		botonv=ttk.Button(Baja_p, text="VOLVER AL MENÚ ANTERIOR", width=29, command=Submenu_Prod)
		botonv.pack(padx=5, pady=50, side= 'bottom')

def Consulta_prod():
	global root, Menu_p, Packed, Consulta_p, Listado

	Unpack()
	Consulta_p=tk.Frame(root)
	Consulta_p.pack(fill="both", expand=True)
	Packed="Consulta_p"
	Consulta_p.config(width=800, height=500, padx=5, pady=5)
	Consulta_p.pack_propagate(0)
	ttk.Label(Consulta_p, text="CONSULTA DE PRODUCTOS", font=("arial",20)).pack(padx=10, pady=20)

	cursor.execute('SELECT NOMBRE_PRODUCTO FROM PRODUCTOS WHERE ESTADO="A"')
	Productos_cargados = cursor.fetchall()
	if Productos_cargados == []:
		messagebox.showwarning("Aviso", "No hay productos cargados!.")
	else:
		Listado = ttk.Combobox(
			master=Consulta_p,
			state="readonly",
			values=Productos_cargados
			)
		Listado.pack(padx=5, pady=5)

	botonv=ttk.Button(Consulta_p, text="VOLVER AL MENÚ ANTERIOR", width=29, command=Submenu_Prod)
	botonv.pack(padx=5, pady=50, side= 'bottom')

def Modifica_prod():
	global root, Menu_p, Packed, Mod_p, Listado, Listado2

	Unpack()
	Mod_p=tk.Frame(root)
	Mod_p.pack(fill="both", expand=True)
	Packed="Mod_p"
	Mod_p.config(width=800, height=500, padx=5, pady=5)
	Mod_p.pack_propagate(0)
	ttk.Label(Mod_p, text="MODIFICACIÓN DE PRODUCTOS", font=("arial",20)).pack(padx=10, pady=15)
	ttk.Label(Mod_p, text="¿Qúe producto desea modificar?", font=("arial",15)).pack(padx=10, pady=10)

	cursor.execute('SELECT DISTINCT NOMBRE_PRODUCTO FROM PRODUCTOS LEFT JOIN CUPOS WHERE PRODUCTOS.ESTADO="A" AND COD_PRODUCTO<>(COD_PROD)')
	Productos_cargados = cursor.fetchall()
	cursor.execute('SELECT NOMBRE_PRODUCTO FROM PRODUCTOS WHERE ESTADO="I"')
	Productos_inactivos = cursor.fetchall()
	if Productos_cargados == [] or Productos_inactivos == []:
		messagebox.showwarning("Aviso", "No hay al menos un producto cargado y uno por cargar!.")
	else:
		Frame_interior = tk.Frame(Mod_p)
		Frame_interior.pack(side='top')
		Listado = ttk.Combobox(
			master=Frame_interior,
			state="readonly",
			values=Productos_cargados
			)
		Listado.pack(padx=5, pady=20)

		ttk.Label(Frame_interior, text="¿Por cuál lo desea modificar?", font=("arial",15)).pack(padx=10, pady=20)

		Listado2 = ttk.Combobox(
			master=Frame_interior,
			state="readonly",
			values=Productos_inactivos
			)
		Listado2.pack(padx=5, pady=10)

		botonaceptar=ttk.Button(Frame_interior, text="Aceptar", width=10, command=lambda:Enviar('Mod'))
		botonaceptar.pack(padx=5, pady=60)


	botonv=ttk.Button(Mod_p, text="VOLVER AL MENÚ ANTERIOR", width=29, command=Submenu_Prod)
	botonv.pack(padx=5, pady=5,side= 'bottom')

def salirAplicacion():
	valor=messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
	if valor=="yes":
		root.destroy()

def Alta_Rubros():
	global root, Menu_p, Packed, Alta_r

	Unpack()
	Alta_r=tk.Frame(root)
	Alta_r.pack(fill="both", expand=True)
	Packed="Alta_r"
	Alta_r.config(width=800, height=500, padx=5, pady=5)
	Alta_r.pack_propagate(0)
	ttk.Label(Alta_r, text="ALTA DE RUBROS", font=("arial",20)).pack(padx=10, pady=20)

	Frame_interior = tk.Frame(Alta_r)
	Frame_interior.pack(side='top')
	Cod = tk.StringVar()
	Nombre = tk.StringVar()
	ttk.Label(Frame_interior, text="Código: ", font=("arial",10)).pack(padx=10, pady=10, side='left', anchor='e')
	ttk.Entry(Frame_interior,textvariable=Cod).pack(padx=10, pady=10,side='right', anchor='w')
	Frame_interior2 = tk.Frame(Alta_r)
	Frame_interior2.pack(side='top')
	ttk.Label(Frame_interior2, text="Nombre:", font=("arial",10)).pack(padx=10, pady=10, side='left', anchor='e')
	ttk.Entry(Frame_interior2,textvariable=Nombre).pack(padx=10, pady=10,side='right', anchor='w')
	botonaceptar=ttk.Button(Alta_r, text="Aceptar", width=10, command=lambda:Enviar_r(Cod.get(),Nombre.get()))
	botonaceptar.pack(padx=5, pady=5)

	botonv=ttk.Button(Alta_r, text="VOLVER AL MENÚ ANTERIOR", width=29, command=Administraciones)
	botonv.pack(padx=5, pady=50, side= 'bottom')

def Enviar_r(Cod,Nombre):
	Bandera = True
	if Cod.isdigit() == False:
		messagebox.showwarning("Error", "El código solo puede estar formado por números.")
		Bandera = False
	if Nombre.replace(' ','').isalpha() == False:
		messagebox.showwarning("Error", "El nombre solo puede estar formado por letras.")
		Bandera = False
	cursor.execute(f'SELECT COD_RUBRO FROM RUBROS WHERE NOMBRE_RUBRO="{Nombre}"')
	Nombreusado = cursor.fetchone()
	chars = '(),'
	if Nombreusado != None:
		Nombreusado = ''.join( x for x in str(Nombreusado) if x not in chars)
		messagebox.showwarning("Error", f"El rubro {Nombre} ya se encuentra cargado con el código {Nombreusado}.")
		Bandera = False
	cursor.execute(f'SELECT NOMBRE_RUBRO FROM RUBROS WHERE COD_RUBRO="{Cod}"')
	Codusado = cursor.fetchone()
	if Codusado != None:
		Codusado = ''.join( x for x in str(Codusado) if x not in chars)
		messagebox.showwarning("Error", f"El código {Cod} ya se encuentra utilizado con el rubro {Codusado}.")
		Bandera = False
	if Bandera == True:
		Nombre = Nombre.capitalize()
		cursor.execute(F'INSERT INTO RUBROS VALUES({Cod},"{Nombre}")')
		conn.commit()
		Alta_Rubros()
		messagebox.showinfo("Alta correcta", "Rubro dado de alta correctamente!")

def Alta_silo():

	global root, Menu_p, Packed, Alta_s, Listado

	Unpack()
	Alta_s=tk.Frame(root)
	Alta_s.pack(fill="both", expand=True)
	Packed="Alta_s"
	Alta_s.config(width=800, height=500, padx=5, pady=5)
	Alta_s.pack_propagate(0)
	ttk.Label(Alta_s, text="ALTA DE SILOS", font=("arial",20)).pack(padx=10, pady=20)

	Frame_interior = tk.Frame(Alta_s)
	Frame_interior.pack(side='top')
	Cod = tk.StringVar()
	Nombre = tk.StringVar()
	ttk.Label(Frame_interior, text="Código: ", font=("arial",10)).pack(padx=10, pady=10, side='left', anchor='e')
	ttk.Entry(Frame_interior,textvariable=Cod).pack(padx=10, pady=10,side='right', anchor='w')
	Frame_nombre = tk.Frame(Alta_s)
	Frame_nombre.pack(side='top')
	ttk.Label(Frame_nombre, text="Nombre:", font=("arial",10)).pack(padx=10, pady=10, side='left', anchor='e')
	ttk.Entry(Frame_nombre,textvariable=Nombre).pack(padx=10, pady=10,side='right', anchor='w')

	Frame_interior2 = tk.Frame(Alta_s)
	Frame_interior2.pack(side='top')
	ttk.Label(Frame_interior2, text="Producto:", font=("arial",10)).pack(padx=10, pady=10, side='left', anchor='e')

	cursor.execute('SELECT NOMBRE_PRODUCTO FROM PRODUCTOS WHERE ESTADO="A"')
	Productos_cargados = cursor.fetchall()
	if Productos_cargados == None:
		pass
	else:
		Listado = ttk.Combobox(
			master=Frame_interior2,
			state="readonly",
			values=Productos_cargados
			)
		Listado.pack(padx=10, pady=10,side='right', anchor='w')

	Frame_interior3 = tk.Frame(Alta_s)
	Frame_interior3.pack(side='top', expand=True)


	botonaceptar=ttk.Button(Frame_interior3, text="Aceptar", width=10, command=lambda:Enviar_s(Cod.get(),Listado.get(),Nombre.get()))
	botonaceptar.pack(padx=5, pady=25, side='left')

	botonv=ttk.Button(Alta_s, text="VOLVER AL MENÚ ANTERIOR", width=29, command=Administraciones)
	botonv.pack(padx=5, pady=50, side= 'bottom')

def Enviar_s(Cod, Producto, Nombre):
	Bandera = True
	if Cod.isdigit() == False:
		messagebox.showwarning("Error", "El código solo puede estar formado por números.")
		Bandera = False
	if Nombre.replace(' ','').isalpha() == False:
		messagebox.showwarning("Error", "El nombre solo puede estar formado por letras.")
		Bandera = False
	if Producto =='':
		messagebox.showwarning("Error", "Debe seleccionar un producto.")
		Bandera = False	
	cursor.execute(f'SELECT COD_SILO FROM SILOS WHERE NOMBRE_SILO="{Nombre.capitalize()}"')
	Silo_existente = cursor.fetchone()
	chars = '(),'
	if Silo_existente != None:
		Silo_existente = ''.join( x for x in str(Silo_existente) if x not in chars)
		messagebox.showwarning("Error", f"El Silo {Nombre.capitalize()} ya se encuentra cargado con el código {Silo_existente}.")
		Bandera = False
	cursor.execute(f'SELECT NOMBRE_SILO FROM SILOS WHERE COD_SILO="{Cod}"')
	Codusado = cursor.fetchone()
	if Codusado != None:
		Codusado = ''.join( x for x in str(Codusado) if x not in chars)
		messagebox.showwarning("Error", f"El código {Cod} ya se encuentra utilizado con el {Codusado}.")
		Bandera = False
	cursor.execute(f'SELECT COD_PRODUCTO FROM PRODUCTOS WHERE NOMBRE_PRODUCTO="{Producto}"')
	CodP = cursor.fetchone()
	CodP = ''.join( x for x in str(CodP) if x not in chars)
	cursor.execute(f'SELECT NOMBRE_SILO FROM SILOS WHERE COD_PROD="{CodP}"')
	Producto_existente = cursor.fetchone()
	if Producto_existente != None:
		Producto_existente = ''.join( x for x in str(Producto_existente) if x not in chars)
		messagebox.showwarning("Error", f"El producto {Producto} ya tiene un silo llamado {Producto_existente}.")
		Bandera = False
	if Bandera == True and CodP != None:
		cursor.execute(f'INSERT INTO SILOS VALUES({Cod},"{CodP}","{Nombre.capitalize()}",0)')
		conn.commit()
		Alta_silo()
		messagebox.showinfo("Alta correcta", "Silo dado de alta correctamente!")

def Asignar_Rubros():
	global root, Menu_p, Packed, Asig_r, Listado, Listado2, subpacked

	Unpack()
	Asig_r=tk.Frame(root)
	Asig_r.pack(fill="both", expand=True)
	Packed="Asig_r"
	Asig_r.config(width=800, height=500, padx=5, pady=5)
	Asig_r.pack_propagate(0)
	ttk.Label(Asig_r, text="ASIGNACIÓN DE RUBROS", font=("arial",20)).pack(padx=10, pady=5)
	ttk.Label(Asig_r, text="¿Qúe rubro desea asignar?", font=("arial",15)).pack(padx=10, pady=5)

	cursor.execute('SELECT NOMBRE_RUBRO FROM RUBROS')
	Rubros = cursor.fetchall()
	cursor.execute('SELECT NOMBRE_PRODUCTO FROM PRODUCTOS WHERE ESTADO="A"')
	Productos_cargados = cursor.fetchall()
	if Rubros == [] or Productos_cargados == []:
		messagebox.showwarning("Error",f"No se pueden asignar rubros sin primero cargar rubros y productos!")
		Volver_Menu()
	else:
		chars = '(),'
		Rubros = map(lambda elem: ''.join( x for x in elem if x not in chars),Rubros)
		Frame_interior = tk.Frame(Asig_r)
		Frame_interior.pack(side='top')
		Rub = ttk.Combobox(
			master=Frame_interior,
			state="readonly",
			values=list(Rubros),
			width=25
			)
		Rub.pack(padx=5, pady=5)

		ttk.Label(Frame_interior, text="¿A qué producto se lo desea asignar?", font=("arial",15)).pack(padx=10, pady=5)

		Prod = ttk.Combobox(
			master=Frame_interior,
			state="readonly",
			values=Productos_cargados,
			width=25
			)
		Prod.pack(padx=5, pady=5)

		tiporubro = tk.IntVar()
		ttk.Label(Frame_interior, text="¿Qué tipo de valor recibirá este producto?", font=("arial",15)).pack(padx=10, pady=5)
		Frame_rb = tk.Frame(Asig_r)
		Frame_rb.pack(side='top')
		subpacked = ''
		ttk.Radiobutton(Frame_rb, text=("Valor numérico".center(15)), variable=tiporubro, value=1, command=lambda:Tipo_rub(Rub.get(),Prod.get(),tiporubro.get())).pack(side='left', anchor='e')
		ttk.Radiobutton(Frame_rb, text=("Sí o no".center(15)), variable=tiporubro, value=2, command=lambda:Tipo_rub(Rub.get(),Prod.get(),tiporubro.get())).pack(side='right', anchor='w')


	botonv=ttk.Button(Asig_r, text="VOLVER AL MENÚ ANTERIOR", width=29, command=Administraciones)
	botonv.pack(padx=5, pady=5,side= 'bottom')

def Tipo_rub(Rubro,Producto,Eleccion):
	global subpacked, ContenedorNum, ContenedorBoolean

	if(subpacked == 'Valnum'):
		ContenedorNum.pack_forget()
	elif(subpacked == 'Boolean'):
		ContenedorBoolean.pack_forget()
	Min = tk.StringVar()
	Max = tk.StringVar()
	Valores = tk.StringVar()

	if Eleccion == 1: # Valnum

		ContenedorNum = tk.Frame(Asig_r)
		ContenedorNum.pack(side='top')

		subpacked = 'Valnum'

		ttk.Label(ContenedorNum, text="Ingrese los valores mínimos y máximos en los que el rubro es aceptado", font=("arial",15)).pack(padx=10, pady=5)

		Frame_vn = tk.Frame(ContenedorNum)	
		Frame_vn.pack(side='top')
		Frame_vn2 = tk.Frame(ContenedorNum)	
		Frame_vn2.pack(side='top')
		ttk.Label(Frame_vn, text="Valor mínimo: ", font=("arial",10)).pack(padx=10, pady=10, side='left', anchor='e')
		ttk.Entry(Frame_vn,textvariable=Min).pack(padx=10, pady=10,side='right', anchor='w')
		ttk.Label(Frame_vn2, text="Valor máximo: ", font=("arial",10)).pack(padx=10, pady=10, side='left', anchor='e')
		ttk.Entry(Frame_vn2,textvariable=Max).pack(padx=10, pady=10,side='right', anchor='w')

		botonenviar=ttk.Button(ContenedorNum, text="Enviar", width=10, command=lambda:Enviar_valores(Rubro,Producto,Min.get(),Max.get()))
		botonenviar.pack(padx=5, pady=5)

	
	elif Eleccion ==2: # Booleano

		ContenedorBoolean = tk.Frame(Asig_r)
		ContenedorBoolean.pack(side='top')

		subpacked = 'Boolean'

		ttk.Label(ContenedorBoolean, text="¿En qué caso se aceptará el rubro?", font=("arial",15)).pack(padx=10, pady=15)

		Frame_boolean = tk.Frame(ContenedorBoolean)	
		Frame_boolean.pack(side='top')

		ttk.Radiobutton(Frame_boolean, text="Sí", variable=Valores, value='True').pack(padx=5,side='left', anchor='e')
		ttk.Radiobutton(Frame_boolean, text="No", variable=Valores, value='False').pack(padx=5, side='right', anchor='w')

		botonenviar=ttk.Button(ContenedorBoolean, text="Enviar", width=10, command=lambda:Enviar_valores(Rubro,Producto,Valores.get()))
		botonenviar.pack(padx=10, pady=30)

def Enviar_valores(Rubro,Producto,Valores,x=''):

	Bandera = True
	Tipo = 'Boolean'
	if subpacked == 'Valnum':
		if Valores.isdigit() == False or x.isdigit() == False:
			messagebox.showwarning("Error","Los valores deben ser numéricos.")
			Bandera = False
		elif int(Valores)<0:
			messagebox.showwarning("Error","El valor mínimo no puede ser menor a 0.")
			Bandera = False
		elif int(x)>100:
			messagebox.showwarning("Error","El valor máximo no puede ser mayor a 100.")
			Bandera = False
		elif int(Valores)>int(x):
			messagebox.showwarning("Error","El valor mínimo no puede ser mayor al máximo.")
			Bandera = False
		else:
			Tipo = 'Numeric'
			Valores = f'{Valores}-{x}'
	cursor.execute(f'SELECT COD_RUBRO FROM RUBROS WHERE NOMBRE_RUBRO="{Rubro}"')
	Cod_rubro = cursor.fetchone()
	chars = '(),'
	Cod_rubro = ''.join( x for x in str(Cod_rubro) if x not in chars)
	cursor.execute(f'SELECT COD_PRODUCTO FROM PRODUCTOS WHERE NOMBRE_PRODUCTO="{Producto}"')
	Cod_prod = cursor.fetchone()
	Cod_prod = ''.join( x for x in str(Cod_prod) if x not in chars)
	cursor.execute(f'SELECT * FROM RUBROS_ASIGNADOS WHERE COD_RUB={Cod_rubro} AND COD_PROD={Cod_prod}')
	if cursor.fetchone() == None and Bandera == True:
		cursor.execute(f'INSERT INTO RUBROS_ASIGNADOS VALUES ({Cod_rubro},{Cod_prod},"{Tipo}","{Valores}")')
		conn.commit()
		Asignar_Rubros()
		messagebox.showinfo("Asignación correcta", f"Rubro asignado correctamente a {Producto.capitalize()}!")
	else:
		messagebox.showwarning("Error",f"{Rubro} ya fue asignado a {Producto.capitalize()}!.")
		Asignar_Rubros()

def Administraciones():
	global root, Adm, Menu_p, Packed, Submp

	Unpack()
	Adm=tk.Frame(root)
	Adm.pack(fill="both", expand=True)
	Packed="Adm"
	Adm.config(width=800, height=500, padx=5, pady=5)
	Adm.pack_propagate(0)
	ttk.Label(Adm, text="MENÚ ADMINISTRACIONES", font=("arial",20)).pack(padx=10, pady=10)
	botona=ttk.Button(Adm, text="TITULARES", width=29, command=Notificacion)
	botona.pack(padx=5, pady=5)
	botonb=ttk.Button(Adm, text="PRODUCTOS", width=29, command=Submenu_Prod)
	botonb.pack(padx=5, pady=5)
	botonc=ttk.Button(Adm, text="RUBROS", width=29, command=Alta_Rubros)
	botonc.pack(padx=5, pady=5)
	botond=ttk.Button(Adm, text="RUBROS POR PRODUCTO", width=29, command=Asignar_Rubros)
	botond.pack(padx=5, pady=5)
	botone=ttk.Button(Adm, text="SILOS", width=29, command=Alta_silo)
	botone.pack(padx=5, pady=5)
	botonf=ttk.Button(Adm, text="SUCURSALES", width=29, command=Notificacion)
	botonf.pack(padx=5, pady=5)
	botong=ttk.Button(Adm, text="PRODUCTO POR TITULAR", width=29, command=Notificacion)
	botong.pack(padx=5, pady=5)
	botonv=ttk.Button(Adm, text="VOLVER AL MENÚ PRINCIPAL", width=29, command=Volver_Menu)
	botonv.pack(padx=5, pady=5)

def Submenu_Prod():
	global root, Menu_p, Packed, Adm, Submp

	Unpack()
	Submp=tk.Frame(root)
	Submp.pack(fill="both", expand=True)
	Packed="Submp"
	Submp.config(width=800, height=500, padx=5, pady=5)
	Submp.pack_propagate(0)
	ttk.Label(Submp, text="SUB-MENÚ PRODUCTOS", font=("arial",20)).pack(padx=10, pady=10)
	botona=ttk.Button(Submp, text="ALTA", width=29, command=Alta_prod)
	botona.pack(padx=5, pady=5)
	botonb=ttk.Button(Submp, text="BAJA", width=29, command=Baja_prod)
	botonb.pack(padx=5, pady=5)
	botonc=ttk.Button(Submp, text="CONSULTA", width=29, command=Consulta_prod)
	botonc.pack(padx=5, pady=5)
	botond=ttk.Button(Submp, text="MODIFICACIÓN", width=29, command=Modifica_prod)
	botond.pack(padx=5, pady=5)
	botone=ttk.Button(Submp, text="VOLVER A ADMINISTRACIONES", width=29, command=Administraciones)
	botone.pack(padx=5, pady=5)

def Volver_Menu():
	global Adm,Menu_p, Packed, Submp

	Unpack()
	Menu_p.pack(fill="both", expand=True)
	Menu_p.pack_propagate(0)
	Packed="Menu_p"

def Menu():
	global Menu_p, Packed, root, Fecha_hoy

	now = datetime.now()
	Fecha_hoy = f'{now.day}/{now.month}/{str(now.year)[2:]}'	
	Menu_p=tk.Frame(root)
	Menu_p.pack(fill="both", expand=True)
	Packed="Menu_p"
	Menu_p.configure(width=800, height=500, padx=5, pady=5)
	Menu_p.pack_propagate(0)
	ttk.Label(Menu_p, text="MENÚ PRINCIPAL", font=("arial",20)).pack(padx=10, pady=10)
	boton1=ttk.Button(Menu_p, text="ADMINISTRACIONES", width=29, command=Administraciones)
	boton1.pack(padx=5, pady=5)
	boton2=ttk.Button(Menu_p, text="ENTREGA DE CUPOS", width=29, command=lambda:Menu_Pat('Cupos'))
	boton2.pack(padx=5, pady=5)
	boton3=ttk.Button(Menu_p, text="RECEPCIÓN", width=29, command=lambda:Menu_Pat('Recepcion'))
	boton3.pack(padx=5, pady=5)
	boton4=ttk.Button(Menu_p, text="REGISTRAR CALIDAD", width=29, command=lambda:Menu_Pat('Calidad'))
	boton4.pack(padx=5, pady=5)
	boton5=ttk.Button(Menu_p, text="REGISTRAR PESO BRUTO", width=29, command=lambda:Menu_Pat("PBruto"))
	boton5.pack(padx=5, pady=5)
	boton6=ttk.Button(Menu_p, text="REGISTRAR DESCARGA", width=29, command=Notificacion)
	boton6.pack(padx=5, pady=5)
	boton7=ttk.Button(Menu_p, text="REGISTRAR TARA", width=29, command=lambda:Menu_Pat("Tara"))
	boton7.pack(padx=5, pady=5)
	boton8=ttk.Button(Menu_p, text="REPORTES", width=29, command=Reportes)
	boton8.pack(padx=5, pady=5)
	boton9=ttk.Button(Menu_p, text="LISTADO DE SILOS Y RECHAZOS", width=29, command=Listado_silos)
	boton9.pack(padx=5, pady=5)
	boton0=ttk.Button(Menu_p, text="FIN DEL PROGRAMA", command=salirAplicacion, width=29)
	boton0.pack(padx=5, pady=5)

def Unpack():
	global Packed, Menu_p, Submp, Adm, Pat, Cup, Cal, Frame_tree
	
	if(Packed=="Menu_p"):
		Menu_p.pack_forget()
	elif(Packed=="Submp"):
		Submp.pack_forget()
	elif(Packed=="Adm"):
		Adm.pack_forget()
	elif(Packed=="Pat"):
		Pat.pack_forget()
	elif(Packed=="Cup"):
		Cup.pack_forget()
	elif(Packed=="Cal"):
		Cal.pack_forget()
	elif(Packed=="PBru"):
		PBru.pack_forget()
	elif(Packed=="Tar"):
		Tar.pack_forget()
	elif(Packed=="Rep"):
		Rep.pack_forget()
	elif(Packed=="Alta_p"):
		Alta_p.pack_forget()
	elif(Packed=="Baja_p"):
		Baja_p.pack_forget()
	elif(Packed=="Consulta_p"):
		Consulta_p.pack_forget()
	elif(Packed=="Mod_p"):
		Mod_p.pack_forget()
	elif(Packed=="Alta_r"):
		Alta_r.pack_forget()
	elif(Packed=="Alta_s"):
		Alta_s.pack_forget()
	elif(Packed=="Asig_r"):
		Asig_r.pack_forget()
	elif(Packed=='Tree'):
		Frame_tree.pack_forget()
	elif(Packed=='Lsil'):
		Lsil.pack_forget()

def Menu_Pat(Op_menu):
	global Pat, root, Patente, Packed, Menu_p

	Unpack()
	Pat=tk.Frame(root)
	Pat.pack(fill="both", expand=True)
	Packed="Pat"
	Pat.config(width=800, height=500, padx=5, pady=5)
	Pat.pack_propagate(0)
	ttk.Label(Pat, text="INGRESO DE PATENTE", font=("arial",20)).pack(padx=10, pady=10)
	Patente=tk.StringVar()
	Cuadrat=tk.Entry(Pat, textvariable=Patente, justify="center", width=20).pack(ipadx=5,ipady=5,padx=10, pady=10)
	Send_button=ttk.Button(Pat, text="Validar", command=lambda:Valida_pat(Op_menu), width=8).pack(ipadx=3,ipady=3,padx=10,pady=10)
	botonmenu=ttk.Button(Pat, text="VOLVER AL MENÚ PRINCIPAL", width=29, command=Volver_Menu).pack(padx=10, pady=10)

def Valida_pat(Op_menu):
	global Patente, Packed, Menu_p

	X=Patente.get()
	if(X=='V') or (X.isalnum()==True) and (len(X)==6) or (len(X)==7):
		Unpack()
		if(Op_menu=="Cupos"):
			Cupos(X)
		elif(Op_menu=="Recepcion"):
			cursor.execute(f'SELECT FECHA FROM CUPOS WHERE PATENTE="{X}" AND ESTADO="P"')
			Fecha = cursor.fetchone()
			if Fecha == None:
				valor=messagebox.askquestion("Error", "La patente ingresada no tiene una recepción pendiente hoy!\n¿Desea recibir otro camión?")
				if valor == 'yes':
					Menu_Pat('Recepcion')
				else:
					Volver_Menu()
			else:
				chars = "()',"
				Fecha = ''.join( x for x in str(Fecha) if x not in chars)
				if Fecha == Fecha_hoy:
					cursor.execute(f'UPDATE CUPOS SET ESTADO="A" WHERE PATENTE="{X}" AND FECHA="{Fecha}"')
					conn.commit()
					valor=messagebox.askquestion("Recepción realizada", "¿Desea recibir otro camión?")
					if valor == 'yes':
						Menu_Pat('Recepcion')
					else:
						Volver_Menu()

		elif(Op_menu=="Calidad"):
			Calidad(X)
		elif(Op_menu=="PBruto"):
			PBruto(X)
		elif(Op_menu=="Tara"):
			Tara(X)

	else:
		valor=messagebox.askretrycancel("Patente inválida", "¿Desea intentarlo nuevamente?")
		if valor==False:
			Unpack()
			Packed="Menu_p"
			Menu_p.pack(fill="both", expand=True)
			Menu_p.pack_propagate(0)
	
def Cupos(Patente):
	global Packed, Cup

	Cup=tk.Frame(root)
	Cup.pack(fill="both", expand=True)
	Cup.config(width=800, height=500, padx=5, pady=5)
	Cup.pack_propagate(0)
	Packed="Cup"
	Title=ttk.Label(Cup, text="ENTREGA DE CUPOS", font=("arial",20)).pack(padx=10, pady=10)

	ttk.Label(Cup, text="Ingrese la fecha para la cual quiere solicitar el cupo", font=("arial",12)).pack(padx=10)


	Cal = Calendar(Cup)
	Cal.pack(pady=20)
	Cal.config(headersbackground='#364c55', foreground='#000', background='#fff', headersforeground ='#fff')

	ttk.Label(Cup, text="¿Qué producto cargará el camión?", font=("arial",12)).pack(padx=10)

	# Lista prods

	cursor.execute('SELECT NOMBRE_PRODUCTO FROM PRODUCTOS WHERE ESTADO="A"')
	Productos_cargados = cursor.fetchall()

	Listado = ttk.Combobox(
		master=Cup,
		state="readonly",
		values=Productos_cargados
		)
	Listado.pack(padx=5, pady=15)

	botonenviar = ttk.Button(Cup, text="Enviar", width=10, command=lambda:Crea_cupo(Patente,Cal.get_date(),Listado.get())).pack(padx=5, pady=15)

	botonmenu=ttk.Button(Cup, text="VOLVER AL MENÚ PRINCIPAL", width=29, command=Volver_Menu).pack(padx=5, pady=10)

def Crea_cupo(Patente,Fecha,Producto):

	Fecha = Fecha.split('/') # Dar formato D-M-Y
	Fecha = f'{Fecha[1]}/{Fecha[0]}/{Fecha[2]}'

	cursor.execute(f'SELECT COD_PRODUCTO FROM PRODUCTOS WHERE NOMBRE_PRODUCTO="{Producto}"')
	Cod_prod = cursor.fetchone()
	chars = '(),'
	Cod_prod = ''.join( x for x in str(Cod_prod) if x not in chars)
	cursor.execute(f'SELECT * FROM CUPOS WHERE PATENTE="{Patente}" AND FECHA="{Fecha}"')
	if cursor.fetchone() != None:
		messagebox.showwarning("Error",f"La patente ingresada ya tiene cupo para el día {Fecha}!")
	else:
		cursor.execute(f'SELECT COD_SILO FROM SILOS WHERE COD_PROD="{Cod_prod}"')
		Silo_existente = cursor.fetchone()
		if Silo_existente == None:
			messagebox.showwarning("Error","Primero debe creaer un silo para ese producto!")
		else:
			cursor.execute(f'INSERT INTO CUPOS VALUES(NULL,"{Patente}","{Cod_prod}","P","{Fecha}",0,0)')
			conn.commit()
			valor=messagebox.askquestion("Asignación correcta", "¿Desea crear otro cupo?")
			if valor == 'yes':
				Menu_Pat('Cupos')
			else:
				Volver_Menu()

def Calidad(Patente):
	global Packed, Cal, Frame_boolean, cont_rubros, rubro, rubros, Frame_Rubros

	Cal=tk.Frame(root)
	Cal.pack(fill="both", expand=True)
	Cal.config(width=800, height=500, padx=5, pady=5)
	Cal.pack_propagate(0)
	Packed="Cal"
	Title=ttk.Label(Cal, text="REGISTRAR CALIDAD", font=("arial",20)).pack(padx=10, pady=10)
	cursor.execute(f'SELECT COD_PROD FROM CUPOS WHERE PATENTE="{Patente}" AND ESTADO="A"')
	Cod_prod = cursor.fetchone()
	if Cod_prod == None:
		valor=messagebox.askquestion("Error", "La patente ingresada no tiene que verificar calidad hoy!\n¿Desea validar otro camión?")
		if valor == 'yes':
			Menu_Pat('Calidad')
		else:
			Volver_Menu()
	else:
		chars = "(),'"
		Cod_prod = ''.join( x for x in str(Cod_prod) if x not in chars)
		cursor.execute(f'SELECT * FROM RUBROS_ASIGNADOS WHERE COD_PROD={Cod_prod} ')
		Rubros_por_validar = cursor.fetchall()
		if Rubros_por_validar == []:
			messagebox.showwarning("Error",f"El camión no puede ingresar a calidad si antes no se crean rubros para el producto!")
			Volver_Menu()
		else:
			Frame_Rubros = tk.Frame(Cal)
			Frame_Rubros.pack(side='bottom',expand=True,fill='both')
			rubros = Listar_rubros(Rubros_por_validar)
			cont_rubros = 0
			Validar_rubro('',Patente)
			botonmenu=ttk.Button(Frame_Rubros, text="VOLVER AL MENÚ PRINCIPAL", width=29, command=Volver_Menu).pack(padx=5, pady=5,side='bottom')
		
def Validar_rubro(subpacked,Patente,Valor=0,Eleccion=0):
	global cont_rubros, Frame_boolean, Frame_num

	if Eleccion!='':
		if subpacked == 'Boolean':
			Frame_boolean.destroy()
			if Valor != Eleccion:
				cont_rubros += 1
		elif subpacked == 'Numeric':
			Frame_num.destroy()
			Valor = Valor.split('-')
			if int(Eleccion)<int(Valor[0]) or int(Eleccion)>int(Valor[1]):
				cont_rubros+=1
		chars = "(),'"
		try:
			rubro = next(rubros)
			cursor.execute(f'SELECT NOMBRE_RUBRO FROM RUBROS WHERE COD_RUBRO={rubro[0]}')
			nombrerubro = cursor.fetchone()
			nombrerubro = ''.join( x for x in str(nombrerubro) if x not in chars)
			if rubro[2] == 'Boolean':
				subpacked = 'Boolean'
				elec = tk.StringVar()
				Frame_boolean = tk.Frame(Frame_Rubros)
				Frame_boolean.pack()
				ttk.Label(Frame_boolean, text=f"El producto sufrió el rubro {nombrerubro}?", font=("arial",14)).pack(padx=10, pady=20)
				ttk.Radiobutton(Frame_boolean, text="Sí", variable=elec, value='True').pack(padx=5)
				ttk.Radiobutton(Frame_boolean, text="No", variable=elec, value='False').pack(padx=5)
				botonenviar=ttk.Button(Frame_boolean, text="Enviar", width=10, command=lambda:Validar_rubro(subpacked,Patente,rubro[3],elec.get()))
				botonenviar.pack(padx=5, pady=5)	
			elif rubro[2] == 'Numeric':
				subpacked = 'Numeric'
				Valor = tk.IntVar()
				Frame_num = tk.Frame(Frame_Rubros)
				Frame_num.pack()
				ttk.Label(Frame_num, text=f"Ingrese el valor del rubro {nombrerubro}", font=("arial",14)).pack(padx=10, pady=20)
				Frame_Valor = tk.Frame(Frame_num)
				Frame_Valor.pack(padx=5, pady=5, side='top')
				ttk.Label(Frame_Valor, text="Valor:", font=("arial",10)).pack(padx=5,pady=10, side='left', anchor='e')
				ttk.Entry(Frame_Valor,textvariable=Valor).pack(padx=5,pady=10,side='right', anchor='w')

				botonenviar=ttk.Button(Frame_num, text="Enviar", width=10, command=lambda:Validar_rubro(subpacked,Patente,rubro[3],Valor.get()))
				botonenviar.pack(padx=5, pady=10)	
		except:
			if cont_rubros>1:
				messagebox.showwarning("Aviso importante","El producto no pasó el control de calidad!\nSe marcará la carga como rechazada.")
				cursor.execute(f'UPDATE CUPOS SET ESTADO="R" WHERE PATENTE="{Patente}" AND ESTADO="A" AND FECHA="{Fecha_hoy}"')
			else:
				messagebox.showinfo("Control correcto", "La carga pasó el control de calidad!")
				cursor.execute(f'UPDATE CUPOS SET ESTADO="C" WHERE PATENTE="{Patente}" AND ESTADO="A" AND FECHA="{Fecha_hoy}"')
			conn.commit()
			valor=messagebox.askquestion("Calidad controlada", "¿Desea controlar la calidad de otra carga?")
			if valor == 'yes':
				Menu_Pat('Calidad')
			else:
				Volver_Menu()
	else:
		messagebox.showwarning("Error","Selecciona una opción!")

def Listar_rubros(Lista_rubros):
	for rubro in Lista_rubros:
		yield rubro

def PBruto(Patente):
	global Packed, PBru

	PBru=tk.Frame(root)
	PBru.pack(fill="both", expand=True)
	PBru.config(width=800, height=500, padx=5, pady=5)
	PBru.pack_propagate(0)
	Packed="PBru"
	Title=ttk.Label(PBru, text="REGISTRAR PESO BRUTO", font=("arial",20)).pack(padx=10, pady=10)

	cursor.execute(f'SELECT COD_PROD FROM CUPOS WHERE PATENTE="{Patente}" AND ESTADO="C" AND FECHA="{Fecha_hoy}"')
	Cod_prod = cursor.fetchone()
	if Cod_prod == None:
		valor=messagebox.askquestion("Error", "La patente ingresada no tiene que ingresar el peso bruto hoy!\n¿Desea ingresar otro camión?")
		if valor == 'yes':
			Menu_Pat('PBruto')
		else:
			Volver_Menu()

	Frame_pb = tk.Frame(PBru)
	Frame_pb.pack()
	PB = tk.StringVar()
	ttk.Label(Frame_pb, text="Peso bruto:", font=("arial",10)).pack(padx=5,pady=10, side='left', anchor='e')
	ttk.Entry(Frame_pb,textvariable=PB).pack(padx=5,pady=10,side='right', anchor='w')

	botonenviar=ttk.Button(PBru, text="Enviar", width=10, command=lambda:Validar_pb(Patente,PB.get()))
	botonenviar.pack(padx=5, pady=10)	

	botonmenu=ttk.Button(PBru, text="VOLVER AL MENÚ PRINCIPAL", width=29, command=Volver_Menu).pack(padx=5, pady=5)

def Validar_pb(Patente,Peso_Bruto):
	try:
		if float(Peso_Bruto)<2:
			messagebox.showwarning("Error", "El peso bruto no puede ser menor a 2kg")
		elif float(Peso_Bruto) > 50000:
			messagebox.showwarning("Error", "El peso bruto no puede ser mayor a 50.000kg")
		else:
			cursor.execute(f'UPDATE CUPOS SET PESO_BRUTO={Peso_Bruto},ESTADO="B" WHERE PATENTE="{Patente}" AND ESTADO="C" AND FECHA="{Fecha_hoy}"')
			conn.commit()
			valor=messagebox.askquestion("Peso bruto asignado correctamente", "¿Desea ingresar el de otro camión?")
			if valor == 'yes':
				Menu_Pat('PBruto')
			else:
				Volver_Menu()
	except:
		messagebox.showwarning("Error", "El peso bruto debe contener solamente números.")
		
def Tara(Patente):
	global Packed, Tar

	Tar=tk.Frame(root)
	Tar.pack(fill="both", expand=True)
	Tar.config(width=800, height=500, padx=5, pady=5)
	Tar.pack_propagate(0)
	Packed="Tar"
	Title=ttk.Label(Tar, text="REGISTRAR TARA", font=("arial",20)).pack(padx=10, pady=10)

	cursor.execute(f'SELECT PESO_BRUTO FROM CUPOS WHERE PATENTE="{Patente}" AND ESTADO="B" AND FECHA="{Fecha_hoy}"')
	Pbruto = cursor.fetchone()
	if Pbruto == None:
		valor=messagebox.askquestion("Error", "La patente ingresada no tiene que ingresar la tara hoy!\n¿Desea ingresar otro camión?")
		if valor == 'yes':
			Menu_Pat('Tara')
		else:
			Volver_Menu()
	chars = "(),'"
	Pbruto = ''.join( x for x in str(Pbruto) if x not in chars)
	Frame_tara = tk.Frame(Tar)
	Frame_tara.pack()
	Tara = tk.StringVar()
	ttk.Label(Frame_tara, text="Tara:", font=("arial",10)).pack(padx=5,pady=10, side='left', anchor='e')
	ttk.Entry(Frame_tara,textvariable=Tara).pack(padx=5,pady=10,side='right', anchor='w')

	botonenviar=ttk.Button(Tar, text="Enviar", width=10, command=lambda:Validar_tara(Patente,Tara.get(),Pbruto))
	botonenviar.pack(padx=5, pady=10)
	botonmenu=ttk.Button(Tar, text="VOLVER AL MENÚ PRINCIPAL", width=29, command=Volver_Menu).pack(padx=5, pady=5)

def Validar_tara(Patente,Tara,Peso_Bruto):
	try:
		if float(Tara)<1:
			messagebox.showwarning("Error", "La tara no puede ser menor a 1kg!")
		elif float(Tara) > float(Peso_Bruto):
			messagebox.showwarning("Error", "La tara no puede ser mayor al peso bruto!")
		else:
			cursor.execute(f'UPDATE CUPOS SET TARA={Tara},ESTADO="F" WHERE PATENTE="{Patente}" AND ESTADO="B" AND FECHA="{Fecha_hoy}"')
			conn.commit()
			cursor.execute(f'SELECT COD_PROD FROM CUPOS WHERE TARA={Tara} AND PATENTE="{Patente}" AND FECHA="{Fecha_hoy}"')
			Cod_prod = cursor.fetchone()
			chars = "(),'"
			Cod_prod = ''.join( x for x in str(Cod_prod) if x not in chars)
			cursor.execute(f'SELECT STOCK_SILO FROM SILOS WHERE COD_PROD={Cod_prod}')
			Stock = cursor.fetchone()
			Stock = ''.join( x for x in str(Stock) if x not in chars)
			Stock = int(Stock) + int(Peso_Bruto) - int(Tara)
			cursor.execute(f'UPDATE SILOS SET STOCK_SILO={Stock} WHERE COD_PROD={Cod_prod}')
			conn.commit()
			valor=messagebox.askquestion("Tara asignada correctamente", "¿Desea ingresar la de otro camión?")
			if valor == 'yes':
				Menu_Pat('Tara')
			else:
				Volver_Menu()
	except:
		messagebox.showwarning("Error", "La tara debe contener solamente números.")

def Reportes():
	global Packed, Rep

	Unpack()
	Rep=tk.Frame(root)
	Rep.pack(fill="both", expand=True)
	Rep.config(width=800, height=500, padx=5, pady=5)
	Rep.pack_propagate(0)
	Packed="Rep"
	Title=ttk.Label(Rep, text="REPORTES", font=("arial",20)).pack(padx=10, pady=10)

	chars = "(),"
	cursor.execute(f'SELECT MAX(NUM_CUPO) FROM CUPOS')
	Cant_Cupos = cursor.fetchone()
	cursor.execute(f'SELECT COUNT(NUM_CUPO) FROM CUPOS WHERE ESTADO<>"P"')
	Cant_Rec = cursor.fetchone()

	Cant_Cupos = ''.join( x for x in str(Cant_Cupos) if x not in chars)
	Cant_Rec = ''.join( x for x in str(Cant_Rec) if x not in chars)

	ttk.Label(Rep, text=f"Cantidad de cupos otorgados: {Cant_Cupos}", font=("arial",12)).pack(padx=10, pady=10)
	ttk.Label(Rep, text=f"Cantidad de camiones recibidos: {Cant_Rec}", font=("arial",12)).pack(padx=10, pady=10)
	Crear_arbol()


def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        showinfo(title='Información', message='Reportes de productos.')

def Listado_silos():
	global Packed, Lsil, Frame_calendar
	Unpack()
	Lsil=tk.Frame(root)
	Lsil.pack(fill="both", expand=True)
	Lsil.config(width=800, height=500, padx=5, pady=5)
	Lsil.pack_propagate(0)
	Packed="Lsil"
	Title=ttk.Label(Lsil, text="LISTADO DE SILOS Y RECHAZOS", font=("arial",20)).pack(padx=10, pady=10)
	cursor.execute(f'SELECT NOMBRE_SILO, STOCK_SILO FROM SILOS WHERE STOCK_SILO=(SELECT MAX(STOCK_SILO) FROM SILOS)')
	Mayor_stock = cursor.fetchone()
	Title=ttk.Label(Lsil, text=f"El silo que tiene el mayor stock actualmente es: {Mayor_stock[0]} con {Mayor_stock[1]}kg", font=("arial",14)).pack(padx=10, pady=15)
	Frame_calendar = tk.Frame(Lsil)
	Frame_calendar.pack()
	Title=ttk.Label(Frame_calendar, text=f"Seleccione una fecha para ver los camiones rechazados ese día", font=("arial",14)).pack(padx=10, pady=10)
	Cal = Calendar(Frame_calendar)
	Cal.pack(pady=20)
	Cal.config(headersbackground='#364c55', foreground='#000', background='#fff', headersforeground ='#fff')
	botonenviar = ttk.Button(Frame_calendar, text="Enviar", width=10, command=lambda:consultar_rechazados(Cal.get_date())).pack(padx=5, pady=10)

def consultar_rechazados(Fecha):
	global Frame_calendar, Lsil

	Fecha = Fecha.split('/')
	Fecha = f'{Fecha[1]}/{Fecha[0]}/{Fecha[2]}'
	cursor.execute(f'SELECT PATENTE FROM CUPOS WHERE ESTADO="R" AND FECHA="{Fecha}"')
	Lista_rechazados = cursor.fetchall()
	if Lista_rechazados == []:
		messagebox.showwarning("Aviso", f"No se rechazaron camiones el día {Fecha}.")
	else:
		Frame_calendar.pack_forget()
		Title=ttk.Label(Lsil, text=f"Lista de rechazados el día {Fecha}:", font=("arial",14)).pack(padx=10, pady=10)
		Listado = ttk.Combobox(
			master=Lsil,
			state="readonly",
			values=Lista_rechazados
			)
		Listado.pack(padx=5, pady=5)
		botonenviar = ttk.Button(Lsil, text="Elegir otro día", width=20, command=Listado_silos).pack(padx=5, pady=20)


def Crear_arbol():
	global tree

	Frame_tree = tk.Frame(Rep)
	Frame_tree.pack(fill="both", expand=True)
	Frame_tree.config(width=800, height=500, padx=5, pady=5)
	Frame_tree.pack_propagate(0)
	chars = "(),'"

	columns = ('Producto','Cantidad de camiones','Peso neto total','Promedio peso neto','Patente mayor descarga','Patente menor descarga')
	tree = ttk.Treeview(Frame_tree, columns=columns, show='headings')
	for column in columns:
		tree.column(f'{column}', anchor='center')
		tree.heading(f'{column}', text=f'{column}')

	tree.bind('<<TreeviewSelect>>', item_selected)
	tree.pack()

	Productos = [
	['Cebada'],
	['Girasol'],
	['Maíz'],
	['Soja'],
	['Trigo']
	]

	# Cantidad de camiones por producto

	for p in range(1,6):
		cursor.execute(f'SELECT COUNT(NUM_CUPO) FROM CUPOS WHERE COD_PROD={p} AND ESTADO<>"P"')
		Cant_cam = cursor.fetchone()
		Cant_cam = ''.join( x for x in str(Cant_cam) if x not in chars)
		Productos[p-1].append(str(Cant_cam))

	# Peso neto total
	
	for p in range(1,6):
		cursor.execute(f'SELECT SUM(PESO_BRUTO-TARA) FROM CUPOS WHERE COD_PROD={p} AND TARA<>0 GROUP BY COD_PROD')
		Peso_n = cursor.fetchone()
		if Peso_n!=None:
			Peso_n = ''.join( x for x in str(Peso_n) if x not in chars)
		else:
			Peso_n = 0
		Productos[p-1].append(str(Peso_n))

	# Promedio peso neto

	for p in range(1,6):
		cursor.execute(f'SELECT AVG(PESO_BRUTO-TARA) FROM CUPOS WHERE COD_PROD={p} AND TARA<>0 AND ESTADO<>"R" GROUP BY COD_PROD')
		Prom = cursor.fetchone()
		if Prom!=None:
			Prom = ''.join( x for x in str(Prom) if x not in chars)
		else:
			Prom = 0
		Productos[p-1].append(str(Prom))

	# Patentes

	# Mayor

	for p in range(1,6):
		cursor.execute(f'SELECT PATENTE FROM CUPOS WHERE COD_PROD={p} AND (PESO_BRUTO-TARA) = (SELECT MAX(PESO_BRUTO-TARA) FROM CUPOS WHERE COD_PROD={p})')
		Pat_may = cursor.fetchone()
		if Pat_may!=None:
			Pat_may = ''.join( x for x in str(Pat_may) if x not in chars)
		else:
			Pat_may = 0
		Productos[p-1].append(str(Pat_may))

	# Menor

	for p in range(1,6):
		cursor.execute(f'SELECT PATENTE FROM CUPOS WHERE COD_PROD={p} AND (PESO_BRUTO-TARA) = (SELECT MIN(PESO_BRUTO-TARA) FROM CUPOS WHERE COD_PROD={p} AND ESTADO="F")')
		Pat_men = cursor.fetchone()
		if Pat_men!=None:
			Pat_men = ''.join( x for x in str(Pat_men) if x not in chars)
		else:
			Pat_men = 0
		Productos[p-1].append(str(Pat_men))

	for prod in Productos:
		tree.insert('', tk.END, values=prod)

	botonmenu=ttk.Button(Frame_tree, text="VOLVER AL MENÚ PRINCIPAL", width=29, command=Volver_Menu).pack(pady=20)

def Notificacion():

	Mantenimiento = Notify(default_notification_icon="trigo.ico")
	Mantenimiento.title = "Función en construcción!"
	Mantenimiento.message = "Por favor intente nuevamente con otra opcion."
	Mantenimiento.send(block=False)

def main_window():
	global root, Rutabbdd
	root = tk.Tk()
	root.config(width=800, height=500, padx=5, pady=5)
	root.title("Sistema de gestión para cerealeras")
	root.iconbitmap("trigo.ico")
	#root.resizable(0,0)
	img = tk.PhotoImage(file="Fondo.png")
	#style = darkstyle(root)
	Rutabbdd = 'D:\Archivos_tp_GUI\Database.db'
	conn_bbdd()
	Menu()
	root.mainloop()

w.destroy()
main_window()
