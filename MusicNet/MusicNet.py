
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pickle

principal =tk.Tk()

principal.title("MusicNet")
principal.iconbitmap(r'c:\Sergio\Introduccion a la programacion\PPI\Guitar.ico')
principal.config(bg="goldenrod")
principal.config(width="800", height="400")
principal.config(bd=45, relief="sunken")

interfaz = Frame(principal, width=800, height=400)
interfaz.pack()
titulo=tk.Label(interfaz, text="MusicNet", fg="black", font=("Baskerville Old Face", 20)).place(x=350, y=10)
texto=tk.Label(interfaz, text="Descripción de la app", fg="black", font=("Lucida Fax", 15)).place(x=300, y=200)

def ventanaAcceder():
    principal.withdraw()
    ventana1=tk.Tk()
    ventana1.title("MusicNet")
    ventana1.iconbitmap(r'c:\Sergio\Introduccion a la programacion\PPI\Guitar.ico')
    ventana1.config(bg="goldenrod")
    ventana1.config(width="800", height="400")
    ventana1.config(bd=45, relief="sunken")
    
    ventana1 = Frame(ventana1, width=800, height=400)
    ventana1.pack()
    titulo1=tk.Label(ventana1, text="Acceso", fg="black", font=("Baskerville Old Face", 20)).place(x=360, y=10)
    botoncliente=tk.Button(ventana1, text="Acceder como cliente", command=ventanaListaDeMusicos, width=18, height=2).place(x=350, y=350)
    botonatras=tk.Button(ventana1, text="Atras", command=(ventana1.quit and principal.update and principal.deiconify), width=5, height=2).place(x=10, y=10)

    NombreUsuario=tk.Label(ventana1, text='Nombre de usuario:', font=('Arial', 14)).place(x=100, y=120)
    Contraseña=tk.Label(ventana1, text='Contraseña', font=('Arial', 14)).place(x=100, y=180)
   
    var_usr_name = tk.StringVar()
    var_usr_name.set('')
    entry_usr_name = tk.Entry(ventana1, text="Nombre de usuario", font=('Arial', 14))
    entry_usr_name.place(x=300,y=120)

    var_usr_pwd = tk.StringVar()
    entry_usr_pwd = tk.Entry(ventana1, text="Contraseña", font=('Arial', 14), show='*')
    entry_usr_pwd.place(x=300, y=180)


    def usr_login():
        
        usr_name = var_usr_name.get()
        usr_pwd = var_usr_pwd.get()

        try:

            with open('usrs_info.pickle', 'rb') as usr_file:
                usrs_info = pickle.load(usr_file)

        except FileNotFoundError:

            with open('usrs_info.pickle', 'wb') as usr_file:

                usrs_info = {'admin': 'admin'}
                pickle.dump(usrs_info, usr_file)
                usr_file.close()   

        if usr_name in usrs_info:

            if usr_pwd == usrs_info[usr_name]:

                tkinter.messagebox.showinfo(title='Bienvenido', message='Todo en armonía? ' + usr_name)

                ventanaListaDeMusicos
            else:

                tkinter.messagebox.showerror(message='Error, tu contraseña no es correcta, intenta de nuevo.')

        else: 

            is_sign_up = tkinter.messagebox.askyesno('Bienvenido! ', 'Aún no te has registrado, quieres hacerlo?')

            if is_sign_up :

                usr_sign_up()

    def usr_sign_up():
    
        def Ingresar_Listademusicos():

            np = new_pwd.get()
            npf = new_pwd_confirm.get()
            nn = new_name.get()


            with open('usrs_info.pickle', 'rb') as usr_file:

                exist_usr_info = pickle.load(usr_file)

            if np != npf:

                tkinter.messagebox.showerror('Error', 'Las contraseñas deben coincidir!')

            elif nn in exist_usr_info:

                tkinter.messagebox.showerror('Error', 'El usuario ya está registrado!')

            else:

                exist_usr_info[nn] = np

                with open('usrs_info.pickle', 'wb') as usr_file:

                    pickle.dump(exist_usr_info, usr_file)

                tkinter.messagebox.showinfo('Bienvenido', 'Te has regitrado exitosamente!')

                Ventana_registro.destroy()

        Ventana_registro = tk.Toplevel(ventana1)
        Ventana_registro.geometry('800x400')
        Ventana_registro.title('Registro')
        Ventana_registro.config(bd=45, relief="sunken")
        Ventana_registro.iconbitmap(r'c:\Sergio\Introduccion a la programacion\PPI\Guitar.ico')

        new_name =tk.StringVar()  
        new_name.set('')   
         

        tk.Label(Ventana_registro, text='Nombre de usuario: ').place(x=10, y=10)  
        entry_new_name = tk.Entry(Ventana_registro, text="Nuevo nombre") 
        entry_new_name.place(x=130, y=10)  
    

        new_pwd = tk.StringVar()
        tk.Label(Ventana_registro, text='Contraseña: ').place(x=10, y=50)
        entry_usr_pwd =tk.Entry(Ventana_registro, text="Nueva contraseña", show='*')
        entry_usr_pwd.place(x=130, y=50)
        
        new_pwd_confirm = tk.StringVar()
        tk.Label(Ventana_registro, text='Confirmar contraseña: ').place(x=10, y=90)
        entry_usr_pwd_confirm = tk.Entry(Ventana_registro, text="Confirmar contraseña", show='*')
        entry_usr_pwd_confirm.place(x=130, y=90)

        btn_comfirm_sign_up =tk. Button(Ventana_registro, text='Registrarse', command=Ingresar_Listademusicos)
        btn_comfirm_sign_up.place(x=180, y=120)

    
    boton_iniciar_sesion = tk.Button(ventana1, text='Iniciar Sesión', command=(usr_login), width=10, height=2)
    boton_iniciar_sesion.place(x=400, y=250)
    boton_registrarse = tk.Button(ventana1, text='Registrarse', command=usr_sign_up, width=10, height=2)
    boton_registrarse.place(x=300, y=250)




booncontinuar=Button(principal, text="Continuar", command=ventanaAcceder,  width=12, height=2).place(x=350, y=250)


def ventanaListaDeMusicos():
   
    ventana3=Tk()
    ventana3.title("MusicNet")
    ventana3.iconbitmap(r'c:\Sergio\Introduccion a la programacion\PPI\Guitar.ico')
    ventana3.config(bg="goldenrod")
    ventana3.config(width="800", height="400")
    ventana3.config(bd=45, relief="sunken")

    ventana3 = Frame(ventana3, width=800, height=400)
    ventana3.pack()
    titulo3=tk.Label(ventana3, text="Lista de musicos", fg="black", font=("Baskerville Old Face", 20)).place(x=350, y=10)
    texto3=tk.Label(ventana3, text="------------", fg="black", font=("Lucida Fax", 15)).place(x=300, y=200)

    botonatras2=Button(ventana3, text="Atras", command=ventanaAcceder, width=5, height=2).place(x=10, y=10)
    continuar=Button(ventana3, text="Continuar", command=ventanaPerfilDeMusico,  width=12, height=2).place(x=350, y=250)

def ventanaPerfilDeMusico():
    
    ventana4=Tk()
    ventana4.title("MusicNet")
    ventana4.iconbitmap(r'c:\Sergio\Introduccion a la programacion\PPI\Guitar.ico')
    ventana4.config(bg="goldenrod")
    ventana4.config(width="800", height="400")
    ventana4.config(bd=45, relief="sunken")

    ventana4 = Frame(ventana4, width=800, height=400)
    ventana4.pack()
    titulo4=tk.Label(ventana4, text="Perfil de Musico", fg="black", font=("Baskerville Old Face", 20)).place(x=350, y=10)
    texto4=tk.Label(ventana4, text="----------------", fg="black", font=("Lucida Fax", 15)).place(x=300, y=200)


    botonatras3=Button(ventana4, text="Atras", command=ventanaListaDeMusicos, width=5, height=2).place(x=10, y=10)
    continuar=Button(ventana4, text="Continuar", command=ventanaInfoContacto,  width=12, height=2).place(x=350, y=250)


def ventanaInfoContacto():
    
    ventana5=Tk()
    ventana5.title("MusicNet")
    ventana5.iconbitmap(r'c:\Sergio\Introduccion a la programacion\PPI\Guitar.ico')
    ventana5.config(bg="goldenrod")
    ventana5.config(width="800", height="400")
    ventana5.config(bd=45, relief="sunken")

    ventana5 = Frame(ventana5, width=800, height=400)
    ventana5.pack()
    titulo5=tk.Label(ventana5, text="Información de contacto", fg="black", font=("Baskerville Old Face", 20)).place(x=350, y=10)
    texto5=tk.Label(ventana5, text="------------", fg="black", font=("Lucida Fax", 15)).place(x=300, y=200)

    botonatras4=Button(ventana5, text="Atras", command=ventanaPerfilDeMusico, width=5, height=2).place(x=10, y=10)





principal.mainloop()
    


