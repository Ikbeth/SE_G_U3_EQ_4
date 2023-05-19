import numpy as np
import pandas as pd
k = 6
def discretizar_rangos(valores):


    df = pd.read_csv('../Archivos/Entrenamiento_Pokes.csv', header=None)

    col6 = df[5].values.tolist()
    #print(col6)

    ran1 = disc(df[0], k)
    newcol1 = df[0].apply(condiciones, args=(ran1,))
    # print(newcol1)

    ran2 = disc(df[1], k)
    newcol2 = df[1].apply(condiciones, args=(ran2,))
    # print(newcol2)

    ran3 = disc(df[2], k)
    newcol3 = df[2].apply(condiciones, args=(ran3,))
    # print(newcol3)

    ran4 = disc(df[3], k)
    newcol4 = df[3].apply(condiciones, args=(ran4,))
    # print(newcol4)

    ran5 = disc(df[4], k)
    newcol5 = df[4].apply(condiciones, args=(ran5,))
   # print(newcol5)

    disarr = np.array(valores)

    # Definimos los límites de los intervalos en los que queremos discretizar el arreglo
    limites = np.array([0, 17, 33, 50, 67, 83, 100])

    # Discretizamos el arreglo utilizando la función digitize() de NumPy
    arreglo_discreto = np.digitize(disarr, limites)

    #print(arreglo_discreto)
    p1 = 'V' + str(arreglo_discreto[0])
    p2 = 'V' + str(arreglo_discreto[1])
    p3 = 'V' + str(arreglo_discreto[2])
    p4 = 'V' + str(arreglo_discreto[3])
    p5 = 'V' + str(arreglo_discreto[4])

    arreglo = [p1, p2, p3, p4, p5]
    return arreglo

    with open('../Archivos/instanciaDiscretizada.csv', 'w') as archivo:
        for i in range(49):
            archivo.write(str(newcol1[i]) + ',' + str(newcol2[i]) + ',' + str(newcol3[i]) + ','
                          + str(newcol4[i]) + ',' + str(newcol5[i]) + ',' + col6[i] + '\n')



def disc(data, k):
    min = np.min(data)
    max = np.max(data)
    width = (max - min) / k

    res = [[min + i * width, min + (i + 1) * width] for i in range(k)]

    return res


def condiciones(val, ran):
    if val < ran[0][1]:
        return 'V1'
    elif ran[1][0] <= val < ran[1][1]:
        return 'V2'
    elif ran[2][0] <= val < ran[2][1]:
        return 'V3'
    elif ran[3][0] <= val < ran[3][1]:
        return 'V4'
    elif ran[4][0] <= val < ran[4][1]:
        return 'V5'
    elif val >= ran[5][0]:
        return 'V6'


if __name__ == '__main__':
    discretizar_rangos()
