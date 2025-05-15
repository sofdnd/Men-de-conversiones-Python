
import tkinter as tk
from tkinter import ttk, messagebox

# Funciones de conversión
def convertir_longitud(valor, tipo):
    try:
        val = float(valor)
        if tipo == "Metros a Kilómetros":
            km = val / 1000
            return f"{val} metros = {km:.3f} km"
        elif tipo == "Pulgadas a Metros":
            m = val * 0.0254
            return f"{val} pulgadas = {m:.3f} metros"
    except ValueError:
        return "Valor no válido"

def convertir_masa(valor, tipo):
    try:
        val = float(valor)
        if tipo == "Kilogramos a Gramos":
            g = val * 1000
            return f"{val} kg = {g:.1f} gramos"
        elif tipo == "Libras a Kilogramos":
            kg = val * 0.4536
            return f"{val} libras = {kg:.3f} kg"
    except ValueError:
        return "Valor no válido"

def convertir_tiempo(valor, tipo):
    try:
        val = float(valor)
        if tipo == "Segundos a Minutos":
            min = val / 60
            return f"{val} segundos = {min:.2f} minutos"
        elif tipo == "Horas a Días":
            dias = val / 24
            return f"{val} horas = {dias:.2f} días"
    except ValueError:
        return "Valor no válido"

# Ventana de conversión específica
def abrir_ventana(tipo):
    ventana = tk.Toplevel()
    ventana.title(f"Conversión de {tipo}")
    ventana.configure(bg="#e0f7fa")

    tk.Label(ventana, text=f"Conversión de {tipo}", bg="#e0f7fa", font=("Courier", 14)).pack(pady=10)

    opciones = []
    if tipo == "Masa":
        opciones = ["Kilogramos a Gramos", "Libras a Kilogramos"]
    elif tipo == "Longitud":
        opciones = ["Metros a Kilómetros", "Pulgadas a Metros"]
    elif tipo == "Tiempo":
        opciones = ["Segundos a Minutos", "Horas a Días"]

    tk.Label(ventana, text="Selecciona tipo de conversión:", bg="#e0f7fa").pack()
    combo = ttk.Combobox(ventana, values=opciones)
    combo.set("Selecciona una opción")
    combo.pack(pady=5)

    tk.Label(ventana, text="Valor a convertir:", bg="#e0f7fa").pack(pady=5)
    entrada = tk.Entry(ventana)
    entrada.pack(pady=5)

    resultado_label = tk.Label(ventana, text="Resultado:", bg="#e0f7fa")
    resultado_label.pack(pady=5)

    def hacer_conversion():
        valor = entrada.get()
        seleccion = combo.get()
        if tipo == "Longitud":
            resultado = convertir_longitud(valor, seleccion)
        elif tipo == "Masa":
            resultado = convertir_masa(valor, seleccion)
        elif tipo == "Tiempo":
            resultado = convertir_tiempo(valor, seleccion)
        resultado_label.config(text=f"Resultado:\n{resultado}")

    tk.Button(ventana, text="Convertir", command=hacer_conversion, bg="#00796b", fg="white").pack(pady=10)

# Menú principal
def menu_principal():
    raiz = tk.Tk()
    raiz.title("Menú de Conversiones")
    raiz.geometry("350x300")
    raiz.configure(bg="#e0f7fa")

    tk.Label(raiz, text="Selecciona una opción:", bg="#e0f7fa", font=("Courier", 14)).pack(pady=15)

    tk.Button(raiz, text="Conversión de Longitud", bg="#80cbc4", fg="black", command=lambda: abrir_ventana("Longitud")).pack(pady=10)
    tk.Button(raiz, text="Conversión de Masa", bg="#80cbc4", fg="black", command=lambda: abrir_ventana("Masa")).pack(pady=10)
    tk.Button(raiz, text="Conversión de Tiempo", bg="#80cbc4", fg="black", command=lambda: abrir_ventana("Tiempo")).pack(pady=10)

    raiz.mainloop()

menu_principal()