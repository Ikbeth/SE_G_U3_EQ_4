import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "Proyecto_U3_Interfaz.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals

        # conectar arduino

        self.btnGenerar.clicked.connect(self.Generar)
        self.btnSalir.clicked.connect(self.Salir)
        self.cBoxCantidad.activated.connect(self.cantidad)
        self.cBoxIA.activated.connect(self.IA)

        self.listaPreArduino = ['Ninguna', ['Media', 'Mediana', 'Moda', 'Menor', 'Mayor']]

        if self.cBoxCantidad.currentText() == '1':
            self.cBoxPreArduino.clear()
            self.cBoxPreArduino.addItem(self.listaPreArduino[0])

        if self.cBoxIA.currentText() == 'ID3':
            self.cBoxDiscretizar.clear()
            self.cBoxDiscretizar.addItem('Si')


    # Área de los Slots
    def Generar(self):
        print();

    def Salir(self):
        # desconectar arduino

        sys.exit()

    def cantidad(self):
        if self.cBoxCantidad.currentText() == '1':
            self.cBoxPreArduino.clear()
            self.cBoxPreArduino.addItem(self.listaPreArduino[0])
        else:
            self.cBoxPreArduino.clear()
            self.cBoxPreArduino.addItems(self.listaPreArduino[1])

    def IA(self):
        if self.cBoxIA.currentText() == 'ID3' or self.cBoxIA.currentText() == 'Naive Bayes':
            self.cBoxDiscretizar.clear()
            self.cBoxDiscretizar.addItem('Si')
        else:
            self.cBoxDiscretizar.clear()
            self.cBoxDiscretizar.addItem('No')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

