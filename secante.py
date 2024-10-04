from PyQt5 import QtWidgets, QtGui, QtCore
from sympy import symbols, lambdify, sympify
import sys

class SecantApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(SecantApp, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Método de la Secante")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: #f0f0f0;")

        mainLayout = QtWidgets.QVBoxLayout()
        header = QtWidgets.QLabel("Método de la Secante")
        header.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Bold))
        header.setAlignment(QtCore.Qt.AlignCenter)
        mainLayout.addWidget(header)

        formLayout = QtWidgets.QFormLayout()
        
        self.functionLineEdit = QtWidgets.QLineEdit(self)
        self.functionLineEdit.setPlaceholderText("Ejemplo: x**2 - 4")
        formLayout.addRow("Función f(x):", self.functionLineEdit)

        self.x0LineEdit = QtWidgets.QLineEdit(self)
        self.x0LineEdit.setPlaceholderText("Ejemplo: 0.5")
        formLayout.addRow("Valor inicial x0:", self.x0LineEdit)

        self.x1LineEdit = QtWidgets.QLineEdit(self)
        self.x1LineEdit.setPlaceholderText("Ejemplo: 3.5")
        formLayout.addRow("Valor inicial x1:", self.x1LineEdit)

        self.iterationsLineEdit = QtWidgets.QLineEdit(self)
        self.iterationsLineEdit.setPlaceholderText("Ejemplo: 10")
        formLayout.addRow("Iteraciones:", self.iterationsLineEdit)

        mainLayout.addLayout(formLayout)

        self.calcButton = QtWidgets.QPushButton("Calcular Secante", self)
        self.calcButton.setFont(QtGui.QFont("Arial", 12))
        self.calcButton.setStyleSheet("background-color: #007acc; color: white; padding: 8px;")
        self.calcButton.clicked.connect(self.calculate_secant)
        mainLayout.addWidget(self.calcButton, alignment=QtCore.Qt.AlignCenter)

        self.resultTextBox = QtWidgets.QTextEdit(self)
        self.resultTextBox.setReadOnly(True)
        self.resultTextBox.setStyleSheet("background-color: #ffffff; color: #333;")
        mainLayout.addWidget(self.resultTextBox)

        centralWidget = QtWidgets.QWidget()
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)

    def calculate_secant(self):
        try:
            function_str = self.functionLineEdit.text()
            x0 = float(self.x0LineEdit.text())
            x1 = float(self.x1LineEdit.text())
            iterations = int(self.iterationsLineEdit.text())

            x = symbols('x')
            f_sympy = sympify(function_str)
            f = lambdify(x, f_sympy)

            result_log = f"<b>Resultados:</b><br>"
            for i in range(iterations):
                if f(x1) - f(x0) == 0:
                    self.resultTextBox.setHtml("<b>Error:</b> División por cero. Intenta con otros valores iniciales.")
                    return
                
                x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
                result_log += f"Iteración {i + 1}: x ≈ {x2:.6f}<br>"
                x0 = x1
                x1 = x2

            result_log += f"<br><b>Resultado final:</b> x ≈ {x1:.6f}"
            self.resultTextBox.setHtml(result_log)

        except Exception as e:
            self.resultTextBox.setHtml(f"<b>Error:</b> {e}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    secant_app = SecantApp()
    secant_app.show()
    sys.exit(app.exec_())
