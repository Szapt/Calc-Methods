import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtCore import Qt
import numpy as np
import math

class SimpsonGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Regla Compuesta de Simpson')

        layout = QVBoxLayout()
        self.a_label = QLabel('a:')
        self.a_input = QLineEdit()
        layout.addWidget(self.a_label)
        layout.addWidget(self.a_input)

        self.b_label = QLabel('b:')
        self.b_input = QLineEdit()
        layout.addWidget(self.b_label)
        layout.addWidget(self.b_input)

        self.n_label = QLabel('n:')
        self.n_input = QLineEdit()
        layout.addWidget(self.n_label)
        layout.addWidget(self.n_input)

        self.h_label = QLabel('h:')
        self.h_input = QLineEdit()
        layout.addWidget(self.h_label)
        layout.addWidget(self.h_input)

        self.func_label = QLabel('Función:')
        self.func_input = QLineEdit()
        layout.addWidget(self.func_label)
        layout.addWidget(self.func_input)

        self.calc_button = QPushButton('Calcular')
        self.calc_button.clicked.connect(self.calcular)
        layout.addWidget(self.calc_button)

        self.result_label = QLabel('Resultado:')
        self.result_text = QTextEdit()
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_text)

        self.setLayout(layout)

    def calcular(self):
        try:
            a = float(self.a_input.text())
            b = float(self.b_input.text())
            n = int(self.n_input.text())
            h = float(self.h_input.text())
            func = self.func_input.text()

            x = np.linspace(a, b, n+1)
            func_vec = np.vectorize(lambda x: eval(func, {'x': x, 'np': np, 'math': math}))
            y = func_vec(x)

            resultado, error = self.regla_compuesta_simpson(x, y)

            self.result_text.setText(f'Resultado: {resultado}\nError: {error}')
        except Exception as e:
            self.result_text.setText(f'Error: {str(e)}')

    def regla_compuesta_simpson(self, x, y):
        try:
            n = len(x) - 1
            h = x[1] - x[0]
            if h <= 0:
                raise ValueError("El paso debe ser positivo")
            if n < 2:
                raise ValueError("El número de subintervalos debe ser al menos 2")
            resultado = (h/3) * (y[0] + y[-1] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-1:2]))
            error = (h**4) / (180 * n**4) * np.abs((y[0] - 2*y[1] + y[2]))
            return resultado, error
        except ValueError as e:
            raise ValueError(f"Error en la regla compuesta de Simpson: {str(e)}")
        except Exception as e:
            raise Exception(f"Error desconocido: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimpsonGUI()
    ex.show()
    sys.exit(app.exec_())