import numpy as np
import pandas as pd
k = 6


def discretizar_rangos(vector):

    df = pd.read_csv('../Archivos/Entrenamiento_Pokes.csv', header=None)
    vector = pd.DataFrame(vector)
    vector = vector.transpose()
    # print(vector)

    ran1 = disc(df[0], k)
    vector[0] = vector[0].apply(condiciones, args=(ran1,))

    ran2 = disc(df[1], k)
    vector[1] = vector[1].apply(condiciones, args=(ran2,))

    ran3 = disc(df[2], k)
    vector[2] = vector[2].apply(condiciones, args=(ran3,))

    ran4 = disc(df[3], k)
    vector[3] = vector[3].apply(condiciones, args=(ran4,))

    ran5 = disc(df[4], k)
    vector[4] = vector[4].apply(condiciones, args=(ran5,))

    vector = vector.values.tolist()
    # print(vector[0])
    return vector[0]


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
    discretizar_rangos([75,100,100,80,30])
