import tkinter as tk
from tkinter import messagebox

def agregar_nombre():
    nombre = entry_nombre.get()

   
    if nombre in nombres:
        messagebox.showerror("Error", "¡El nombre ya ha sido ingresado! Ingrese un nombre diferente.")
    else:
        nombres.append(nombre)
        entry_nombre.delete(0, tk.END)  

def mostrar_resultados():
    mensaje = "Nombres ingresados:\n" + "\n".join(nombres)
    messagebox.showinfo("Nombres Ingresados", mensaje)

ventana = tk.Tk()
ventana.title("Ingresar Nombres Únicos")

etiqueta_nombre = tk.Label(ventana, text="Ingrese el nombre:")
entry_nombre = tk.Entry(ventana)
etiqueta_nombre.grid(row=0, column=0, padx=10, pady=5)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

boton_agregar = tk.Button(ventana, text="Agregar Nombre", command=agregar_nombre)
boton_agregar.grid(row=1, column=0, columnspan=2, pady=10)

boton_mostrar_resultados = tk.Button(ventana, text="Mostrar Resultados", command=mostrar_resultados)
boton_mostrar_resultados.grid(row=2, column=0, columnspan=2, pady=10)

nombres = []

ventana.mainloop()
