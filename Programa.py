###############################################################################################
#
#-----------------------DOCUMENTACIÓN INTERNA------------------------------
#
#    Nombre del programa: ProyectoFinal
#
#    Lenguaje: Python 3.9
#
#    Programadores: Diego Fernando Patzán Marroquín            23525 / pat23525@uvg.edu.gt
#                   Ihan Gilberto Alexander Marroquín Sequén   23108 / mar23108@uvg.edu.gt
#                   Isabella Recinos Rodríguez                 23003 / rec23003@uvg.edu.gt
#                   Milton Giovanni Polanco Serrano            23471 / pol23471@uvg.edu.gt
#
#    Fin en mente: Proyecto final (AgriPro)
#
#    Recursos: Investigación previa
#              Entrevistas
#              
#    Historial de modificación: [000] Nuevo programa 29/04/2023
###############################################################################################
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import csv

class app(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.geometry("1000x700")
        self.configure(bg="limegreen")
        self.title("AgriPro")
        
        #Button(text="⌂", font=("Arial 20 bold"), width=2, height=1).place(x=20, y=20)
        
        Label(text="Registro", font=("Purisa 30 bold"), bg="limegreen", fg="darkgreen").place(x=390, y=100)
        
        
        Label(text="Usuario", font=("Purisa", 20 ,"bold"), bg="limegreen").place(x=250, y=300)
        self.user = Entry(width=20, borderwidth=0, font=("Purisa", 20 ,"bold")); self.user.place(x=470, y=300)
        
        Label(text="Contraseña", font=("Purisa", 20 ,"bold"), bg="limegreen").place(x=250, y=400)
        self.password = Entry(width=20, borderwidth=0, font=("Purisa", 20 ,"bold")); self.password.place(x=470, y=400)
        self.password['show'] = '*'
        
        self.btn_login = Button(text="Entrar", font=("Purisa", 20 ,"bold"), bg="darkgreen", fg="white", command=self.login).place(x=420, y=525)
        self.btn_new_account = Button(text="Crear cuenta", font=("Purisa", 15 ,"underline"), bg="limegreen", fg="black", borderwidth=0, command=self.nueva_cuenta).place(x=410, y=600)

    def login(self):
        user = self.user.get()
        password = self.password.get()

        bienvenida = False

        with open("usuarios.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for c in csv_reader:
                if c[8].split() == user.split() and c[9].split() == password.split():
                    bienvenida = True
            if bienvenida:
                self.v2 = Toplevel()
                self.v2.geometry("1000x700")
                self.v2.configure(bg="limegreen")
                self.v2.title("AgriPro")
            else:
                messagebox.showerror("Error", "Usuario no existente")
            self.user.delete(0, END)
            self.password.delete(0, END)

    def nueva_cuenta(self):
        self.v3 = Toplevel()
        self.v3.geometry("1000x700")
        self.v3.configure(bg="limegreen")
        self.v3.title("AgriPro")

        Label(self.v3, text="Ingrese todos los datos solicitados: ", bg="limegreen").place(x=20, y=20)
        self.e31 = Entry(self.v3, width=30, font=("Arial",20)); self.e31.place(x=20, y=50)
        self.e31.insert(0, "Nombre completo")
        Label(self.v3, text="Fecha de nacimiento: ", bg="limegreen").place(x=20, y=20)
        self.e321 = ttk.Combobox()

app().mainloop()