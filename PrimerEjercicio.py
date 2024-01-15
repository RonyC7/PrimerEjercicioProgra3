import tkinter as tk
from tkinter import messagebox
from collections import Counter

def encontrar_mayor_menor_repetido():

    numeros = [float(entry.get()) for entry in entradas]

    numero_mayor = max(numeros)
    numero_menor = min(numeros)

    numeros_contador = Counter(numeros)
    numero_repetido, cantidad_repeticiones = numeros_contador.most_common(1)[0]

    mensaje = f"El número  con valor mayor es: {numero_mayor}\nEl número  con valor menor es: {numero_menor}\nEl número que se repite más veces es: {numero_repetido} (Se repite {cantidad_repeticiones} veces)"
    messagebox.showinfo("Resultado", mensaje)

ventana = tk.Tk()
ventana.title("Encontrar Mayor, Menor y Número Repetido")

etiquetas = [tk.Label(ventana, text=f"Ingrese el número {i + 1}:") for i in range(10)]
entradas = [tk.Entry(ventana) for _ in range(10)]

for i in range(10):
    etiquetas[i].grid(row=i, column=0, padx=10, pady=5)
    entradas[i].grid(row=i, column=1, padx=10, pady=5)

boton_calculo = tk.Button(ventana, text="Calcular", command=encontrar_mayor_menor_repetido)
boton_calculo.grid(row=10, column=0, columnspan=2, pady=10)

ventana.mainloop()
