from PyQt5 import QtWidgets
from sympy import symbols, lambdify, sympify, diff
import sys

class TrapezoidApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(TrapezoidApp, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Trapecio Compuesto")
        self.setStyleSheet("background-color: #f0f0f0;")  # Light gray background

        # Crear campos de entrada
        self.headerLabel = QtWidgets.QLabel("Trapecio Compuesto", self)
        self.headerLabel.setGeometry(50, 20, 400, 30)
        self.headerLabel.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")

        self.functionLineEdit = QtWidgets.QLineEdit(self)
        self.functionLineEdit.setPlaceholderText("Ingresa f(x)")
        self.functionLineEdit.setGeometry(50, 50, 200, 30)
        self.functionLineEdit.setStyleSheet("border: 1px solid #ccc; border-radius: 5px; padding: 5px;")

        self.aLineEdit = QtWidgets.QLineEdit(self)
        self.aLineEdit.setPlaceholderText("Ingresa limite inferior")
        self.aLineEdit.setGeometry(50, 100, 200, 30)
        self.aLineEdit.setStyleSheet("border: 1px solid #ccc; border-radius: 5px; padding: 5px;")

        self.bLineEdit = QtWidgets.QLineEdit(self)
        self.bLineEdit.setPlaceholderText("Ingresa limite superior")
        self.bLineEdit.setGeometry(50, 150, 200, 30)
        self.bLineEdit.setStyleSheet("border: 1px solid #ccc; border-radius: 5px; padding: 5px;")

        self.nLineEdit = QtWidgets.QLineEdit(self)
        self.nLineEdit.setPlaceholderText("Ingresa el núm de subintervalos n")
        self.nLineEdit.setGeometry(50, 200, 200, 30)
        self.nLineEdit.setStyleSheet("border: 1px solid #ccc; border-radius: 5px; padding: 5px;")

        # Botón para calcular
        self.calculateButton = QtWidgets.QPushButton("Obtener Integral", self)
        self.calculateButton.setGeometry(50, 250, 200, 40)
        self.calculateButton.setStyleSheet("background-color: #4CAF50; color: #fff; border: none; border-radius: 5px; padding: 10px;")
        self.calculateButton.clicked.connect(self.trapezoid_integration)

        # Etiqueta de resultados
        self.resultLabel = QtWidgets.QLabel(self)
        self.resultLabel.setGeometry(50, 300, 400, 50)
        self.resultLabel.setStyleSheet("font-size: 18px; font-weight: bold; color: #333;")

    def trapezoid_integration(self):
        try:
            # Recoger los valores ingresados
            function_str = self.functionLineEdit.text()
            a = float(self.aLineEdit.text())
            b = float(self.bLineEdit.text())
            n = int(self.nLineEdit.text())

            # Definir la función simbólica
            x = symbols('x')
            func_expr = sympify(function_str.replace('^', '**'))
            f = lambdify(x, func_expr)

            # Calcular la segunda derivada de f
            second_derivative_expr = diff(func_expr, x, 2)
            f_second_derivative = lambdify(x, second_derivative_expr)

            # Llamar a la función que implementa la regla del trapecio compuesto
            result = self.trapezoid_compound(f, f_second_derivative, a, b, n)
            
            # Mostrar el resultado
            self.resultLabel.setText(f"La integral desde {a} hasta {b}: {result}")

        except Exception as e:
            self.resultLabel.setText(f"Error: {str(e)}")

    def trapezoid_compound(self, f, f_second_derivative, a, b, n):
        h = (b - a) / n
        sum = f(a) + f(b)  # Primer y último término

        # Sumar los términos intermedios con un factor de 2
        for i in range(1, n):
            sum += 2 * f(a + i * h)

        # Calcular la integral con la regla del trapecio
        integral = (h / 2) * sum

        # Calcular el término de corrección basado en la segunda derivada
        e = (a + b) / 2  # Aproximación para el punto e
        correction = ((b - a) / (12 * n ** 2)) * f_second_derivative(e)

        # Restar la corrección
        corrected_integral = integral - correction

        return corrected_integral

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TrapezoidApp()
    window.setGeometry(100, 100, 500, 450)
    window.show()
    sys.exit(app.exec_())
