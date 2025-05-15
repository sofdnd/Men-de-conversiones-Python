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