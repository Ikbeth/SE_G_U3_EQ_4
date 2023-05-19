import sys
from time import sleep
from Proyecto_U3.Modulos.Discretizar import discretizar_rangos
from Proyecto_U3.Modulos.Main import id3s
from Proyecto_U3.Modulos.Knn import knn
from Proyecto_U3.Modulos.Asociador_Lineal import asociador
from Proyecto_U3.Modulos.NaiveBayes import NaiveBayes
import serial as conectar
from PyQt5 import uic, QtWidgets

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

        self.arduino = None
        self.arduino = conectar.Serial(port="COM3", baudrate=9600, timeout=1)


    # Área de los Slots
    def Generar(self):
        try:
            # Envir una cadena que indique el tipo de preprocesamiento de datos usaremos
            # Ejemplo: A,30, el A se obtiene del preprocesmiento y el numero de cBoxCantidad
            self.cantidad = self.cBoxCantidad.currentText()
            self.preProcesamiento = self.cBoxPreArduino.currentText()
            if self.preProcesamiento == 'Menor':
                self.proceso = "A"
            elif self.preProcesamiento == 'Mayor':
                self.proceso = "B"
            elif self.preProcesamiento == 'Media':
                self.proceso = "C"
            elif self.preProcesamiento == 'Mediana':
                self.proceso = "D"
            elif self.preProcesamiento == 'Moda':
                self.proceso = "E"
            else:
                self.proceso = "Q"

            self.pre = self.proceso + "," + self.cantidad

            self.arduino.write(self.pre.encode())
            sleep(1)
            if not self.arduino == None:
                if self.arduino.isOpen():
                    self.cadena = self.arduino.readline()
                    self.cadena = self.cadena.decode()
                    self.cadena = self.cadena.replace("\n", "")
                    self.cadena = self.cadena.replace("\r", "")
            print(self.cadena)

            self.vector = self.cadena.split(",")
            self.vectorP = list(map(int, self.vector))
            print(self.vectorP)

            # Preprocesar en Python

            if self.cBoxIA.currentText() == 'ID3':
                self.arr = discretizar_rangos(self.vectorP)
                print(self.arr)
                self.clase = id3s(self.arr)

            elif self.cBoxIA.currentText() == 'Naive Bayes':
                self.arr = discretizar_rangos(self.vectorP)
                self.clase = NaiveBayes(self.vectorP)

            elif self.cBoxIA.currentText() == 'Asociador Lineal':
                self.clase = asociador(self.vectorP)

            elif self.cBoxIA.currentText() == 'KNN':
                self.clase = knn(self.vectorP)

            print(self.clase)

        except Exception as error:
            print(error)

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

