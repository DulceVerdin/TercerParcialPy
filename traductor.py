import tkinter as tk
from tkinter import messagebox
from deep_translator import GoogleTranslator

def traducir():
    palabra = cuadro_palabra.get("1.0", tk.END).strip()
    opcion = opcion_idioma.get()

    if palabra == "":
        messagebox.showwarning("Aviso", "Escribe la palabra que quieres traducir")
        return

    try:
        if opcion == "Inglés → Español":
            resultado = GoogleTranslator(source='en', target='es').translate(palabra)  #source = idioma del texto original "en" le dice al traductor que el texto esta en ingles
        else:
            resultado = GoogleTranslator(source='es', target='en').translate(palabra)  #tsrget = idioma al que quieres traducir "es" le dice al traductor que el texto esta en español

        cuadro_resultado.delete("1.0", tk.END)
        cuadro_resultado.insert(tk.END, resultado)

    except:
        messagebox.showerror("Error", "No se pudo traducir la palabra")

def limpiar():
    cuadro_palabra.delete("1.0", tk.END)
    cuadro_resultado.delete("1.0", tk.END)

# Ventana principal
ventana = tk.Tk()
ventana.title("Traductor Inglés ↔ Español")
ventana.geometry("500x400")

# Selector de idioma
opcion_idioma = tk.StringVar(value="Inglés → Español")
menu = tk.OptionMenu(ventana, opcion_idioma, "Inglés → Español", "Español → Inglés")
menu.pack(pady=10)

# Cuadro de texto original
tk.Label(ventana, text="Palabra a traducir:").pack()
cuadro_palabra = tk.Text(ventana, height=5)
cuadro_palabra.pack(padx=10, pady=5)

# Botón traducir
btn_traducir = tk.Button(ventana, text="Traducir", command=traducir)
btn_traducir.pack(pady=5)

# Resultado
tk.Label(ventana, text="Traduccion:").pack()
cuadro_resultado = tk.Text(ventana, height=5)  #height(sirve para especificar la altura del area de contenido,reyeno o borde)
cuadro_resultado.pack(padx=10, pady=5)

# Botón limpiar
btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
btn_limpiar.pack(pady=5)


ventana.mainloop()