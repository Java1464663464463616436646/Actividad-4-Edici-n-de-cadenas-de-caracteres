import tkinter as tk
from tkinter import filedialog
import pandas as pd

ventana = tk.Tk()
ventana.title("Ventana")
ventana.geometry("600x400") 

# Definir la secuencia inicial
secuencia = "TGTAGTGCAGTGGCGTGATCTTGGCTCACTGCAGCCTCCACCTTAGAGCAATCCTCTTGCCTCATCCTCCCGGGTAGTTGGGACTACATGTGCATGCCACATGCCTGGCTAATTTTTGTATTTTTAGTA"

# Función para cerrar la ventana
def cerrar_ventana():
    ventana.destroy()

# Función para abrir un archivo CSV
def abrir_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])
    if archivo:
        # Cargarlo con pandas
        df = pd.read_csv(archivo)
        print("Archivo cargado con éxito:", archivo)
        return df

# Función para fusionar cadenas
def fusionar_cadenas(cadena1_idx, cadena2_idx, texto_resultado, resultado_label):
    idx1 = int(cadena1_idx) - 1
    idx2 = int(cadena2_idx) - 1
    with open('cadenas_modificadas.csv', 'r') as archivo:
        contenido = archivo.readlines()
        cadena1 = contenido[idx1 + 1].strip()
        cadena2 = contenido[idx2 + 1].strip()
        original = contenido[1].strip()  

    mod1 = cadena1.split(',')[0::2]
    mod2 = cadena2.split(',')[0::2]

    cadena1_original = cadena1.split(',')[0]
    cadena2_original = cadena2.split(',')[0]
    Original_Original = original.split(',')[0]

    mod_fusionadas = list(Original_Original)

    for l in range(len(Original_Original)):
        if Original_Original[l] != cadena1_original[l]:
            mod_fusionadas[l] = cadena1_original[l]
        elif Original_Original[l] != cadena2_original[l]:
            mod_fusionadas[l] = cadena2_original[l]

    cadena_fusionada = ''.join(mod_fusionadas)

    resultado = f"Cadena fusionada: {cadena_fusionada}"

    resultado_label.config(text=resultado)

# Función para generar combinaciones
def generar_combinaciones():
    df = abrir_archivo()
    if df is None:
        return
    
    ventana_actual = 0
    ventana_size = 10
    step = 5
    
    while ventana_actual <= len(secuencia) - ventana_size:
        ventana_texto = secuencia[ventana_actual:ventana_actual + ventana_size]
        print("Ventana {}: {}".format(ventana_actual, ventana_texto))
        
        for i in range(ventana_size):
            for letra in "ACGT":
                combinacion = list(ventana_texto)
                combinacion[i] = letra
                nueva_secuencia = secuencia[:ventana_actual + i] + letra + secuencia[ventana_actual + i + 1:]
                print("Combinación:", nueva_secuencia)
        
        ventana_actual += step

# Interfaz gráfica
frame_superior = tk.Frame(ventana)
frame_superior.pack(side="top", fill="x")

etiqueta_bienvenidos = tk.Label(frame_superior, text="Bienvenidos")
etiqueta_bienvenidos.pack(pady=15)

boton_abrir = tk.Button(ventana, text="Abrir archivo CSV", command=abrir_archivo)
boton_abrir.pack(pady=5)

boton_combinar = tk.Button(ventana, text="Combinar", command=generar_combinaciones)
boton_combinar.pack(pady=5)

boton_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar_ventana)
boton_cerrar.pack(pady=5)


cadena1_entry = tk.Entry(ventana)
cadena1_entry.pack(pady=5)

cadena2_entry = tk.Entry(ventana)
cadena2_entry.pack(pady=5)

resultado_label = tk.Label(ventana, text="")
resultado_label.pack(pady=5)

fusionar_button = tk.Button(ventana, text="Fusionar Cadenas", 
                            command=lambda: fusionar_cadenas(cadena1_entry.get(), cadena2_entry.get(), "", resultado_label))
fusionar_button.pack(pady=5)

ventana.mainloop()
