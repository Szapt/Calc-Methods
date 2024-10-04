from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import subprocess
import os

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("La Calculadora de Clara :)")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: #f0f0f0;")

        mainLayout = QtWidgets.QVBoxLayout()
        header = QtWidgets.QLabel("La Calculadora de Clara :)")
        header.setFont(QtGui.QFont("Arial", 24, QtGui.QFont.Bold))
        header.setAlignment(QtCore.Qt.AlignCenter)
        header.setStyleSheet("color: #007acc;")
        mainLayout.addWidget(header)

        subheader = QtWidgets.QLabel("Seleccione el Método Numérico")
        subheader.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Bold))
        subheader.setAlignment(QtCore.Qt.AlignCenter)
        mainLayout.addWidget(subheader)

        # Crear un layout para las dos columnas
        columnsLayout = QtWidgets.QHBoxLayout()

        # Crear la primera columna
        column1Layout = QtWidgets.QVBoxLayout()
        column1Header = QtWidgets.QLabel("Derivación Númerica")
        column1Header.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Bold))
        column1Header.setAlignment(QtCore.Qt.AlignCenter)
        column1Layout.addWidget(column1Header)

        self.puntosButton = QtWidgets.QPushButton("Método por puntos", self)
        self.puntosButton.setFont(QtGui.QFont("Arial", 12))
        self.puntosButton.setStyleSheet("background-color: #007acc; color: white; padding: 8px; border-radius: 5px;")
        self.puntosButton.clicked.connect(self.open_puntos)
        column1Layout.addWidget(self.puntosButton)

        self.difDiviButton = QtWidgets.QPushButton("Método por diferencias divididas", self)
        self.difDiviButton.setFont(QtGui.QFont("Arial", 12))
        self.difDiviButton.setStyleSheet("background-color: #007acc; color: white; padding: 8px; border-radius: 5px;")
        self.difDiviButton.clicked.connect(self.open_difDivi)
        column1Layout.addWidget(self.difDiviButton)

        self.richardsonButton = QtWidgets.QPushButton("Extrapolación de Richardson", self)
        self.richardsonButton.setFont(QtGui.QFont("Arial", 12))
        self.richardsonButton.setStyleSheet("background-color: #007acc; color: white; padding: 8px; border-radius: 5px;")
        self.richardsonButton.clicked.connect(self.open_richardson)
        column1Layout.addWidget(self.richardsonButton)

        self.newtonButton = QtWidgets.QPushButton("Método de Newton", self)
        self.newtonButton.setFont(QtGui.QFont("Arial", 12))
        self.newtonButton.setStyleSheet("background-color: #007acc; color: white; padding: 8px; border-radius: 5px;")
        self.newtonButton.clicked.connect(self.open_newton)
        column1Layout.addWidget(self.newtonButton)

        self.secanteButton = QtWidgets.QPushButton("Método de la Secante", self)
        self.secanteButton.setFont(QtGui.QFont("Arial", 12))
        self.secanteButton.setStyleSheet("background-color: #007acc; color: white; padding: 8px; border-radius: 5px;")
        self.secanteButton.clicked.connect(self.open_secante)
        column1Layout.addWidget(self.secanteButton)

        # Crear la segunda columna
        column2Layout = QtWidgets.QVBoxLayout()
        column2Header = QtWidgets.QLabel("Integración Númerica")
        column2Header.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Bold))
        column2Header.setAlignment(QtCore.Qt.AlignCenter)
        column2Layout.addWidget(column2Header)

        self.trapecioButton = QtWidgets.QPushButton("Método del Trapecio", self)
        self.trapecioButton.setFont(QtGui.QFont("Arial", 12))
        self.trapecioButton.setStyleSheet("background-color: #007acc; color: white; padding: 8px; border-radius: 5px;")
        self.trapecioButton.clicked.connect(self.open_trapecio)
        column2Layout.addWidget(self.trapecioButton)

        self.trapecioCompuestoButton = QtWidgets.QPushButton("Método del Trapecio Compuesto", self)
        self.trapecioCompuestoButton.setFont(QtGui.QFont("Arial", 12))
        self.trapecioCompuestoButton.setStyleSheet("background-color: #007acc; color: white; padding: 8px; border-radius: 5px;")
        self.trapecioCompuestoButton.clicked.connect(self.open_trapecio_compuesto)
        column2Layout.addWidget(self.trapecioCompuestoButton)

        self.simpsonButton = QtWidgets.QPushButton("Método de Simpson", self)
        self.simpsonButton.setFont(QtGui.QFont("Arial", 12))
        self.simpsonButton.setStyleSheet("background-color: #007acc; color: white; padding: 8px; border-radius: 5px;")
        self.simpsonButton.clicked.connect(self.open_simpson)
        column2Layout.addWidget(self.simpsonButton)

        self.simpson38Button = QtWidgets.QPushButton("Método de Simpson 3/8", self)
        self.simpson38Button.setFont(QtGui.QFont("Arial", 12))
        self.simpson38Button.setStyleSheet("background-color: #007acc; color: white; padding:  8px; border-radius: 5px;")
        self.simpson38Button.clicked.connect(self.open_simpson38)
        column2Layout.addWidget(self.simpson38Button)

        self.simpson38Button = QtWidgets.QPushButton("Método Simpson Compuesto", self)
        self.simpson38Button.setFont(QtGui.QFont("Arial", 12))
        self.simpson38Button.setStyleSheet("background-color: #007acc; color: white; padding:  8px; border-radius: 5px;")
        self.simpson38Button.clicked.connect(self.open_compSimpson)
        column2Layout.addWidget(self.simpson38Button)

        self.puntoMedioButton = QtWidgets.QPushButton("Método del Punto Medio", self)
        self.puntoMedioButton.setFont(QtGui.QFont("Arial", 12))
        self.puntoMedioButton.setStyleSheet("background-color: #007acc; color: white; padding: 8px; border-radius: 5px;")
        self.puntoMedioButton.clicked.connect(self.open_punto_medio)
        column2Layout.addWidget(self.puntoMedioButton)

        self.puntoMedioCompuestoButton = QtWidgets.QPushButton("Método del Punto Medio Compuesto", self)
        self.puntoMedioCompuestoButton.setFont(QtGui.QFont("Arial", 12))
        self.puntoMedioCompuestoButton.setStyleSheet("background-color: #007acc; color: white; padding: 8px; border-radius: 5px;")
        self.puntoMedioCompuestoButton.clicked.connect(self.open_punto_medio_compuesto)
        column2Layout.addWidget(self.puntoMedioCompuestoButton)

        # Agregar las columnas al layout principal
        columnsLayout.addLayout(column1Layout)
        columnsLayout.addLayout(column2Layout)

        mainLayout.addLayout(columnsLayout)

        centralWidget = QtWidgets.QWidget()
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)

    def open_secante(self):
        # Abre el archivo de secante
        subprocess.Popen(['python', os.path.join('Calc-Methods', 'secante.py')])
        
    def open_difDivi(self):
        # Abre el archivo de diferencias divididas
        subprocess.Popen(['python', os.path.join('Calc-Methods', 'diferencias_divididas.py')])

    def open_punto_medio(self):
        # Abre el archivo de punto medio
        subprocess.Popen(['python', os.path.join('Calc-Methods', 'puntoMedio.py')])

    def open_punto_medio_compuesto(self):
        # Abre el archivo de punto medio compuesto
        subprocess.Popen(['python', os.path.join('Calc-Methods', 'medioCompuesto.py')])

    def open_newton(self):
        # Abre el archivo de newton
        subprocess.Popen(['python', os.path.join('Calc-Methods', 'newton.py')])

    def open_richardson(self):
        # Abre el archivo de richardson
        subprocess.Popen(['python', os.path.join('Calc-Methods', 'richardson.py')])

    def open_puntos(self):
        # Abre el archivo de richardson
        subprocess.Popen(['python', os.path.join('Calc-Methods', 'puntos.py')])

    def open_simpson(self):
        # Abre el archivo de simpson
        subprocess.Popen(['python', os.path.join('Calc-Methods', 'simpson.py')])

    def open_simpson38(self):
        # Abre el archivo de simpson 3/8
        subprocess.Popen(['python', os.path.join('Calc-Methods', 'simpson3.8.py')])

    def open_trapecio_compuesto(self):
        # Abre el archivo de trapecio compuesto
        subprocess.Popen(['python', os.path.join('Calc-Methods', 'trapcompu.py')])

    def open_trapecio(self):
        # Abre el archivo de trapecio
        subprocess.Popen(['python', os.path.join('Calc-Methods', 'trapecio.py')])

    def open_compSimpson(self):
        # Abre el archivo de trapecio
        subprocess.Popen(['python', os.path.join('Calc-Methods', 'compuesta-simpson.py')])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())