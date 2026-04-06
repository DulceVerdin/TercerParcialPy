import tkinter as tk
from tkinter import messagebox
    
ventana = tk.Tk()
ventana.title("Traductor")
ventana.geometry("600x400")

ARCHIVO = "diccionario.txt"

def registrar_palabra():
    ing = entrada_ing.get().strip()
    esp = entrada_esp.get().strip()
    
    if not ing or not esp:
        messagebox.showwarning("Error", "Llena ambos campos")
        return

    with open(ARCHIVO, "a") as f:
        f.write(f"{ing}:{esp}\n")
    
    messagebox.showinfo("Éxito", "Palabra guardada")
    entrada_ing.delete(0, tk.END)
    entrada_esp.delete(0, tk.END)

def buscar_traduccion(Palabra):
    buscar = (Palabra)
    
    try:
        with open(ARCHIVO, "r") as f:
            lineas = f.readlines() 
            
        encontrado = False
        for linea in lineas:
            datos = linea.strip().split(":")
            if len(datos) == 2:
                ingles, espanol = datos

                if Palabra == "en_es" and ingles == buscar:
                    lbl_resultado.config(text=f"Español: {espanol}", fg="green")
                    encontrado = True
                    break
                elif Palabra == "es_en" and espanol == buscar:
                    lbl_resultado.config(text=f"Inglés: {ingles}", fg="green")
                    encontrado = True
                    break
        
        if not encontrado:
            lbl_resultado.config(text="No encontrada", fg="red" )
            
    except FileNotFoundError:
        messagebox.showerror("Error", "Registra una palabra primero.")
        
# Botones
opcion = tk.IntVar()

tk.Label(ventana, text="Ingresa la palabra a traducir:").grid(row=0, column=0, padx=10, pady=10)
entrada_busqueda = tk.Entry(ventana)
entrada_busqueda.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Selecciona la opción:").grid(row=1, column=0, padx=10, pady=10)

tk.Radiobutton(ventana, text="Español - Inglés", variable=opcion, value=1).grid(row=2, column=0, padx=10)
tk.Radiobutton(ventana, text="Inglés - Español", variable=opcion, value=2).grid(row=2, column=1, padx=10)

tk.Button(ventana, text="Traducir", command=lambda: buscar_traduccion(entry.get())).grid(row=3, column=0, columnspan=2, pady=10)

lbl_resultado = tk.Label(ventana, text="", font=("Arial", 12))
lbl_resultado.grid(row=4, column=0, columnspan=2, pady=10)

tk.Label(ventana, text="Agregar nueva palabra").grid(row=5, column=0, columnspan=2, pady=10)

tk.Label(ventana, text="Inglés").grid(row=6, column=0)
entrada_ing = tk.Entry(ventana)
entrada_ing.grid(row=7, column=0, padx=10)

tk.Label(ventana, text="Español").grid(row=6, column=1)
entrada_esp = tk.Entry(ventana)
entrada_esp.grid(row=7, column=1, padx=10)

tk.Button(ventana, text="Agregar", command=registrar_palabra).grid(row=8, column=0, columnspan=2, pady=10)

ventana.mainloop()