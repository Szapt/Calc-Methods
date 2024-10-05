import tkinter as tk
from tkinter import *
from tkinter import ttk
import sympy as sp

# Interfaz
root = Tk()
root.title("Diferencias Divididas y Polinomio de Lagrange")
root.geometry("800x600")  # Cambia el tamaño de la ventana

# Aplicar estilos para mejorar la apariencia
style = ttk.Style()
style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))
style.configure("Treeview", font=("Helvetica", 10))
style.configure("TButton", font=("Helvetica", 10))

frame1 = Frame(root)
frame1.grid(column=0, row=0, sticky="nsew", padx=20, pady=20)
frame1.pack(fill="both", expand="True")
frame1.config(bd="10")

titulo = Label(root, text="Diferencias Divididas y Polinomio de Lagrange", font=("Helvetica", 14, "bold"))
titulo.pack(pady=10)

Label(frame1, text="Función (en x): ").grid(column=0, row=0, pady=10, padx=10, sticky="e")
ingresa_funcion = Entry(frame1, width=20)
ingresa_funcion.grid(column=1, row=0, pady=10)

Label(frame1, text="X0: ").grid(column=0, row=1, pady=10, padx=10, sticky="e")
ingresa_x0 = Entry(frame1, width=20)
ingresa_x0.grid(column=1, row=1, pady=10)

Label(frame1, text="Aumento de Xi: ").grid(column=0, row=2, pady=10, padx=10, sticky="e")
ingresa_aumento = Entry(frame1, width=20)
ingresa_aumento.grid(column=1, row=2, pady=10)

Label(frame1, text="# Iteraciones: ").grid(column=0, row=3, pady=10, padx=10, sticky="e")
ingresa_k = Entry(frame1, width=20)
ingresa_k.grid(column=1, row=3, pady=10)

# Crear el marco de la tabla
tree_frame = Frame(root)
tree_frame.pack(pady=20)

# Crear el área para mostrar el polinomio
polinomio_label = Label(root, text="Polinomio de Lagrange: ", font=("Helvetica", 12))
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
    aumento = float(ingresa_aumento.get())
    k = int(ingresa_k.get())
    fx = ingresa_funcion.get()
    x = sp.symbols('x')  # Definir la variable simbólica 'x'
    f = sp.sympify(fx)  # Convertir la función en una expresión simbólica

    x0 = float(ingresa_x0.get())  # Convertir X0 a número
    x_lista = []
    y_lista = []

    for i in range(k):
        xi = x0 + aumento * i
        fxi = f.subs(x, xi).evalf()
        x_lista.append(xi)
        y_lista.append(fxi)

    return x_lista, y_lista


def calcular_todas_diferencias_divididas(x, y):
    """
    Calcula todas las diferencias divididas de los datos (x, y).
    Devuelve una lista de listas de diferencias divididas.
    """
    diferencias = [y]
    n = len(y)
    for i in range(1, n):
        nivel_diferencias = []
        for j in range(n - i):
            valor = (diferencias[i-1][j+1] - diferencias[i-1][j]) / (x[j+i] - x[j])
            nivel_diferencias.append(valor)
        diferencias.append(nivel_diferencias)
    return diferencias


def organizar_datos(x_lista, y_lista, diferencias):
    # Inicializamos una lista de listas para almacenar los datos de la tabla
    resultados_tabla = []

    # Añadir las dos primeras columnas: xi y f(xi)
    for i in range(len(x_lista)):
        fila = [f"{x_lista[i]}", f"{y_lista[i]}"]  # xi, f(xi)
        resultados_tabla.append(fila)

    # Añadir las diferencias divididas en diagonal
    for j in range(1, len(diferencias)):
        for i in range(j, len(diferencias)):
            resultados_tabla[i].append(f"{diferencias[j][i-j]}")
    
    # Rellenar las celdas vacías para la diagonal superior
    for i in range(len(resultados_tabla)):
        while len(resultados_tabla[i]) < len(diferencias) + 2:
            resultados_tabla[i].append("")  # Agregar celdas vacías

    return resultados_tabla


def mostrar_diferencias_divididas(resultados_tabla, tree):
    tree.delete(*tree.get_children())  # Limpiar la tabla antes de mostrar los datos

    for fila in resultados_tabla:
        tree.insert("", "end", values=fila)


def construir_polinomio_lagrange(diferencias, x_lista):
    x = sp.symbols('x')
    polinomio = diferencias[0][0]  # Comienza con el término independiente
    termino = 1  # Inicialmente el término es 1

    # Construir el polinomio sumando los términos con diferencias divididas y productos (x - xi)
    for i in range(1, len(diferencias)):
        termino *= (x - x_lista[i-1])
        polinomio += diferencias[i][0] * termino  # Agregar el nuevo término
    
    return polinomio


def mostrar_polinomio_lagrange(polinomio):
    polinomio_label.config(text=f"Polinomio de Lagrange: {sp.pretty(polinomio)}")


def resolver_diferencias_divididas():
    x_lista, y_lista = diferencias_divididas()
    if x_lista and y_lista:
        # Obtener el número de iteraciones para configurar la tabla
        k = int(ingresa_k.get())
        tree = configurar_tabla(k)  # Configurar la tabla según k

        # Calculamos todas las diferencias divididas
        diferencias = calcular_todas_diferencias_divididas(x_lista, y_lista)
        
        # Organizar los datos para mostrarlos en la tabla
        resultados_tabla = organizar_datos(x_lista, y_lista, diferencias)
        
        # Mostramos las diferencias divididas en la tabla
        mostrar_diferencias_divididas(resultados_tabla, tree)

        # Construir y mostrar el polinomio de Lagrange
        polinomio = construir_polinomio_lagrange(diferencias, x_lista)
        mostrar_polinomio_lagrange(polinomio)


# Botón para resolver
resolver = Button(frame1, width=20, text='Resolver', bg='brown', bd=5, command=resolver_diferencias_divididas)
resolver.grid(columnspan=2, row=4, pady=20, padx=10, sticky="ew")

root.mainloop()