import numpy as np


def discretizar():
    with open('../Archivos/ebw.csv', 'r') as archivo:
        V = [int(num) for num in archivo.read().split(',')]

    k = int(input('INDIQUE LAS ITERACIONES: '))
    min = np.min(V)
    max = np.max(V)
    width = (max - min) / 2

    print('{}, {}, {}'.format(min, max, width))

    res = [[min + i * width, min + (i + 1) * width] for i in range(k)]

    for i in range(k):
        print(res[i])


if __name__ == '__main__':
    discretizar()
