import csv
import random
import sys
import pandas as pd
import numpy as np
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "Ejercicio_4.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_exc.clicked.connect(self.accion)

    def accion(self):
        try:
            archivo = self.txt_Instancia.text() + ".xlsx"
            datos = pd.read_excel(archivo)
            totDatos = int(self.txt_totLeer.text())
            matriz = np.array(datos).reshape(49, 8)
            entre = int(self.txt_Entrenamiento.text())
            entrenamiento = []
            prueba = []
            if totDatos <= 49:
                np.random.shuffle(matriz)
                for i in range(totDatos):
                    if i <= entre:
                        entrenamiento.append(matriz[i])
                    else:
                        prueba.append(matriz[i])

            self.txt_Prueba.setText(str(totDatos - entre))

            archivo = open("Entrenamiento.csv", "w")
            for lectura in entrenamiento:
                archivo.write(str(lectura) + ",")

            archivo = open("Prueba.csv", "w")
            for lectura in entrenamiento:
                archivo.write(str(lectura) + ","+"/n")

        except Exception as error:
            print(error)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

#Aun faltan mejoras pero el objetivo ya lo hace