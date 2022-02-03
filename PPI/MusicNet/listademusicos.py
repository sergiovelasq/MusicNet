import tkinter
from tkinter import *
from acceder import *
from registro import *
import acceder
import registro

def crearventana(ventana):
    ventana.title("MusicNet7")
    ventana.iconbitmap(r'c:\Sergio\Introduccion a la programacion\PPI\Guitar.ico')
    ventana.configure(background="goldenrod")
    ventana.config(width="800", height="400")
    ventana.config(bd=45, relief="sunken")


def iniciarlistademusicos(principal):
    
    listademusicos=Toplevel()
    crearventana(listademusicos)

    def volver(event=None):
        listademusicos.destroy()
        acceder.iniciaracceder(principal)



    