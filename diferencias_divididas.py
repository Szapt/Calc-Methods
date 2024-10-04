import tkinter as tk
from tkinter import *
from tkinter import ttk
import sympy as sp

# Interfaz
root = Tk()
root.title("Diferencias Divididas y Polinomio de Lagrange")

frame1 = Frame(root, width="650", height="350")
frame1.grid(column=0, row=0, sticky="nsew")
frame1.pack(fill="both", expand="True")
frame1.config(bd="10")

Label(root, text="Diferencias Divididas y Polinomio de Lagrange").pack()

Label(frame1, text="Función (en x): ").grid(column=0, row=0, pady=20, padx=10)
ingresa_funcion = Entry(frame1, width=20)
ingresa_funcion.grid(column=1, row=0)

Label(frame1, text="X0: ").grid(column=0, row=1, pady=10, padx=10)
ingresa_x0 = Entry(frame1, width=20)
ingresa_x0.grid(column=1, row=1)

Label(frame1, text="Aumento de Xi: ").grid(column=0, row=2, pady=10, padx=10)
ingresa_aumento = Entry(frame1, width=20)
ingresa_aumento.grid(column=1, row=2)

Label(frame1, text="# Iteraciones: ").grid(column=0, row=3, pady=10, padx=10)
ingresa_k = Entry(frame1, width=20)
ingresa_k.grid(column=1, row=3)

# Crear el marco de la tabla
tree_frame = Frame(root)
tree_frame.pack(pady=20)

# Crear el área para mostrar el polinomio
polinomio_label = Label(root, text="Polinomio de Lagrange: ")
polinomio_label.pack(pady=10)

def configurar_tabla(k):
    # Limpiar cualquier tabla anterior
    for widget in tree_frame.winfo_children():
        widget.destroy()

    # Definir las columnas dinámicas según el número de diferencias
    columnas = ["Xi", "F(Xi)"] + [f"Diferencia {i}" for i in range(1, k)]
    
    # Crear la tabla con el número dinámico de columnas
    tree = ttk.Treeview(tree_frame, columns=columnas, show="headings", height=10)
    tree.pack()

    # Definir los encabezados dinámicamente
    for col in columnas:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")

    return tree

def diferencias_divididas():
    try:
        aumento = float(ingresa_aumento.get())
        k = int(ingresa_k.get())
        fx = ingresa_funcion.get()
        x = sp.symbols('x')  # Definir la variable simbólica 'x'
        f = sp.sympify(fx)  # Convertir la función en una expresión simbólica

        x0 = float(ingresa_x0.get())  # Convertir X0 a número
        xi_lista = []

        for i in range(k):
            xi = x0 + aumento * i
            fxi = f.subs(x, xi).evalf()
            xi_lista.append((xi, fxi))

        return xi_lista
    except Exception as e:
        tree.delete(*tree.get_children())  # Limpiar la tabla si hay errores
        tree.insert("", "end", values=("Error", f"{e}", ""))
        return None

def calcular_diferencias_divididas(xi_lista):
    diferencias = [xi_lista]  # Guardar todas las diferencias divididas por iteración
    for nivel in range(1, len(xi_lista)):
        nueva_lista = []
        for i in range(len(diferencias[-1]) - 1):
            numerador = diferencias[-1][i + 1][1] - diferencias[-1][i][1]
            denominador = diferencias[-1][i + 1][0] - diferencias[-1][i][0]
            nueva_lista.append((diferencias[-1][i][0], numerador / denominador))
        diferencias.append(nueva_lista)
    return diferencias

def organizar_datos(diferencias):
    resultados_tabla = []
    max_niveles = len(diferencias)
    
    for i in range(len(diferencias[0])):
        fila = [f"{diferencias[0][i][0]}", f"{diferencias[0][i][1]}"]
        
        # Agregamos las diferencias por nivel, alineadas correctamente
        for nivel in range(1, max_niveles):
            if i >= nivel and i < len(diferencias[nivel]) + nivel:
                fila.append(f"{diferencias[nivel][i - nivel][1]}")
            else:
                fila.append("")
        resultados_tabla.append(fila)
    
    return resultados_tabla

def mostrar_diferencias_divididas(resultados_tabla, tree):
    tree.delete(*tree.get_children())  # Limpiar la tabla antes de mostrar los datos

    for fila in resultados_tabla:
        tree.insert("", "end", values=fila)


def construir_polinomio_lagrange(diferencias, xi_lista):
    x = sp.symbols('x')
    polinomio = diferencias[0][0][1]  # El primer término del polinomio es el valor inicial de f(x0)
    terminos = [1]
    coeficientes = [f"{diferencias[0][0][1]}"]  # Lista para los coeficientes con formato
    
    for i in range(1, len(diferencias)):
        # Multiplicamos por los factores (x - xi) correspondientes
        terminos.append(terminos[-1] * (x - xi_lista[i-1][0]))
        polinomio += diferencias[i][0][1] * terminos[-1]
        # Agregamos el coeficiente en formato
        coeficientes.append(f"{diferencias[i][0][1]}")
    
    return sp.expand(polinomio), coeficientes

def mostrar_polinomio_lagrange(coeficientes, xi_lista):
    polinomio_str = f"P(x) = {coeficientes[0]}"
    for i in range(1, len(coeficientes)):
        terminos = " * ".join([f"(x - {xi_lista[j][0]})" for j in range(i)])
        polinomio_str += f" + {coeficientes[i]} * {terminos}"
    
    polinomio_label.config(text=f"Polinomio de Lagrange: {polinomio_str}")

def resolver_diferencias_divididas():
    xi_lista = diferencias_divididas()
    if xi_lista:
        # Obtener el número de iteraciones para configurar la tabla
        k = int(ingresa_k.get())
        tree = configurar_tabla(k)  # Configurar la tabla según k

        # Calculamos todas las diferencias divididas
        diferencias = calcular_diferencias_divididas(xi_lista)
        
        # Organizar los datos para mostrarlos en la tabla
        resultados_tabla = organizar_datos(diferencias)
        
        # Mostramos las diferencias divididas en la tabla
        mostrar_diferencias_divididas(resultados_tabla, tree)

        # Construir y mostrar el polinomio de Lagrange
        polinomio, coeficientes = construir_polinomio_lagrange(diferencias, xi_lista)
        mostrar_polinomio_lagrange(coeficientes, xi_lista)

# Botón para resolver
resolver = Button(frame1, width=20, text='Resolver', bg='brown', bd=5, command=resolver_diferencias_divididas)
resolver.grid(columnspan=2, row=4, pady=20, padx=10)

root.mainloop()

