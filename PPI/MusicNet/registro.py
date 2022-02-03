from tkinter import *
import tkinter
from acceder import *
import acceder

def crearventana(ventana):
    ventana.title("MusicNet5")
    ventana.iconbitmap(r'c:\Sergio\Introduccion a la programacion\PPI\Guitar.ico')
    ventana.configure(background="goldenrod")
    ventana.config(width="800", height="400")
    ventana.config(bd=45, relief="sunken")

def crearpanelregistrarse(ventana, root1, f1):
    
    miframe=Frame(ventana, bd=1, relief=RAISED, background="goldenrod")
    miframe.place(in_=ventana, anchor="c", relx=.5, relt=.5)

    usuariolabel = Label(miframe, text="Usuario: ", background="goldenrod")
    usuariolabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    cuadrousuario=Entry(miframe)
    cuadrousuario.grid(row=0, column=1, pady=10)
    cuadrousuario.config(justify="center")

    contraseñalabel = Label(miframe, text="Contraseña: ", background="goldenrod")
    contraseñalabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

    cuadrocontraseña=Entry(miframe)
    cuadrocontraseña.grid(row=2, column=1, padx=10, pady=10)
    cuadrocontraseña.config(show="*", justify="center")

    botoncancelar = Button(miframe, text="Cancelar: ", fg="goldenrod", bg="blue", command=f1)
    botoncancelar.grid(row=3, column=0, sticky="w", padx=10, pady=10)

    botonregistrarse=Button(miframe, text="Registrarse", fg="blue", bg="goldenrod", command=lambda: validarregistro(cuadrousuario.get(), cuadrocontraseña.get(), ventana, root1))
    botonregistrarse.grid(row=3, column=1, sticky="w", padx=10, pady=10)

    def limpiarcampos():
        cuadrousuario.delete(0, 'end')
        cuadrocontraseña.delete(0, 'end')

    botonlimpiar=Button(miframe, text="Limpiar", fg="blue", bg="goldenrod", command=limpiarcampos())
    botonlimpiar.grid(row=3, column=2, sticky="w", padx=10, pady=10)



def validarregistro(usuario, password, ventana, root1):

    if ((not usuario or not usuario.strip())and (not password or not password.strip())):
        tkinter.messagebox.showinfo("Error de registro", "\nIngrese el usuario. \n\nIngrese el password.")
    else:
        archivo=open("listausuarios.txt", "r")
        usuarios=archivo.readlines()

        registar=[]
        existe=False
        for line in usuarios:
            registrar=line.split()
            if registrar[0]==usuario:
                tkinter.messagebox.showinfo("Registro incorrecto", "\nYa existe un usuario con ese nombre de usuario." "\n\nIntente con un nombre de usuario diferente.")

                exite=True
                break
            else:
                if registrar[1]==password:
                    tkinter.messagebox.showinfo("Registro incorrecto", "\nYa existe un usuario con esa contraseña." "\n\nIntente con una contraseña diferente.")

                    exite=True
                    break
        archivo.close()
            
        if not existe:
            tkinter.messagebox.showinfo("Usuario regitrado", "\nFelicitaciones." "\n\nRegistro exitoso.")
            archivo=open("listausuarios.txt", "a+") 
            archivo.writelines("\n"+usuario+" "+password)
            archivo.close()
            ventana.destroy()
            root1.update()
            root1.deiconify()

def iniciarregistro(principal):

    registro=Toplevel()
    crearventana(registro)

    def volver(event=None):

        registro.destroy()
        acceder.iniciaracceder(principal)

    crearpanelregistrarse(registro, volver)
