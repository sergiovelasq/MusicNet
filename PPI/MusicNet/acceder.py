from tkinter import *
from tkinter import messagebox
from principal import *

from registro import *

from listademusicos import *
import listademusicos





def crearventana(ventana):
    ventana.title("MusicNet3")
    ventana.iconbitmap(r'c:\Sergio\Introduccion a la programacion\PPI\Guitar.ico')
    ventana.configure(background="goldenrod")
    ventana.config(width="800", height="400")
    ventana.config(bd=45, relief="sunken")

def crearpanellogin(ventana, principal, f1, f2):
    
    login=Frame(ventana, width=800, height=400)
    login.pack()
    login=Label(login, text="MusicNet4", fg="black", font=("Baskerville Old Face", 20)).place(x=350, y=10)
    
    usuariolabel=Label(login, text="Usuario: ", fg="black").place(x=250, y=150)
    
    ingresarusuario=Entry(login)
    ingresarusuario.pack()
    ingresarusuario.place(x=350 , y=150)
    ingresarusuario.config(justify="center")
    
    passwordlabel = Label(login, text="Contraseña: ", fg="black").place(x=250, y=200)
    
    passwordusuario = Entry(login)
    passwordusuario.pack()
    passwordusuario.place(x=350 , y=200)
    passwordusuario.config(show="*", justify="center")

    volver=Button(login, text="Volver", fg="Black", command=f1)
    volver.place(x=0 , y=0 )

    accedercomocliente=Button(login, text="Acceder como cliente", fg="black", command=f2)
    accedercomocliente.place(x=250 , y=300 )

    def funingresar(usuario, password):

        if (not (usuario) and not (usuario.strip())) or (not (password) and not (password.strip())):
            messagebox.showinfo("Error de ingreso", "\nIngrese el usuario. \nIngrese la contraseña")
        else:
            archivo=open("listausuarios.txt", "r")
            usuarios=archivo.readlines()

            registration=[]
            existe=False
            for line in usuarios:
                registration=line.split() #["admin"(posicion 0),"123"(posicion 1)]
                if registration[0]==usuario and registro[1]==password:
                    messagebox.showinfo("Usuario correcto", "\nBienvenido: "+usuario+"\nPuedes ingresar")
                    iniciarlistademusicos(ventana)
                    ventana.withdraw()
                    exite=True
                    break
            archivo.close()
        if not existe:
            messagebox.showinfo("El usuario no existe",
                                "\nEste usuario no existe. \n\nPor favor registrese.")

        ingresarusuario.delete(0, 'end')
        passwordusuario.delete(0, 'end')
    
    def registrarse():

        acceder.destroy()
        registro.iniciarregistro(principal)
    
    registrarse = Button(login, text="Registrarse", fg="black", command=registrarse())
    registrarse.place(x=300, y=250)

    def iniciarsesion():
        acceder.destroy()
        listademusicos.iniciarlistademusicos(principal)

    iniciarsesion=Button(login, text="Iniciar Sesión", fg="black", command=lambda: funingresar(ingresarusuario.get(), passwordusuario.get(), ventana, principal))
    iniciarsesion.place(x=400, y=350)


def iniciaracceder(principal):

    acceder=Toplevel()
    crearventana(acceder)
    

    def volver(event=None):
        acceder.destroy()
        principal.update()
        principal.deiconify()

    def accedercomocliente(event=None):
        acceder.destroy()
        listademusicos.iniciarlistademusicos(principal)
      
    crearpanellogin(acceder,  volver, accedercomocliente)

    
    
        

   

