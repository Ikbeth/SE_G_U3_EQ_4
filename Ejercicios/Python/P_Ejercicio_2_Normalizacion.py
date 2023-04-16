
def normalizacion():

    # MIN Y MAX

    min1 = 999
    max1 = 0
    min2 = 999
    max2 = 0
    min3 = 999
    max3 = 0
    min4 = 999
    max4 = 0
    min5 = 999
    max5 = 0
    min6 = 999
    max6 = 0

    inst = open('../Archivos/instancia.csv', "r")
    for line in inst:
        datos = line.split(",")
        # print(datos)

        if int(datos[1]) < min1:
            min1 = int(datos[1])
        elif int(datos[1]) > max1:
            max1 = int(datos[1])

        if int(datos[2]) < min2:
            min2 = int(datos[2])
        elif int(datos[2]) > max2:
            max2 = int(datos[2])

        if int(datos[3]) < min3:
            min3 = int(datos[3])
        elif int(datos[3]) > max3:
            max3 = int(datos[3])

        if int(datos[4]) < min4:
            min4 = int(datos[4])
        elif int(datos[4]) > max4:
            max4 = int(datos[4])

        if int(datos[5]) < min5:
            min5 = int(datos[5])
        elif int(datos[5]) > max5:
            max5 = int(datos[5])

        if int(datos[6]) < min6:
            min6 = int(datos[6])
        elif int(datos[6]) > max6:
            max6 = int(datos[6])

    print("-{}, {}, {}, {}, {}, {}".format(min1, min2, min3, min4, min5, min6))
    print("+{}, {}, {}, {}, {}, {}".format(max1, max2, max3, max4, max5, max6))

    inst.close()

    # NORMALIZAR

    inst = open('../Archivos/instancia.csv', "r")
    instestd = open("../Archivos/instanciaNormalizada.csv", "w")
    for line in inst:
        datos = line.split(",")
        # print(datos)

        n1 = (int(datos[1]) - min1) / (max1 - min1)
        n2 = (int(datos[2]) - min2) / (max2 - min2)
        n3 = (int(datos[3]) - min3) / (max3 - min3)
        n4 = (int(datos[4]) - min4) / (max4 - min4)
        n5 = (int(datos[5]) - min5) / (max5 - min5)
        n6 = (int(datos[6]) - min6) / (max6 - min6)

        instestd.write(datos[0] + "," + str(n1) + "," + str(n2) + "," + str(n3) + "," + str(n4) + "," +
                       str(n5) + "," + str(n6) + "," + datos[7] + "\n")

    inst.close()
    instestd.close()


if __name__ == "__main__":
    normalizacion()
