from PyQt5 import QtWidgets
from sympy import symbols, lambdify, sympify
import sys

class RichardsonApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(RichardsonApp, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Richardson Extrapolation")

        # Crear campos de entrada
        self.functionLineEdit = QtWidgets.QLineEdit(self)
        self.functionLineEdit.setPlaceholderText("Enter the function f(x)")
        self.functionLineEdit.setGeometry(50, 50, 200, 30)

        self.x0LineEdit = QtWidgets.QLineEdit(self)
        self.x0LineEdit.setPlaceholderText("Enter x0")
        self.x0LineEdit.setGeometry(50, 100, 200, 30)

        self.hLineEdit = QtWidgets.QLineEdit(self)
        self.hLineEdit.setPlaceholderText("Enter step size h")
        self.hLineEdit.setGeometry(50, 150, 200, 30)

        self.qLineEdit = QtWidgets.QLineEdit(self)
        self.qLineEdit.setPlaceholderText("Enter reduction factor q")
        self.qLineEdit.setGeometry(50, 200, 200, 30)

        self.pLineEdit = QtWidgets.QLineEdit(self)
        self.pLineEdit.setPlaceholderText("Enter order of error p")
        self.pLineEdit.setGeometry(50, 250, 200, 30)

        # Botón para calcular
        self.calculateButton = QtWidgets.QPushButton("Calculate", self)
        self.calculateButton.setGeometry(50, 300, 200, 40)
        self.calculateButton.clicked.connect(self.richardson_extrapolation)

        # Etiqueta de resultados
        self.resultLabel = QtWidgets.QLabel(self)
        self.resultLabel.setGeometry(50, 350, 400, 50)

    def richardson_extrapolation(self):
        try:
            # Recoger los valores ingresados
            function_str = self.functionLineEdit.text()
            x0 = float(self.x0LineEdit.text())
            h = float(self.hLineEdit.text())
            q = float(self.qLineEdit.text())
            p = int(self.pLineEdit.text())

            # Definir la función simbólica
            x = symbols('x')
            func_expr = sympify(function_str.replace('^', '**'))
            f = lambdify(x, func_expr)

            # Llamar a la función que implementa la extrapolación de Richardson
            result = self.richardson_derivative_general(f, x0, h, q, p)
            
            # Mostrar el resultado
            self.resultLabel.setText(f"Derivative at x = {x0}: {result}")

        except Exception as e:
            self.resultLabel.setText(f"Error: {str(e)}")

    def richardson_derivative_general(self, f, x0, h, q, p):
        # Derivada numérica básica con paso h
        F_h = (f(x0 + h) - f(x0)) / h
        # Derivada numérica con paso h/q
        F_hq = (f(x0 + (h / q)) - f(x0)) / (h / q)
        
        # Aplicamos tu fórmula de extrapolación de Richardson
        F_richardson = F_h + (F_h - F_hq) / (q**(-p) - 1)
        
        return F_richardson

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = RichardsonApp()
    window.setGeometry(100, 100, 500, 450)
    window.show()
    sys.exit(app.exec_())
