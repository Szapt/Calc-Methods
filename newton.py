from PyQt5 import QtWidgets
from sympy import symbols, diff, lambdify, sympify
import sys

class NewtonRaphsonApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(NewtonRaphsonApp, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Newton-Raphson Method")

        # Create input fields
        self.initialGuessLineEdit = QtWidgets.QLineEdit(self)
        self.initialGuessLineEdit.setPlaceholderText("Enter initial guess (x0)")
        self.initialGuessLineEdit.setGeometry(50, 50, 200, 30)

        self.functionLineEdit = QtWidgets.QLineEdit(self)
        self.functionLineEdit.setPlaceholderText("Enter the function (f(x))")
        self.functionLineEdit.setGeometry(50, 100, 200, 30)

        self.toleranceLineEdit = QtWidgets.QLineEdit(self)
        self.toleranceLineEdit.setPlaceholderText("Enter tolerance")
        self.toleranceLineEdit.setGeometry(50, 150, 200, 30)

        self.maxIterationsLineEdit = QtWidgets.QLineEdit(self)
        self.maxIterationsLineEdit.setPlaceholderText("Enter max iterations")
        self.maxIterationsLineEdit.setGeometry(50, 200, 200, 30)

        # Button to trigger calculation
        self.calculateButton = QtWidgets.QPushButton("Calculate", self)
        self.calculateButton.setGeometry(50, 250, 200, 40)
        self.calculateButton.clicked.connect(self.newton_raphson)

        # Output label
        self.resultLabel = QtWidgets.QLabel(self)
        self.resultLabel.setGeometry(50, 300, 400, 50)

    def newton_raphson(self):
        try:
            x0 = float(self.initialGuessLineEdit.text())
            fx = self.functionLineEdit.text()
            tolerance = float(self.toleranceLineEdit.text())
            maxIterations = int(self.maxIterationsLineEdit.text())

            # Symbolic math with sympy
            x = symbols('x')
            func_expr = sympify(fx)
            func = lambdify(x, func_expr)
            derivative = lambdify(x, diff(func_expr, x))

            # Newton-Raphson iteration
            iterations = 0
            x_current = x0

            while iterations < maxIterations:
                fx_value = func(x_current)
                fpx_value = derivative(x_current)

                # Check if derivative is zero (avoid division by zero)
                if fpx_value == 0:
                    self.resultLabel.setText("Derivative is zero. Stopping.")
                    return

                x_next = x_current - fx_value / fpx_value

                # Verificar convergencia en base a la diferencia entre x_current y x_next
                if abs(x_next - x_current) < tolerance:
                    self.resultLabel.setText(f"Root: {x_next}, Iterations: {iterations}")
                    return

                x_current = x_next
                iterations += 1

            # Si no se ha alcanzado la convergencia en el número máximo de iteraciones
            self.resultLabel.setText(f" Llega hasta la raíz {x_next}.Falla la convergencia para {iterations} iteraciones ")

        except Exception as e:
            self.resultLabel.setText(f"Error: {str(e)}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = NewtonRaphsonApp()
    window.setGeometry(100, 100, 500, 400)
    window.show()
    sys.exit(app.exec_())
