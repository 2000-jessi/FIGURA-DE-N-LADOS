import tkinter as tk
from tkinter import *
from turtle import *
import turtle as turtle
#EL PROGRAMA DIBUJA CUALQUIER FIGRUA REGULAR DE N LADOS
class VentanaEjemplo:
    def __init__(self, master):
         
        self.master = master
        master.title("FIGURA N LADOS")
        self.etiqueta = Label(master, text="SELECCIONA CON QUE ALGORITMO DESEAS DIBUJAR LA FIGURA DE N LADOS")
        self.etiqueta.pack()
        self.botonDDA = Button(master, text="DDA", command=self.DDA,bg="#006",fg="white")
        self.botonDDA.pack()
        self.botonBresenham = Button(master, text="BRESENHAM", command=self.Bresenham,bg="#006",fg="white")
        self.botonBresenham.pack()
        self.botonCerrar = Button(master, text="CERRAR", command=master.quit,bg="#006",fg="white")
        self.botonCerrar.pack()

    def DDA(self):
        self.master.destroy()
        title("DDA")
        lados = int(input("\nDIGITE LOS LADOS DE LA FIGURA: "))
        turtle.speed(1)
        turtle.pensize(3)
        turtle.pencolor("green")
        turtle.bgcolor("lightblue")
        angulo = 180-(((lados-2)/lados)*180) 
        print("COORDENADAS")
        
        for i in range(lados):
            turtle.left(angulo)
            turtle.fd(50)
            hideturtle()
            dot(12,0,0,0)
            p=turtle.pos ()
            print('\n'+str(p))

    def Bresenham(self):
        self.master.destroy()
        title("BRESENHAM")
        lados = int(input("\nDIGITE LOS LADOS DE LA FIGURA: "))
        turtle.speed(1)
        turtle.pensize(3)
        turtle.pencolor("blue")
        turtle.bgcolor("lightblue")
        angulo = 180-(((lados-2)/lados)*180) 
        print("COORDENADAS")
        
        for i in range(lados):
            turtle.left(angulo)
            turtle.fd(50)
            hideturtle()
            dot(12,0,0,0)
            p=turtle.pos ()
            print('\n'+str(p))

root = Tk()
root.configure(background="lightblue")
miVentana = VentanaEjemplo(root)   
root.mainloop()