import numpy as np


def outliers(vector):

    # GUARDAR NUMEROS

    inst = open('../Archivos/instancia_entrenamiento.csv', "r")

    col1 = []
    col2 = []
    col3 = []
    col4 = []
    col5 = []

    for line in inst:
        datos = line.split(",")
        # print(datos)

        col1.append(int(datos[0]))
        col2.append(int(datos[1]))
        col3.append(int(datos[2]))
        col4.append(int(datos[3]))
        col5.append(int(datos[4]))

        #print("{}, {}, {}, {}, {}, {}".format(col1, col2, col3, col4, col5))

    inst.close()

    # ORDENAR

    col1.sort()
    col2.sort()
    col3.sort()
    col4.sort()
    col5.sort()

    #print(col3)
    # POSICION CUARTILES

    pos = []
    v = len(col1)

    for i in range(4):
        #print(v)
        pos.append(((i + 1) * (v + 1)) / 4)
    #print(pos)

    # VALOR CUARTILES 1 Y 3

    q1c1 = np.percentile(col1, 25)
    q3c1 = np.percentile(col1, 75)

    q1c2 = np.percentile(col2, 25)
    q3c2 = np.percentile(col2, 75)

    q1c3 = np.percentile(col3, 25)
    q3c3 = np.percentile(col3, 75)

    q1c4 = np.percentile(col4, 25)
    q3c4 = np.percentile(col4, 75)

    q1c5 = np.percentile(col5, 25)
    q3c5 = np.percentile(col5, 75)

    q1 = [q1c1, q1c2, q1c3, q1c4, q1c5]
    # IQR

    iqr1 = q3c1 - q1c1
    iqr2 = q3c2 - q1c2
    iqr3 = q3c3 - q1c3
    iqr4 = q3c4 - q1c4
    iqr5 = q3c5 - q1c5

    iqr = [iqr1, iqr2, iqr3, iqr4, iqr5]

    # OUTLIERS EXTREMOS

    exmin = []
    for i in range(5):
        exmin.append(q1[i] - 3 * iqr[i])

    exmax = []
    for i in range(5):
        exmax.append(q1[i] + 3 * iqr[i])

    # BUSCAR OUTLIERS

    ex = False

    for i in range(5):
        if ex:
            break
        if vector[i] < exmin[i] or vector[i] > exmax[i]:
            ex = True

    # print(ex)
    return ex


if __name__ == "__main__":
    outliers([130,200,45,45,35])
