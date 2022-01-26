
from tkinter import *
from ayudas import *
import acceder
import listademusicos

def crearventana(ventana):

    ventana.title("MusicNet")
    ventana.configure(bg=goldenrod)

    anchoventana=ventana.winfo_reqwidth()
    altoventana=ventana.winfo_reqheight()

    positionderecha=int(ventana.winfo_screenwidth()/2-anchoventana/2)
    positionabajo=int(ventana.winfo_reqheight()/2-altoventana/2)

    ventana.geometry("1000x600".format(positionderecha, positionabajo))
    ventana.wm_attributes('-toolwindow', 1)

    titulo=Frame(ventana, bg=goldenrod)
    titulo.place(in_=ventana, anchor="c", relx=0.5, rely=0.2)
    textotitulo=Label(titulo, text="Registro", font=("Times New Roman", 70),
                      fg=gold4, bg=goldenrod)
    textotitulo.grid(row=0, column=0, padx=10, pady=10)

def crearbarra(ventana, f1, f2):
    barra=Frame(ventana, bd=1, relief=RAISED)
    barra.pack(side=TOP, fill=X)

    volver=Button(barra, text="volver", command=f1)
    volver.pack(side=LEFT, padx=2, pady=2)

    siguiente = Button(barra, text="Siguiente", command=f2)
    siguiente.pack(side=RIGHT, padx=2, pady=2)

    barra.pack(side=TOP, fill=X)

def iniciarregistro(principal):

    registro = Toplevel()
    crearventana(registro)

    def volver(event=None):

        registro.destroy()
        acceder.iniciaracceder(principal)

    def siguiente(event=None):

        registro.destroy()
        listademusicos.iniciarlistademusicos(principal)

    crearbarra(registro, volver, siguiente)