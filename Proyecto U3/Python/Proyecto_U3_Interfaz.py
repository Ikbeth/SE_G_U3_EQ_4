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

        self.cBoxPreArduino.model().item(0).setEnabled(False)
        self.cBoxPreArduino.model().item(1).setEnabled(False)
        self.cBoxPreArduino.model().item(2).setEnabled(False)
        self.cBoxPreArduino.model().item(3).setEnabled(False)
        self.cBoxPreArduino.model().item(4).setEnabled(False)
        self.cBoxPreArduino.model().item(5).setEnabled(True)


    # Área de los Slots
    def Generar (self):
        print();

    def Salir (self):
        # desconectar arduino

        sys.exit()

    def cantidad (self):
        if self.cBoxCantidad.currentText() == '1':
            self.cBoxPreArduino.model().item(0).setEnabled(False)
            self.cBoxPreArduino.model().item(1).setEnabled(False)
            self.cBoxPreArduino.model().item(2).setEnabled(False)
            self.cBoxPreArduino.model().item(3).setEnabled(False)
            self.cBoxPreArduino.model().item(4).setEnabled(False)
            self.cBoxPreArduino.model().item(5).setEnabled(True)
        else:
            self.cBoxPreArduino.model().item(0).setEnabled(True)
            self.cBoxPreArduino.model().item(1).setEnabled(True)
            self.cBoxPreArduino.model().item(2).setEnabled(True)
            self.cBoxPreArduino.model().item(3).setEnabled(True)
            self.cBoxPreArduino.model().item(4).setEnabled(True)
            self.cBoxPreArduino.model().item(5).setEnabled(False)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

