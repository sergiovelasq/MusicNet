from acceder import *
from tkinter import *
from ayudas import *


principal = Tk()

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
    textotitulo=Label(titulo, text="Descripcion", font=("Times New Roman", 70),
                      fg=gold4, bg=goldenrod)
    textotitulo.grid(row=0, column=0, padx=10, pady=10)

    def funcontinuar(event=None):
        iniciaracceder()
        ventana.withdraw()

    panelboton=Frame(ventana, bg=goldenrod)
    panelboton.place(in_=ventana, anchor="c", relx=0.9, rely=0.9)
    continuar=Button(panelboton, text="Continuar", command=funcontinuar())
    continuar.grid(row=0, column=0, padx=10, pady=10)

def crearbarra(ventana):
    barra=Frame(ventana, bd=1, relief=RAISED)
    barra.pack(side=TOP, fill=X)

    def salir():
        ventana.quit()

    salir=Button(barra, text="Salir", command=salir)
    salir.pack(side=RIGHT, padx=2, pady=2)

    barra.pack(side=TOP, fill=X)

crearventana(principal)
crearbarra(principal)


principal.mainloop()