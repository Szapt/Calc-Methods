from PyQt5 import QtWidgets, QtGui, QtCore
from sympy import symbols, lambdify, sympify
import sys

class MidpointApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MidpointApp, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Método del Punto Medio")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: #f0f0f0;")

        mainLayout = QtWidgets.QVBoxLayout()
        header = QtWidgets.QLabel("Método del Punto Medio")
        header.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Bold))
        header.setAlignment(QtCore.Qt.AlignCenter)
        mainLayout.addWidget(header)

        formLayout = QtWidgets.QFormLayout()
        
        self.functionLineEdit = QtWidgets.QLineEdit(self)
        self.functionLineEdit.setPlaceholderText("Ejemplo: x**2")
        formLayout.addRow("Función f(x):", self.functionLineEdit)

        self.aLineEdit = QtWidgets.QLineEdit(self)
        self.aLineEdit.setPlaceholderText("Ejemplo: 0")
        formLayout.addRow("Límite inferior a:", self.aLineEdit)

        self.bLineEdit = QtWidgets.QLineEdit(self)
        self.bLineEdit.setPlaceholderText("Ejemplo: 1")
        formLayout.addRow("Límite superior b:", self.bLineEdit)

        mainLayout.addLayout(formLayout)

        self.calcButton = QtWidgets.QPushButton("Calcular Punto Medio", self)
        self.calcButton.setFont(QtGui.QFont("Arial", 12))
        self.calcButton.setStyleSheet("background-color: #007acc; color: white; padding: 8px;")
        self.calcButton.clicked.connect(self.calculate_midpoint)
        mainLayout.addWidget(self.calcButton, alignment=QtCore.Qt.AlignCenter)

        self.resultTextBox = QtWidgets.QTextEdit(self)
        self.resultTextBox.setReadOnly(True)
        self.resultTextBox.setStyleSheet("background-color: #ffffff; color: #333;")
        mainLayout.addWidget(self.resultTextBox)

        centralWidget = QtWidgets.QWidget()
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)

    def calculate_midpoint(self):
        try:
            function_str = self.functionLineEdit.text()
            a = float(self.aLineEdit.text())
            b = float(self.bLineEdit.text())

            x = symbols('x')
            f_sympy = sympify(function_str)
            f = lambdify(x, f_sympy)

            midpoint = (a + b) / 2
            result = f(midpoint) * (b - a)

            self.resultTextBox.setHtml(f"<b>Resultado:</b> ∫f(x)dx ≈ {result:.6f}")

        except Exception as e:
            self.resultTextBox.setHtml(f"<b>Error:</b> {e}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    midpoint_app = MidpointApp()
    midpoint_app.show()
    sys.exit(app.exec_())
