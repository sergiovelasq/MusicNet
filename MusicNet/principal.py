
from tkinter import *
import acceder
from acceder import *
from tkinter import messagebox
from registro import *



principal = tkinter.Tk()

def crearventana(ventana):
    ventana.title("MusicNet")
    ventana.iconbitmap(r'c:\Sergio\Introduccion a la programacion\PPI\Guitar.ico')
    ventana.configure(background="goldenrod")
    ventana.config(width="800", height="400")
    ventana.config(bd=45, relief="sunken")
    
    interfaz = Frame(ventana, width=800, height=400)
    interfaz.pack()
    Label(interfaz, text="MusicNet", fg="black", font=("Baskerville Old Face", 20)).place(x=350, y=10)
    Label(interfaz, text="Descripción de la app", fg="black", font=("Lucida Fax", 15)).place(x=300, y=200)
   

    def continuar():

        iniciaracceder(ventana)
        ventana.withdraw()

    continuar=Button(ventana, text="Continuar", command=continuar)
    continuar.pack()
    continuar.place(x=370, y=320)


    def salir():
        respuesta=messagebox.askquestion("Salir", "\n¿Seguro que quieres salir?")
        if respuesta=="yes":
            ventana.quit()

        salir=Button(ventana, text="Salir", command=salir)
        salir.pack()
        salir.place(in_=ventana, anchor="c", relx=0.05, rely=0.05)
     
    

crearventana(principal)
principal.mainloop()
    


