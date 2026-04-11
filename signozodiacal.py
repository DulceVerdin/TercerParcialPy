import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from PIL import Image, ImageTk  

def calcular_zodiaco_chino(anio):
    signos = ["Mono", "Gallo", "Perro", "Cerdo", "Rata", "Buey", 
              "Tigre", "Conejo", "Dragon", "Serpiente", "Caballo", "Cabra"]
    return signos[anio % 12]

def imprimir_datos():
    try:
        
        nombre_completo = f"{entry_nom.get()} {entry_pat.get()} {entry_mat.get()}"
        dia = int(entry_dia.get())
        mes = int(entry_mes.get())
        año = int(entry_año.get())
        
        
        hoy= datetime.now()
        edad =hoy.year - año - ((hoy.month,hoy.day)< (mes, dia))
        
        signo = calcular_zodiaco_chino(año)
        
       
        lbl_res_nombre.config(text=f"Hola {nombre_completo}")
        lbl_res_edad.config(text=f"Tienes {edad} años")
        lbl_res_signo.config(text=f"tu signo zodiacal\nEs {signo}")
        
        img = Image.open(f"imagenesSigno/{signo}.jpeg").resize((130, 130))
        foto = ImageTk.PhotoImage(img)
        lbl_res_img.config(image=foto)
        lbl_res_img.image = foto
        
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa datos válidos en la fecha.")


ventana = tk.Tk()
ventana.title("Práctica 1 - Zodiaco")
ventana.geometry("600x400")


frame_izq = tk.Frame(ventana, padx=20, pady=20)
frame_izq.pack(side="left", fill="both", expand=True)

tk.Label(frame_izq, text="Datos Personales", font=("Arial", 12, "bold")).pack()

tk.Label(frame_izq, text="Nombre:").pack()
entry_nom = tk.Entry(frame_izq)
entry_nom.pack()

tk.Label(frame_izq, text="A. Paterno:").pack()
entry_pat = tk.Entry(frame_izq)
entry_pat.pack()

tk.Label(frame_izq, text="A. Materno:").pack()
entry_mat = tk.Entry(frame_izq)
entry_mat.pack()

tk.Label(frame_izq, text="\nFecha de nacimiento", font=("Arial", 10, "bold")).pack()
frame_fecha = tk.Frame(frame_izq)
frame_fecha.pack()

tk.Label(frame_fecha, text="Día").grid(row=0, column=0)
entry_dia = tk.Entry(frame_fecha, width=5)
entry_dia.grid(row=1, column=0)

tk.Label(frame_fecha, text="Mes").grid(row=0, column=1)
entry_mes = tk.Entry(frame_fecha, width=5)
entry_mes.grid(row=1, column=1)

tk.Label(frame_fecha, text="Año").grid(row=0, column=2)
entry_año = tk.Entry(frame_fecha, width=8)
entry_año.grid(row=1, column=2)

tk.Label(frame_izq, text="\nSexo").pack()
var_sexo = tk.StringVar(value="M")
tk.Radiobutton(frame_izq, text="Masculino", variable=var_sexo, value="M").pack()
tk.Radiobutton(frame_izq, text="Femenino", variable=var_sexo, value="F").pack()

btn_imprimir = tk.Button(frame_izq, text="imprimir", command=imprimir_datos, bg="black", fg="white", width=15)
btn_imprimir.pack(pady=20)


frame_der = tk.Frame(ventana, padx=20, pady=20, bg="white")
frame_der.pack(side="right", fill="both", expand=True)

lbl_res_nombre = tk.Label(frame_der, text="", font=("Arial", 12, "italic"), bg="white")
lbl_res_nombre.pack(pady=10)

lbl_res_edad = tk.Label(frame_der, text="", font=("Arial", 12, "bold"), bg="white")
lbl_res_edad.pack()

lbl_res_signo = tk.Label(frame_der, text="", font=("Arial", 12), bg="white")
lbl_res_signo.pack(pady=10)


lbl_res_img = tk.Label(frame_der, bg="white")
lbl_res_img.pack(pady=20)

ventana.mainloop()