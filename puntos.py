import tkinter as tk
from tkinter import *
from tkinter import ttk
import sympy as sp

#Interfaz
root = Tk()

root.title("Aproximaciones a la derivada")
#root.geometry("650x350")

frame1 = Frame(root,width="650", height="350" )
frame1.grid(column=0, row=0, sticky="nsew")
frame1.pack(fill="both", expand="True")
frame1.config(bd="10")

Label(root, text="Fórmula de dos, tres y cinco puntos").pack()
funcion = Label(frame1, text="Función: ").grid(column=0, row=0, pady=20, padx=10)
ingresa_funcion = Entry(frame1, width=20)
ingresa_funcion.grid(column=1, row=0)

x0 = Label(frame1, text="X0: ").grid(column=0, row=1, pady=10, padx=10)
ingresa_x0 = Entry(frame1, width=20)
ingresa_x0.grid(column=1, row=1)



#funciones
def dos_puntos(fx0, x0, h):
    aproximaciones = {}
    for i in h:
        fx_h = fx0.subs(x0, x0 + i)
        aprox = (fx_h - fx0) / i

        f2_x0 = sp.diff(fx0, x0, 2)
        err = (i*f2_x0) / 2

        # Evaluar las ecuaciones en el punto x0
        x0_valor = float(ingresa_x0.get())
        aprox_valor = aprox.subs(x0, x0_valor).evalf()
        err_valor = err.subs(x0, x0_valor).evalf()

        aproximaciones[i] = (aprox_valor, err_valor)
    return aproximaciones

def tres_puntos(fx0, x0, h):
    aproximaciones = {}
    for i in h:
        fx_h1 = fx0.subs(x0, x0 + i)
        fx_h2 = fx0.subs(x0, x0 - i)
        aprox = (fx_h1 - fx_h2) / (2*i)

        f3_x0 = sp.diff(fx0, x0, 3)
        err = ((i**2) / 6) * f3_x0

        # Evaluar las ecuaciones en el punto x0
        x0_valor = float(ingresa_x0.get())
        aprox_valor = aprox.subs(x0, x0_valor).evalf()
        err_valor = err.subs(x0, x0_valor).evalf()

        aproximaciones[i] = (aprox_valor, err_valor)
    return aproximaciones

def cinco_puntos(fx0, x0, h):
    aproximaciones = {}
    for i in h:
        fx_h1 = fx0.subs(x0, x0 - 2*i)
        fx_h2 = fx0.subs(x0, x0 - i)
        fx_h3 = fx0.subs(x0, x0 + i)
        fx_h4 = fx0.subs(x0, x0 + 2*i)
        aprox = (1 / (12*i)) * (fx_h1 - 8*fx_h2 + 8*fx_h3 - fx_h4)

        f5_x0 = sp.diff(fx0, x0, 5)
        err = ((i**4) / 30) * f5_x0

        # Evaluar las ecuaciones en el punto x0
        x0_valor = float(ingresa_x0.get())
        aprox_valor = aprox.subs(x0, x0_valor).evalf()
        err_valor = err.subs(x0, x0_valor).evalf()

        aproximaciones[i] = (aprox_valor, err_valor)
    return aproximaciones

def formulas_puntos():
    fx = ingresa_funcion.get()
    x0 = sp.symbols(ingresa_x0.get())
    fx0 = sp.sympify(fx).subs('x', x0)
    h = [0.1, 0.01, 0.001]
    mensaje = "para una función ", fx, " con X0 = ", str(x0)

    dos_puntos_resultado = dos_puntos(fx0, x0, h)
    tres_puntos_resultado = tres_puntos(fx0, x0, h)
    cinco_puntos_resultado = cinco_puntos(fx0, x0, h)

    return mensaje, dos_puntos_resultado, tres_puntos_resultado, cinco_puntos_resultado

def mostrar_datos():
    # Eliminar el frame de la tabla anterior
    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame) and widget != frame1:
            widget.destroy()

    mensaje, dos_puntos, tres_puntos, cinco_puntos = formulas_puntos()
    # Crear un frame para las tablas
    frame_tablas = Frame(root, bg="#f0f0f0")
    frame_tablas.pack(pady=20)

    # Crear un Treeview para la tabla de dos puntos
    tabla_dos_puntos = ttk.Treeview(frame_tablas)
    tabla_dos_puntos["columns"] = ("h", "Aproximación", "Error")
    tabla_dos_puntos.column("#0", width=0, stretch=tk.NO)
    tabla_dos_puntos.column("h", anchor=tk.W, width=100)
    tabla_dos_puntos.column("Aproximación", anchor=tk.W, width=150)
    tabla_dos_puntos.column("Error", anchor=tk.W, width=150)
    tabla_dos_puntos.heading("#0", text="", anchor=tk.W)
    tabla_dos_puntos.heading("h", text="h", anchor=tk.W)
    tabla_dos_puntos.heading("Aproximación", text="Aproximación", anchor=tk.W)
    tabla_dos_puntos.heading("Error", text="Error", anchor=tk.W)
    tabla_dos_puntos.grid(column=0, row=1, padx=10, pady=10)
    Label(frame_tablas, text="dos puntos").grid(column=0, row=0)

    # Crear un Treeview para la tabla de tres puntos
    tabla_tres_puntos = ttk.Treeview(frame_tablas)
    tabla_tres_puntos["columns"] = ("h", "Aproximación", "Error")
    tabla_tres_puntos.column("#0", width=0, stretch=tk.NO)
    tabla_tres_puntos.column("h", anchor=tk.W, width=100)
    tabla_tres_puntos.column("Aproximación", anchor=tk.W, width=150)
    tabla_tres_puntos.column("Error", anchor=tk.W, width=150)
    tabla_tres_puntos.heading("#0", text="", anchor=tk.W)
    tabla_tres_puntos.heading("h", text="h", anchor=tk.W)
    tabla_tres_puntos.heading("Aproximación", text="Aproximación", anchor=tk.W)
    tabla_tres_puntos.heading("Error", text="Error", anchor=tk.W)
    tabla_tres_puntos.grid(column=1, row=1, padx=10, pady=10)
    Label(frame_tablas, text="tres puntos").grid(column=1, row=0)

    # Crear un Treeview para la tabla de tres puntos
    tabla_cinco_puntos = ttk.Treeview(frame_tablas)
    tabla_cinco_puntos["columns"] = ("h", "Aproximación", "Error")
    tabla_cinco_puntos.column("#0", width=0, stretch=tk.NO)
    tabla_cinco_puntos.column("h", anchor=tk.W, width=100)
    tabla_cinco_puntos.column("Aproximación", anchor=tk.W, width=150)
    tabla_cinco_puntos.column("Error", anchor=tk.W, width=150)
    tabla_cinco_puntos.heading("#0", text="", anchor=tk.W)
    tabla_cinco_puntos.heading("h", text="h", anchor=tk.W)
    tabla_cinco_puntos.heading("Aproximación", text="Aproximación", anchor=tk.W)
    tabla_cinco_puntos.heading("Error", text="Error", anchor=tk.W)
    tabla_cinco_puntos.grid(column=2, row=1, padx=10, pady=10)
    Label(frame_tablas, text="cinco puntos").grid(column=2, row=0)
    
    # Agregar los datos a las tablas
    for i, (aprox, err) in dos_puntos.items():
        tabla_dos_puntos.insert("", tk.END, values=(i, aprox, err))
    for i, (aprox, err) in tres_puntos.items():
        tabla_tres_puntos.insert("", tk.END, values=(i, aprox, err))
    for i, (aprox, err) in cinco_puntos.items():
        tabla_cinco_puntos.insert("", tk.END, values=(i, aprox, err))

# Llamar a la función para mostrar los datos
resolver = Button(frame1, width=20, text='Resolver', bg='brown', bd=5, command= mostrar_datos)
resolver.grid(columnspan=2, row=3, pady=20, padx=10)



root.mainloop()