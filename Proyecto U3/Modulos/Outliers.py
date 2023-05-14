import numpy as np


def outliers():

    # GUARDAR NUMEROS

    inst = open('../Archivos/instancia_entrenamiento.csv', "r")

    col1 = []
    col2 = []
    col3 = []
    col4 = []
    col5 = []
    col6 = []
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


    # IQR

    iqr1 = q3c1 - q1c1
    iqr2 = q3c2 - q1c2
    iqr3 = q3c3 - q1c3
    iqr4 = q3c4 - q1c4
    iqr5 = q3c5 - q1c5

    #print("{}, {}, {}, {}, {}, {}".format(iqr1, iqr2, iqr3, iqr4, iqr5, iqr6))

    # OUTLIERS SUA

    suamin1 = q1c1 - 1.5 * iqr1
    suamin2 = q1c2 - 1.5 * iqr2
    suamin3 = q1c3 - 1.5 * iqr3
    suamin4 = q1c4 - 1.5 * iqr4
    suamin5 = q1c5 - 1.5 * iqr5

    suamax1 = q1c1 + 1.5 * iqr1
    suamax2 = q1c2 + 1.5 * iqr2
    suamax3 = q1c3 + 1.5 * iqr3
    suamax4 = q1c4 + 1.5 * iqr4
    suamax5 = q1c5 + 1.5 * iqr5

    # OUTLIERS EXTREMOS

    exmin1 = q1c1 - 3 * iqr1
    exmin2 = q1c2 - 3 * iqr2
    exmin3 = q1c3 - 3 * iqr3
    exmin4 = q1c4 - 3 * iqr4
    exmin5 = q1c5 - 3 * iqr5

    exmax1 = q1c1 + 3 * iqr1
    exmax2 = q1c2 + 3 * iqr2
    exmax3 = q1c3 + 3 * iqr3
    exmax4 = q1c4 + 3 * iqr4
    exmax5 = q1c5 + 3 * iqr5

    # BUSCAR OUTLIERS

    sua1 = [valor for valor in col1 if valor < suamin1 or valor > suamax1]
    sua2 = [valor for valor in col2 if valor < suamin2 or valor > suamax2]
    sua3 = [valor for valor in col3 if valor < suamin3 or valor > suamax3]
    sua4 = [valor for valor in col4 if valor < suamin4 or valor > suamax4]
    sua5 = [valor for valor in col5 if valor < suamin5 or valor > suamax5]

    ex1 = [valor for valor in col1 if valor < exmin1 or valor > exmax1]
    ex2 = [valor for valor in col2 if valor < exmin2 or valor > exmax2]
    ex3 = [valor for valor in col3 if valor < exmin3 or valor > exmax3]
    ex4 = [valor for valor in col4 if valor < exmin4 or valor > exmax4]
    ex5 = [valor for valor in col5 if valor < exmin5 or valor > exmax5]

    # RESULTADOS

    print("Sua columna 1: {}".format(sua1))
    print("Extremos columna 1: {}".format(ex1))
    print("Sua columna 2: {}".format(sua2))
    print("Extremos columna 2: {}".format(ex2))
    print("Sua columna 3: {}".format(sua3))
    print("Extremos columna 3: {}".format(ex3))
    print("Sua columna 4: {}".format(sua4))
    print("Extremos columna 4: {}".format(ex4))
    print("Sua columna 5: {}".format(sua5))
    print("Extremos columna 5: {}".format(ex5))


if __name__ == "__main__":
    outliers()
