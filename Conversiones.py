import tkinter as tk
from tkinter import ttk, messagebox

# Funciones de conversión
def convertir_longitud(valor):
    try:
        val = float(valor)
        km = val / 1000
        m = val * 0.0254
        return f"{val} metros = {km:.3f} km\n{val} pulgadas = {m:.3f} metros"
    except ValueError:
        return "Valor no válido"

def convertir_masa(valor):
    try:
        val = float(valor)
        g = val * 1000
        kg = val * 0.4536
        return f"{val} kg = {g:.1f} gramos\n{val} libras = {kg:.3f} kg"
    except ValueError:
        return "Valor no válido"

def convertir_tiempo(valor):
    try:
        val = float(valor)
        min = val / 60
        dias = val / 24
        return f"{val} segundos = {min:.2f} minutos\n{val} horas = {dias:.2f} días"
    except ValueError:
        return "Valor no válido"
    
def abrir_ventana(tipo):
    ventana = tk.Toplevel()
    ventana.title(f"Conversión de {tipo}")

    tk.Label(ventana, text="Ingrese valor:").pack(pady=5)
    entrada = tk.Entry(ventana)
    entrada.pack(pady=5)

    resultado_label = tk.Label(ventana, text="Resultado:")
    resultado_label.pack(pady=5)

    def hacer_conversion():
        valor = entrada.get()
        if tipo == "Longitud":
            resultado = convertir_longitud(valor)
        elif tipo == "Masa":
            resultado = convertir_masa(valor)
        elif tipo == "Tiempo":
            resultado = convertir_tiempo(valor)
        resultado_label.config(text=f"Resultado:\n{resultado}")

    tk.Button(ventana, text="Convertir", command=hacer_conversion).pack(pady=5)

# Menú principal
def menu_principal():
    raiz = tk.Tk()
    raiz.title("Conversor de Unidades")
    raiz.geometry("300x250")

    tk.Label(raiz, text="Escoja su opción", bg="lightgreen", font=("Arial", 12)).pack(fill="x")

    tk.Button(raiz, text="Longitud", bg="orange", command=lambda: abrir_ventana("Longitud")).pack(pady=10)
    tk.Button(raiz, text="Masa", bg="orange", command=lambda: abrir_ventana("Masa")).pack(pady=10)
    tk.Button(raiz, text="Tiempo", bg="orange", command=lambda: abrir_ventana("Tiempo")).pack(pady=10)

    raiz.mainloop()

menu_principal()