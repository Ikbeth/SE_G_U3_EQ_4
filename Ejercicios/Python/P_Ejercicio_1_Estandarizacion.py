import math


def estandarizacion():

    # PROMEDIO

    inst = open('../Archivos/instancia.csv', "r")
    contador = 0
    prom1 = 0
    prom2 = 0
    prom3 = 0
    prom4 = 0
    prom5 = 0
    prom6 = 0
    for line in inst:
        datos = line.split(",")
        #print(datos)

        prom1 = prom1 + int(datos[1])
        prom2 = prom2 + int(datos[2])
        prom3 = prom3 + int(datos[3])
        prom4 = prom4 + int(datos[4])
        prom5 = prom5 + int(datos[5])
        prom6 = prom6 + int(datos[6])

        #print("{}, {}, {}, {}, {}, {}".format(prom1, prom2, prom3, prom4, prom5, prom6))

        contador = contador + 1

    inst.close()

    prom1 = prom1 / contador
    prom2 = prom2 / contador
    prom3 = prom3 / contador
    prom4 = prom4 / contador
    prom5 = prom5 / contador
    prom6 = prom6 / contador

    print("{}, {}, {}, {}, {}, {}".format(prom1, prom2, prom3, prom4, prom5, prom6))

    # DESVIACION ESTANDAR

    inst = open('../Archivos/instancia.csv', "r")
    contador = 0
    desv1 = 0
    desv2 = 0
    desv3 = 0
    desv4 = 0
    desv5 = 0
    desv6 = 0
    for line in inst:
        datos = line.split(",")
        # print(datos)

        #print("-{}, {}, {}, {}, {}, {}".format(datos[1], datos[2], datos[3], datos[4], datos[5], datos[6]))
        #print("*{}, {}, {}, {}, {}, {}".format(prom1, prom2, prom3, prom4, prom5, prom6))

        desv1 = desv1 + (pow((int(datos[1]) - prom1), 2))
        desv2 = desv2 + (pow((int(datos[2]) - prom2), 2))
        desv3 = desv3 + (pow((int(datos[3]) - prom3), 2))
        desv4 = desv4 + (pow((int(datos[4]) - prom4), 2))
        desv5 = desv5 + (pow((int(datos[5]) - prom5), 2))
        desv6 = desv6 + (pow((int(datos[6]) - prom6), 2))

        #print("{}, {}, {}, {}, {}, {}".format(desv1, desv2, desv3, desv4, desv5, desv6))

        contador = contador + 1

    inst.close()

    contador = contador - 1

    #print("{}, {}, {}, {}, {}, {}".format(desv1, desv2, desv3, desv4, desv5, desv6))

    desv1 = math.sqrt(desv1 / contador)
    desv2 = math.sqrt(desv2 / contador)
    desv3 = math.sqrt(desv3 / contador)
    desv4 = math.sqrt(desv4 / contador)
    desv5 = math.sqrt(desv5 / contador)
    desv6 = math.sqrt(desv6 / contador)

    print("{}, {}, {}, {}, {}, {}".format(desv1, desv2, desv3, desv4, desv5, desv6))

    # ESTADISTICO Z

    inst = open('../Archivos/instancia.csv', "r")
    instestd = open("../Archivos/instanciaEstandarizada.csv", "w")
    for line in inst:
        datos = line.split(",")
        # print(datos)

        z1 = (int(datos[1]) - prom1) / desv1
        z2 = (int(datos[2]) - prom2) / desv2
        z3 = (int(datos[3]) - prom3) / desv3
        z4 = (int(datos[4]) - prom4) / desv4
        z5 = (int(datos[5]) - prom5) / desv5
        z6 = (int(datos[6]) - prom6) / desv6

        # print("{}, {}, {}, {}, {}, {}".format(desv1, desv2, desv3, desv4, desv5, desv6))

        instestd.write(datos[0] + "," + str(z1) + "," + str(z2) + "," + str(z3) + "," + str(z4) + "," +
                       str(z5) + "," + str(z6) + "," + datos[7] + "\n")

    inst.close()
    instestd.close()


if __name__ == "__main__":
    estandarizacion()
