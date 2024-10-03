from PyQt5 import QtWidgets  # Corrección aquí
from sympy import symbols, diff, lambdify
import sys

class NewtonRaphsonApp(QtWidgets.QMainWindow):  # Corrección aquí
    def __init__(self):
        super(NewtonRaphsonApp, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Newton-Raphson Method")

        # Create input fields
        self.initialGuessLineEdit = QtWidgets.QLineEdit(self)  # Corrección aquí
        self.initialGuessLineEdit.setPlaceholderText("Enter initial guess (x0)")
        self.initialGuessLineEdit.setGeometry(50, 50, 200, 30)

        self.functionLineEdit = QtWidgets.QLineEdit(self)  # Corrección aquí
        self.functionLineEdit.setPlaceholderText("Enter the function (f(x))")
        self.functionLineEdit.setGeometry(50, 100, 200, 30)

        self.toleranceLineEdit = QtWidgets.QLineEdit(self)  # Corrección aquí
        self.toleranceLineEdit.setPlaceholderText("Enter tolerance")
        self.toleranceLineEdit.setGeometry(50, 150, 200, 30)

        self.maxIterationsLineEdit = QtWidgets.QLineEdit(self)  # Corrección aquí
        self.maxIterationsLineEdit.setPlaceholderText("Enter max iterations")
        self.maxIterationsLineEdit.setGeometry(50, 200, 200, 30)

        # Button to trigger calculation
        self.calculateButton = QtWidgets.QPushButton("Calculate", self)  # Corrección aquí
        self.calculateButton.setGeometry(50, 250, 200, 40)
        self.calculateButton.clicked.connect(self.newton_raphson)

        # Output label
        self.resultLabel = QtWidgets.QLabel(self)  # Corrección aquí
        self.resultLabel.setGeometry(50, 300, 400, 50)

    def newton_raphson(self):
        try:
            x0 = float(self.initialGuessLineEdit.text())
            fx = self.functionLineEdit.text()
            tolerance = float(self.toleranceLineEdit.text())
            maxIterations = int(self.maxIterationsLineEdit.text())

            # Symbolic math with sympy
            x = symbols('x')
            func = lambdify(x, fx)
            derivative = lambdify(x, diff(fx, x))

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

                if abs(fx_value) < tolerance:
                    break

                x_current = x_next
                iterations += 1

            if abs(func(x_current)) < tolerance:
                self.resultLabel.setText(f"Root: {x_current}, Iterations: {iterations}")
            else:
                self.resultLabel.setText("Failed to converge within the given tolerance.")

        except Exception as e:
            self.resultLabel.setText(f"Error: {str(e)}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # Corrección aquí
    window = NewtonRaphsonApp()
    window.setGeometry(100, 100, 500, 400)
    window.show()
    sys.exit(app.exec_())
