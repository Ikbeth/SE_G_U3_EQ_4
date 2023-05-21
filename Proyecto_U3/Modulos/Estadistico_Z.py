import numpy as np


def stdZ(vector):

    # GUARDAR NUMEROS

    inst = open('../Archivos/instancia.csv', "r")

    col1 = []
    col2 = []
    col3 = []
    col4 = []
    col5 = []

    umbralZ = 2.5

    for line in inst:
        datos = line.split(",")
        # print(datos)

        col1.append(int(datos[1]))
        col2.append(int(datos[2]))
        col3.append(int(datos[3]))
        col4.append(int(datos[4]))
        col5.append(int(datos[5]))

        # print("{}, {}, {}, {}, {}, {}".format(prom1, prom2, prom3, prom4, prom5, prom6))

    inst.close()

    col1 = np.array(col1)
    col2 = np.array(col2)
    col3 = np.array(col3)
    col4 = np.array(col4)
    col5 = np.array(col5)

    media1 = np.mean(col1)
    media2 = np.mean(col2)
    media3 = np.mean(col3)
    media4 = np.mean(col4)
    media5 = np.mean(col5)

    std1 = np.std(col1)
    std2 = np.std(col2)
    std3 = np.std(col3)
    std4 = np.std(col4)
    std5 = np.std(col5)

    z1 = ((vector[0] - media1) / std1)
    z2 = ((vector[1] - media2) / std2)
    z3 = ((vector[2] - media3) / std3)
    z4 = ((vector[3] - media4) / std4)
    z5 = ((vector[4] - media5) / std5)

    z = [z1, z2, z3, z4, z5]

    ex = False

    for i in range(5):
        if ex:
            break
        if z[i] < -umbralZ or z[i] > umbralZ:
            ex = True

    # print(ex)
    return ex


if __name__ == '__main__':
    stdZ([130,100,45,45,35])