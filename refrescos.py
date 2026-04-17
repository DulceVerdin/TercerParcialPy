import customtkinter as ctk
from tkinter import messagebox, simpledialog
from PIL import Image
import os

precios = {
    "Coca": 8,
    "Fanta": 5,
    "Sprite": 5,
    "Agua": 4,
    "Jarrito": 5,
    "Mundet": 4
}

stock = {
    "Coca": 8,
    "Fanta": 5,
    "Sprite": 5,
    "Agua": 4,
    "Jarrito": 5,
    "Mundet": 4
}

dinero = 0

def ingresar_monedas(valor):
    global dinero
    dinero += valor
    actualizar()

def actualizar():
    global dinero
    lbl_dinero.configure(text=f"$ {dinero}")
    bebida = opcion.get()

    actualizar_stock_texto()

    if bebida:
        precio = precios[bebida]
        lbl_precio.configure(text=f"Precio: $ {precio}")

        try:
            ruta = os.path.join("imagenes", f"{bebida}.jpg")
            img_pil = Image.open(ruta)

            ctk_img = ctk.CTkImage(light_image=img_pil, dark_image=img_pil, size=(130, 130))

            lbl_res_img.configure(image=ctk_img, text="")
            lbl_res_img.image = ctk_img

        except Exception as e:
            lbl_res_img.configure(image=None, text="Imagen no encontrada")
            print("Error:", e)

        if dinero >= precio and stock[bebida] > 0:
            btn_comprar.configure(state="normal")
        else:
            btn_comprar.configure(state="disabled")

    actualizar_stock()

def actualizar_stock():
    for bebida, rb in radios.items():
        if stock[bebida] <= 0:
            rb.configure(state="disabled")
        else:
            rb.configure(state="normal")

def actualizar_stock_texto():
    for bebida, rb in radios.items():
        rb.configure(text=f"{bebida} ({stock[bebida]})")

def comprar():
    global dinero
    bebida = opcion.get()
    precio = precios[bebida]

    if dinero < precio:
        messagebox.showwarning("Error", "Dinero insuficiente")
        return

    cambio = dinero - precio
    dinero = 0
    stock[bebida] -= 1

    actualizar()

    messagebox.showinfo(
        "Compra",
        f"GRACIAS POR SU COMPRA\n\nProducto: {bebida}\nCambio: $ {cambio}"
    )

def surtir():
    bebida = simpledialog.askstring("Surtir", "¿Qué bebida?")
    if bebida not in stock:
        messagebox.showerror("Error", "No existe")
        return

    cantidad = simpledialog.askinteger("Cantidad", "¿Cuántos agregar?")
    if cantidad is None or cantidad < 0:
        messagebox.showerror("Error", "Valor inválido")
        return

    stock[bebida] += cantidad
    actualizar()

def cambiar_precio():
    bebida = simpledialog.askstring("Precio", "¿Qué bebida?")
    if bebida not in precios:
        messagebox.showerror("Error", "No existe")
        return

    nuevo = simpledialog.askinteger("Nuevo precio", "Nuevo precio:")
    if nuevo is None or nuevo < 0:
        messagebox.showerror("Error", "Valor inválido")
        return

    precios[bebida] = nuevo
    actualizar()

app = ctk.CTk()
app.title("Máquina Expendedora")
app.geometry("500x500")

# MENU
menu = ctk.CTkFrame(app)
menu.pack(pady=5)

ctk.CTkButton(menu, text="Surtir", command=surtir).pack(side="left", padx=5)
ctk.CTkButton(menu, text="Cambiar Precio", command=cambiar_precio).pack(side="left", padx=5)

# MONEDAS
frame_monedas = ctk.CTkFrame(app)
frame_monedas.pack(pady=10)

for m in [0.5, 1, 2, 5, 10]:
    ctk.CTkButton(frame_monedas, text=str(m),
                  command=lambda v=m: ingresar_monedas(v)).pack(side="left", padx=5)

lbl_dinero = ctk.CTkLabel(app, text="$ 0")
lbl_dinero.pack()

lbl_precio = ctk.CTkLabel(app, text="Precio: $ 0")
lbl_precio.pack()

frame_main = ctk.CTkFrame(app)
frame_main.pack(pady=10)

opcion = ctk.StringVar()
radios = {}

frame_refrescos = ctk.CTkFrame(frame_main)
frame_refrescos.pack(side="left", padx=10)

for bebida in precios:
    rb = ctk.CTkRadioButton(
        frame_refrescos,
        text=f"{bebida} ({stock[bebida]})",
        variable=opcion,
        value=bebida,
        command=actualizar
    )
    rb.pack(anchor="w")
    radios[bebida] = rb

lbl_res_img = ctk.CTkLabel(frame_main, text="")
lbl_res_img.pack(pady=20)

btn_comprar = ctk.CTkButton(app, text="Tomar Refresco", command=comprar, state="disabled")
btn_comprar.pack(pady=10)

actualizar()
app.mainloop