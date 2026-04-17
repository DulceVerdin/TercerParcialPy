import customtkinter as ctk
from tkinter import ttk, messagebox
import os

class AppPizzeria(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Practica Pizzas - Registro de Pedidos")
        self.geometry("900x650")
        
        self.archivo_temporal = "pizzas_temp.txt"
        self.archivo_ventas = "ventas.txt"
        self.total_dia = 0.0
        
        
        self.frame_cliente = ctk.CTkFrame(self)
        self.frame_cliente.pack(pady=10, padx=20, fill="x")
        
        ctk.CTkLabel(self.frame_cliente, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.ent_nombre = ctk.CTkEntry(self.frame_cliente, width=200)
        self.ent_nombre.grid(row=0, column=1, padx=5)
        
        ctk.CTkLabel(self.frame_cliente, text="Dirección:").grid(row=0, column=2, padx=5, pady=5)
        self.ent_direccion = ctk.CTkEntry(self.frame_cliente, width=200)
        self.ent_direccion.grid(row=0, column=3, padx=5)
        
        ctk.CTkLabel(self.frame_cliente, text="Teléfono:").grid(row=0, column=4, padx=5, pady=5)
        self.ent_telefono = ctk.CTkEntry(self.frame_cliente, width=120)
        self.ent_telefono.grid(row=0, column=5, padx=5)

        ctk.CTkLabel(self.frame_cliente, text="Fecha:").grid(row=1, column=0, padx=5, pady=5)

        self.ent_dia = ctk.CTkEntry(self.frame_cliente, width=50, placeholder_text="Dia")
        self.ent_dia.grid(row=1, column=1, padx=5)

        self.ent_mes = ctk.CTkEntry(self.frame_cliente, width=50, placeholder_text="Mes")
        self.ent_mes.grid(row=1, column=2, padx=5)

        self.ent_anio = ctk.CTkEntry(self.frame_cliente, width=80, placeholder_text="Año")
        self.ent_anio.grid(row=1, column=3, padx=5)

       
        self.frame_opciones = ctk.CTkFrame(self)
        self.frame_opciones.pack(pady=10, padx=20, fill="x")
        
        self.var_tamano = ctk.StringVar(value="Chica")
        self.p_tamanos = {"Chica": 45, "Mediana": 85, "Grande": 125}
        
        ctk.CTkLabel(self.frame_opciones, text="Tamaño Pizza", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=20)
        for i, (t, p) in enumerate(self.p_tamanos.items()):
            ctk.CTkRadioButton(self.frame_opciones, text=f"{t} ${p}", variable=self.var_tamano, value=t).grid(row=i+1, column=0, sticky="w", padx=20)

        self.var_ingrediente = ctk.StringVar(value="Jamón")
        self.p_ingredientes = {"Jamón": 15, "Piña": 15, "Champiñones": 15}
        
        ctk.CTkLabel(self.frame_opciones, text="Ingredientes", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=20)
        for i, (ing, p) in enumerate(self.p_ingredientes.items()):
            ctk.CTkRadioButton(self.frame_opciones, text=f"{ing} ${p}", variable=self.var_ingrediente, value=ing).grid(row=i+1, column=1, sticky="w", padx=20)

        ctk.CTkLabel(self.frame_opciones, text="Num. Pizzas:").grid(row=1, column=2, padx=10)
        self.ent_cantidad = ctk.CTkEntry(self.frame_opciones, width=60)
        self.ent_cantidad.insert(0, "1")
        self.ent_cantidad.grid(row=2, column=2)
        
        self.btn_agregar = ctk.CTkButton(self.frame_opciones, text="Agregar", command=self.agregar_pizza)
        self.btn_agregar.grid(row=3, column=2, pady=10, padx=10)

       
        self.frame_tabla = ctk.CTkFrame(self)
        self.frame_tabla.pack(pady=10, padx=20, fill="both", expand=True)
        
        columns = ("tamano", "ingrediente", "cantidad", "subtotal")
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columns, show="headings")
        self.tabla.heading("tamano", text="Tamaño")
        self.tabla.heading("ingrediente", text="Ingredientes")
        self.tabla.heading("cantidad", text="Num. Pizzas")
        self.tabla.heading("subtotal", text="SubTotal")
        self.tabla.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        
        self.txt_ventas = ctk.CTkTextbox(self.frame_tabla, width=250)
        self.txt_ventas.pack(side="right", fill="both", padx=5, pady=5)
        self.txt_ventas.insert("0.0", "Ventas del día:\n" + "-"*25 + "\n")

        
        self.frame_controles = ctk.CTkFrame(self)
        self.frame_controles.pack(pady=10, fill="x")
        
        ctk.CTkButton(self.frame_controles, text="Quitar", fg_color="red", command=self.quitar_pizza).pack(side="left", padx=50)
        ctk.CTkButton(self.frame_controles, text="Terminar Pedido", fg_color="green", command=self.terminar_pedido).pack(side="right", padx=50)

        
        self.frame_total = ctk.CTkFrame(self)
        self.frame_total.pack(pady=10, fill="x")

        self.lbl_total_dia = ctk.CTkLabel(
            self.frame_total,
            text="Total del día: $0.00",
            font=("Arial", 16, "bold")
        )
        self.lbl_total_dia.pack(pady=5)

    def agregar_pizza(self):
        try:
            cant = int(self.ent_cantidad.get())
            tam = self.var_tamano.get()
            ing = self.var_ingrediente.get()
            
            subtotal = (self.p_tamanos[tam] + self.p_ingredientes[ing]) * cant
            
            self.tabla.insert("", "end", values=(tam, ing, cant, f"${subtotal:.2f}"))
            
            with open(self.archivo_temporal, "a") as f:
                f.write(f"{tam},{ing},{cant},{subtotal}\n")
                
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número")

    def quitar_pizza(self):
        selected = self.tabla.selection()
        if selected:
            for item in selected:
                self.tabla.delete(item)
        else:
            messagebox.showwarning("Atención", "Selecciona una fila para quitar")

    def terminar_pedido(self):
        nombre = self.ent_nombre.get()
        if not nombre or not os.path.exists(self.archivo_temporal):
            messagebox.showwarning("Error", "Datos incompletos o tabla vacía")
            return
        
        total_pedido = 0.0
       
        with open(self.archivo_temporal, "r") as f:
            for linea in f:
                datos = linea.strip().split(",")
                total_pedido += float(datos[3])
        
        direccion = self.ent_direccion.get()
        telefono = self.ent_telefono.get()
        fecha = f"{self.ent_dia.get()}/{self.ent_mes.get()}/{self.ent_anio.get()}"

        
        with open(self.archivo_ventas, "a") as f:
            f.write(f"Cliente: {nombre}\n")
            f.write(f"Total: ${total_pedido:.2f}\n")
            
        
        messagebox.showinfo("Pedido Terminado", f"Cliente: {nombre}\nTotal a pagar: ${total_pedido:.2f}")
        
        self.txt_ventas.insert("end", f"{nombre} total ${total_pedido:.2f}\n")
        
        self.total_dia += total_pedido
        self.lbl_total_dia.configure(text=f"Total del día: {self.total_dia:.2f}")
      
        self.limpiar_pantalla()
        
    def limpiar_pantalla(self):
        self.tabla.delete(*self.tabla.get_children())
        if os.path.exists(self.archivo_temporal):
            os.remove(self.archivo_temporal)
        self.ent_nombre.delete(0, 'end')
        self.ent_direccion.delete(0, 'end')
        self.ent_telefono.delete(0, 'end')

if __name__ == "__main__":
    app = AppPizzeria()
    app.mainloop()