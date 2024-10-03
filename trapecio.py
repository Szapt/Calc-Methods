import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextBrowser
from PyQt5.QtGui import QFont

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Método del Trapecio')

        layout = QVBoxLayout()

        label_a = QLabel('Ingrese el valor de a:')
        self.campo_a = QLineEdit()
        layout.addWidget(label_a)
        layout.addWidget(self.campo_a)

        label_b = QLabel('Ingrese el valor de b:')
        self.campo_b = QLineEdit()
        layout.addWidget(label_b)
        layout.addWidget(self.campo_b)

        label_funcion = QLabel('Ingrese la función:')
        self.campo_funcion = QLineEdit()
        layout.addWidget(label_funcion)
        layout.addWidget(self.campo_funcion)

        boton_calcular = QPushButton('Calcular')
        boton_calcular.clicked.connect(self.calcular_integral)
        layout.addWidget(boton_calcular)

        self.resultados = QTextBrowser()
        layout.addWidget(self.resultados)

        self.setLayout(layout)

    def calcular_integral(self):
        try:
            a = float(self.campo_a.text())
            b = float(self.campo_b.text())
            funcion = self.campo_funcion.text()

            fa = eval(funcion.replace('x', str(a)), {"__builtins__": None}, {"math": math})
            fb = eval(funcion.replace('x', str(b)), {"__builtins__": None}, {"math": math})

            integral = ((b - a) * (fa + fb)) / 2

            error = abs(integral - self.integral_exacta(a, b, funcion))

            self.resultados.setText(f'Integral: {integral:.4f}\nError: {error:.4f}')
        except Exception as e:
            self.resultados.setText(f'Error: {str(e)}')

    def integral_exacta(self, a, b, funcion):
        if funcion == 'x**2':
            return (b**3 - a**3) / 3
        elif funcion == 'x**3':
            return (b**4 - a**4) / 4
        else:
            return 0  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
