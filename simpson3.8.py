import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtCore import Qt
import math


class SimpsonMethod(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Método de Simpson 3/8')

        layout = QVBoxLayout()

        # Campos de entrada
        self.a_label = QLabel('Valor de a:')
        self.a_edit = QLineEdit()
        layout.addWidget(self.a_label)
        layout.addWidget(self.a_edit)

        self.b_label = QLabel('Valor de b:')
        self.b_edit = QLineEdit()
        layout.addWidget(self.b_label)
        layout.addWidget(self.b_edit)

        self.h_label = QLabel('Valor de h:')
        self.h_edit = QLineEdit()
        layout.addWidget(self.h_label)
        layout.addWidget(self.h_edit)

        self.n_label = QLabel('Valor de n:')
        self.n_edit = QLineEdit()
        layout.addWidget(self.n_label)
        layout.addWidget(self.n_edit)

        self.func_label = QLabel('Funcion a integrar:')
        self.func_edit = QLineEdit()
        layout.addWidget(self.func_label)
        layout.addWidget(self.func_edit)

        self.calc_button = QPushButton('Calcular')
        self.calc_button.clicked.connect(self.calculate)
        layout.addWidget(self.calc_button)

        self.result_text = QTextEdit()
        layout.addWidget(self.result_text)

        self.setLayout(layout)

    def calculate(self):
        try:
            a = float(self.a_edit.text())
            b = float(self.b_edit.text())
            h = float(self.h_edit.text())
            n = int(self.n_edit.text())
            func_str = self.func_edit.text()

            if h <= 0:
                self.result_text.setText('Error: h debe ser un valor positivo')
                return

            def func(x):
                return eval(func_str)

            x = [a + i * h for i in range(n + 1)]
            y = [func(x_i) for x_i in x]
            integral = (3 * h / 8) * (y[0] + y[-1] + 3 * sum(y[1:-1:3]) + 3 * sum(y[2:-1:3]) + 2 * sum(y[3:-1:3]))

            error = self.error_estimate(a, b, n)

            self.result_text.setText(f'Resultado: {integral:.6f}\nError: {error:.6f}')
        except ValueError:
            self.result_text.setText('Error: Verificar que los valores ingresados sean válidos')
        except Exception as e:
            self.result_text.setText(f'Error: {str(e)}')

    def error_estimate(self, a, b, n):
        return (b - a) / (180 * n**4)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpsonMethod()
    window.show()
    sys.exit(app.exec_())