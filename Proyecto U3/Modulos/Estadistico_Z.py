import numpy as np


def outliers():

    # GUARDAR NUMEROS

    inst = open('../Archivos/instancia.csv', "r")

    col1 = []
    col2 = []
    col3 = []
    col4 = []
    col5 = []
    col6 = []
    for line in inst:
        datos = line.split(",")
        # print(datos)

        col1.append(int(datos[1]))
        col2.append(int(datos[2]))
        col3.append(int(datos[3]))
        col4.append(int(datos[4]))
        col5.append(int(datos[5]))
        col6.append(int(datos[6]))

        # print("{}, {}, {}, {}, {}, {}".format(prom1, prom2, prom3, prom4, prom5, prom6))

    inst.close()

    col1 = np.array(col1)
    col1 = np.array(col1)
    col1 = np.array(col1)
    col1 = np.array(col1)
    col1 = np.array(col1)
    col1 = np.array(col1)

    media1 = np.mean(col1)
    media2 = np.mean(col2)
    media3 = np.mean(col3)
    media4 = np.mean(col4)
    media5 = np.mean(col5)
    media6 = np.mean(col6)

    std1 = np.std(col1)
    std2 = np.std(col2)
    std3 = np.std(col3)
    std4 = np.std(col4)
    std5 = np.std(col5)
    std6 = np.std(col6)

    z1 = ()
