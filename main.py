from msilib.schema import ListBox
import tkinter as ak
from tkinter import *
import csv
from tkinter import ttk
from tkinter import messagebox
from operator import itemgetter 


def opcion1():
    def eligeciudad():
        indices = listboxciudad.curselection()
        for i in indices:
             nombreciudad=listboxciudad.get(i)
    
        lblestudiantes=Label(ventanaNueva, text="Estudiantes segun ciudad "+nombreciudad).place(x=150, y=30)
    
        list=Listbox(ventanaNueva, height=10, width=60, selectmode=EXTENDED)
        list.place(x=140, y=50)
        list.delete(0,END)
        
        for alumno in alumnos:
            ciudad= alumno["ciudad"]
            if ciudad==nombreciudad:
                nombre = alumno["nombre"]
                apellido= alumno["apellido"]
                pais= alumno["pais"]
                edad = alumno["edad"]
                carrera=alumno["carrera"]
                list.insert(END, nombre+","+apellido+" de "+ciudad+"-"+pais+" ("+str(edad)+")"+" Prof:"+carrera)

    ventanaNueva= Toplevel(ventana)
    ventanaNueva.title="Listado de ciudades donde residen los estudiantes"
    ventanaNueva.geometry("600x300")
    
    listboxciudad = Listbox(ventanaNueva, selectmode=EXTENDED)
    listboxciudad.insert(0, *ciudades)

    listboxciudad.place(x=10,y=50)
    boton_obtener_seleccion = ttk.Button(ventanaNueva, text="Elija ciudad", command=eligeciudad)
    boton_obtener_seleccion.place(x=10, y=10, width=100, height=30)   


def opcion2():
    def eligepais():
        indices = listboxpais.curselection()
        for i in indices:
             nombrepais=listboxpais.get(i)
    
        lblestudiantes=Label(ventanaNueva, text="Estudiantes segun pais: "+nombrepais).place(x=150, y=30)
    
        list=Listbox(ventanaNueva, height=10, width=65, selectmode=EXTENDED)
        list.place(x=140, y=50)
        list.delete(0,END)
        for alumno in alumnos:
            pais= alumno["pais"]
            if pais==nombrepais:
                nombre = alumno["nombre"]
                apellido= alumno["apellido"]
                ciudad= alumno["ciudad"]
                edad = alumno["edad"]
                carrera=alumno["carrera"]
                list.insert(END, nombre+","+apellido+" de "+ciudad+"-"+pais+" ("+str(edad)+")"+" Prof:"+carrera)    
                

    ventanaNueva= Toplevel(ventana)
    ventanaNueva.title="Alumnos según Pais donde residen"
    ventanaNueva.geometry("600x300")
    
    listboxpais = Listbox(ventanaNueva, selectmode=EXTENDED)
    listboxpais.insert(0, *paises)
    listboxpais.place(x=10,y=50)
    boton_obtener_seleccion = ttk.Button(ventanaNueva, text="Elija pais", command=eligepais)
    boton_obtener_seleccion.place(x=10, y=10, width=100, height=30)   


def opcion3():
    def devolverDatos():
        textoCaja1=edad1.get()
        textoCaja2=edad2.get()
        lab2=Label(ventanaNueva, text="Alumnos entre: "+textoCaja1+" y "+textoCaja2+" años de edad").place(x=1, y=50)
        list=Listbox(ventanaNueva, height=10, width=60, selectmode=EXTENDED)
        list.place(x=1, y=70)
        for alumno in alumnos:
            edad = int(alumno["edad"])
            if edad>=int(textoCaja1) and edad<=int(textoCaja2):
                nombre = alumno["nombre"]
                apellido= alumno["apellido"]
                pais= alumno["pais"]
                ciudad= alumno["ciudad"]
                carrera=alumno["carrera"]
                list.insert(END, nombre+","+apellido+" de "+ciudad+"-"+pais+" ("+str(edad)+")"+" Prof:"+carrera)
        return(textoCaja1)
    
    ventanaNueva= Toplevel(ventana)
    ventanaNueva.title="Alumnos según el rango de edad"
    ventanaNueva.geometry("600x300")

    edad1=StringVar()
    edad2=StringVar()
    lab1=Label(ventanaNueva, text="Ingrese rango de edad:").place(x=1, y=10)
    #ENTRY 
    entryedad1=Entry(ventanaNueva, textvariable=edad1, width=10).place(x=140, y=10)
    entryedad2=Entry(ventanaNueva, textvariable=edad2, width=10).place(x=250, y=10)
    
    boton_obtener_seleccion = Button(ventanaNueva, text="Acepta", command=lambda:devolverDatos())
    boton_obtener_seleccion.place(x=450, y=10, width=100, height=30)   

def opcion4():
    ventanaNueva= Toplevel(ventana)
    ventanaNueva.title="Listado de ciudades donde residen los estudiantes"
    ventanaNueva.geometry("500x200")
        
    list=Listbox(ventanaNueva, height=10, width=60, selectmode=EXTENDED)
    list.place(x=1, y=10)
    for ciudad in ciudades:
        list.insert(END, ciudad)


def opcion5():
    def promediodecarrera():
        indices = listboxcarreras.curselection()
        for i in indices:
             nombrecarrera=listboxcarreras.get(i)
    
        sumaedades=0
        contador=0
        for alumno in alumnos:
            carrera=alumno["carrera"]
            if carrera==nombrecarrera:
                sumaedades=sumaedades+int(alumno["edad"])
                contador=contador+1

        promedio=int(sumaedades/contador)
        
        lblabel1=Label(ventanaNueva, text="Para la carrera: "+nombrecarrera, font=("Arial", 12)).place(x=150, y=48)
        lblpromedio=Label(ventanaNueva, text="El promedio de edad es: "+str(promedio)+" años", font=("Arial", 25)).place(x=150, y=70)
    
    
    ventanaNueva= Toplevel(ventana)
    ventanaNueva.title="Listado de carreras y promerio de edades"
    ventanaNueva.geometry("650x300")
    
    listboxcarreras = Listbox(ventanaNueva, selectmode=EXTENDED)
    listboxcarreras.insert(0, *carreras)
    listboxcarreras.place(x=10,y=50)

    boton_obtener_seleccion = ttk.Button(ventanaNueva, text="Elija carrera", command=promediodecarrera)
    boton_obtener_seleccion.place(x=10, y=10, width=100, height=30)   

def opcion6():

    def promediodecarrera():
        def verestado():
            indices = list.curselection()
            for i in indices:
                   estudiante=list.get(i)
            
            lblabel3=Label(ventanaNueva, text="El estudiante ("+estudiante+")", bg='#fff', fg='#f00').place(x=140, y=260)
            datos_edad=int(estudiante[1:3])
            if datos_edad>promedio:
                lblabel4=Label(ventanaNueva, text="está por encima del promedio", bg='#fff', fg='#f00', font=("Arial", 14)).place(x=350, y=255)
            else:
                lblabel5=Label(ventanaNueva, text="está por debajo del promedio", bg='#fff', fg='#f00', font=("Arial", 14)).place(x=350, y=255)
                                
                

        indices = listboxcarreras.curselection()
        for i in indices:
             nombrecarrera=listboxcarreras.get(i)
    
        sumaedades=0
        contador=0
        for alumno in alumnos:
            carrera=alumno["carrera"]
            if carrera==nombrecarrera:
                sumaedades=sumaedades+int(alumno["edad"])
                contador=contador+1
        promedio=int(sumaedades/contador)

        lblabel1=Label(ventanaNueva, text="Carrera ("+nombrecarrera+") el promedio de edad es ("+str(promedio)+" años)", bg='#fff', fg='#f00').place(x=137, y=30)

        list=Listbox(ventanaNueva, height=10, width=80, selectmode=EXTENDED)
        list.place(x=140, y=50)
        list.delete(0,END)
        for alumno in alumnos:
            carrera=alumno["carrera"]
            if carrera==nombrecarrera:
                nombre = alumno["nombre"]
                apellido= alumno["apellido"]
                edad = alumno["edad"]
                list.insert(END, "("+str(edad)+")"+" "+nombre+","+apellido)
        
        boton_estado = ttk.Button(ventanaNueva, text="Ver Estado del Estudiante", command=verestado)
        boton_estado.place(x=140, y=220, width=150, height=30)   

    ventanaNueva= Toplevel(ventana)
    ventanaNueva.title="Listado de carreras y promedio de edad del estudiante"
    ventanaNueva.geometry("650x320")
    
    listboxcarreras = Listbox(ventanaNueva, selectmode=EXTENDED)
    listboxcarreras.insert(0, *carreras)
    listboxcarreras.place(x=10,y=50)

    boton_obtener_seleccion = ttk.Button(ventanaNueva, text="Elija carrera", command=promediodecarrera)
    boton_obtener_seleccion.place(x=10, y=10, width=100, height=30)   

def opcion7():
    ventanaNueva= Toplevel(ventana)
    ventanaNueva.title="Listado de carreras y promedio de edad del estudiante"
    ventanaNueva.geometry("650x400")

    lblabel1=Label(ventanaNueva, text="(Edades entre 18-25)").place(x=10, y=10)
    lblabel2=Label(ventanaNueva, text="(Edades entre 26-35)").place(x=200, y=10)
    lblabel3=Label(ventanaNueva, text="(Mayores de 35)").place(x=400, y=10)


    list_18_25 = Listbox(ventanaNueva, height=20, width=30, selectmode=EXTENDED)
    list_18_25.place(x=10, y=30)
    list_26_35=Listbox(ventanaNueva, height=20, width=30, selectmode=EXTENDED)
    list_26_35.place(x=200, y=30)
    list_mayores35=Listbox(ventanaNueva, height=20, width=30, selectmode=EXTENDED)
    list_mayores35.place(x=400, y=30)
    for alumno in alumnos:
        edad=int(alumno["edad"])
        if edad>=18 and edad<=25:
            nombre = alumno["nombre"]
            apellido= alumno["apellido"]
            edad = alumno["edad"]
            list_18_25.insert(END, "("+str(edad)+")"+" "+nombre+","+apellido)
        elif edad>=26 and edad<=35:
            nombre = alumno["nombre"]
            apellido= alumno["apellido"]
            edad = alumno["edad"]
            list_26_35.insert(END, "("+str(edad)+")"+" "+nombre+","+apellido)
        elif edad>35:
            nombre = alumno["nombre"]
            apellido= alumno["apellido"]
            edad = alumno["edad"]
            list_mayores35.insert(END, "("+str(edad)+")"+" "+nombre+","+apellido)
        


def opcion8():
    ventanaNueva= Toplevel(ventana)
    ventanaNueva.title="Listado de carreras y promerio de edades"
    ventanaNueva.geometry("650x300")
    
    #listboxcarreras = Listbox(ventanaNueva, selectmode=EXTENDED)
    #listboxcarreras.insert(0, *carreras)
    #listboxcarreras.place(x=10,y=50)
    
    #ordeno lista alumnos por ciudad
    ordenados_ciudad = sorted(alumnos, key=lambda campociudad : campociudad['ciudad'])

    lista_ciudad_carreras=[]
    for alumno in ordenados_ciudad:
        ciudad = alumno["ciudad"]
        carrera= alumno["carrera"]
        lista_ciudad_carreras.append((
            ciudad,
            carrera
        ))

    ordanodo_porcarreras=sorted(lista_ciudad_carreras, key=itemgetter(0,1))
    
    list_resumen_carreras=[]
    bandera_ciudad=""
    bandera_carreras=""
    contador_carreras=0
    pasa=1
    for lista in ordanodo_porcarreras:
        nombreciudad=lista[0]
        nombrecarrera=lista[1]
        if pasa==1:
            bandera_ciudad=nombreciudad
            pasa=0
        if bandera_ciudad==nombreciudad:
            if nombrecarrera!=bandera_carreras:
                bandera_carreras=nombrecarrera
                contador_carreras=contador_carreras+1
        else:
            list_resumen_carreras.append((bandera_ciudad,contador_carreras))
            bandera_ciudad=nombreciudad
            contador_carreras=0
            pasa=1
    list_resumen_carreras.append((bandera_ciudad,contador_carreras))
    
    sort_por_carreras=sorted(list_resumen_carreras, key=itemgetter(1), reverse=True)
    
    lblabel1=Label(ventanaNueva, text="Ciudades que con mayor variedades de carreras ").place(x=10, y=10)
    list = Listbox(ventanaNueva, height=20, width=50, selectmode=EXTENDED)
    list.place(x=10, y=30)

    for lista in sort_por_carreras:
        nombreciudad=lista[0]
        cantidad_carreras=lista[1]
        list.insert(END, "Ciudad de "+nombreciudad+" ofrece ("+str(cantidad_carreras)+") carreras")
        


    #ordenados_carreras = sorted(lista_ciudad_carreras, key=lambda porcarreras : porcarreras['carrera'])
 


# programa principal
ventana = Tk()

ventana.title('Información de estudiantes')
wtotal = ventana.winfo_screenwidth()
htotal = ventana.winfo_screenheight()
wventana = 900
hventana = 300
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)

separador = ","
with open("data.csv", encoding="utf-8") as archivo:
    next(archivo)  # Omitir encabezado del archivo
    alumnos = []
    ciudades = set([])
    paises=set([])
    carreras=set([])
    listbox = []
    for linea in archivo:
        linea = linea.rstrip("\n")  # Quitar salto de línea
        columnas = linea.split(separador)
        nombre = columnas[0]
        apellido = columnas[1]
        ciudad = columnas[2]
        pais = columnas [3]
        edad = int(columnas[4])
        carrera = columnas[5]
        alumnos.append({
        "nombre": nombre,
        "apellido": apellido,
        "ciudad": ciudad,
        "pais": pais,
        "edad": edad,
        "carrera": carrera,
        })
        ciudades.add(ciudad)
        paises.add(pais)
        carreras.add(carrera)
        
    
ventana.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
ventana.overrideredirect(True)
menubar = Menu(ventana)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="1) Obtener todos los estudiantes que pertenezcan a una ciudad dada", command=opcion1)
filemenu.add_command(label="2) Obtener todos los estudiantes que vivan en un país dado", command=opcion2)
filemenu.add_command(label="3) Obtener todos los estudiantes que estén dentro del rango de edades dado", command=opcion3)
filemenu.add_command(label="4) Obtener todas las ciudades de residencia de los estudiantes", command=opcion4)
filemenu.add_command(label="5) Identificar la edad promedio por carrera", command=opcion5)
filemenu.add_command(label="6) Indicar por carrera si el estudiante está por encima o por debajo del promedio de edad", command=opcion6)
filemenu.add_command(label="7) Agrupa los estudiantes en diferentes rangos de edad (18-25, 26-35, mayores de 35)", command=opcion7)
filemenu.add_command(label="8) Identifica la ciudad que tienen la mayor variedad de carreras universitarias entre los estudiantes", command=opcion8)
filemenu.add_command(label="Salir", command=ventana.quit)

menubar.add_cascade(label="Información de los Estuadiantes", menu=filemenu)

ventana.config(menu=menubar)

ventana.mainloop()

    





