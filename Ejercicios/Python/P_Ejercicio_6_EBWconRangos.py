import numpy as np
import pandas as pd

k = 6


def discretzar_rangos():
    df = pd.read_csv('../Archivos/100_pokemones_ACTUALIZADA.csv', header=None)

    col0 = df[0].values.tolist()
    col7 = df[7].values.tolist()
    # print(col0)

    ran1 = disc(df[1], k)
    newcol1 = df[1].apply(condiciones, args=(ran1, ))
    # print(newcol1)

    ran2 = disc(df[2], k)
    newcol2 = df[2].apply(condiciones, args=(ran2,))
    # print(newcol2)

    ran3 = disc(df[3], k)
    newcol3 = df[3].apply(condiciones, args=(ran3,))
    # print(newcol3)

    ran4 = disc(df[4], k)
    newcol4 = df[4].apply(condiciones, args=(ran4,))
    # print(newcol4)

    ran5 = disc(df[5], k)
    newcol5 = df[5].apply(condiciones, args=(ran5,))
    # print(newcol5)

    ran6 = disc(df[6], k)
    newcol6 = df[6].apply(condiciones, args=(ran6,))
    # print(newcol6)

    with open('../Archivos/instancia100Discretizada.csv', 'w') as archivo:
        for i in range(100):
            archivo.write(col0[i] + ',' + str(newcol1[i]) + ',' + str(newcol2[i]) + ',' + str(newcol3[i]) + ','
                          + str(newcol4[i]) + ',' + str(newcol5[i]) + ',' + str(newcol6[i]) + ',' + col7[i] + '\n')



def disc(data, k):
    min = np.min(data)
    max = np.max(data)
    width = (max - min) / k

    # print('{}, {}, {}'.format(min, max, width))

    res = [[min + i * width, min + (i + 1) * width] for i in range(k)]

    # for i in range(k):
    #     print(res[i])

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
    discretzar_rangos()
