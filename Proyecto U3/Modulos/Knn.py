import math

def knn(vectorP):

    def Coseno(A, B):
        dot_product = sum(a * b for a, b in zip(A, B))
        magnitude1 = math.sqrt(sum(a ** 2 for a in A))
        magnitude2 = math.sqrt(sum(b ** 2 for b in B))
        return 1 - dot_product / (magnitude1 * magnitude2)

    ###CARGAR INSTANCIA
    archivo = open("../Archivos/InstanciaPokesKnn.txt", "r")  # ABRE EL ARCHIVO
    contenido = archivo.readlines()  # LEE TODO EL CONTENIDO DEL ARCHIVO


    #print('\nArchivo Completo: ')
    #for l in contenido:
        #print(l, end="")  # por el formato en que se lee el archivo se quita el terminador (salto de linea) para evidar un doble salto
    #print("\n\n")

    lista = [linea.split("\t") for linea in contenido]

    # VISUALIZA LISTA PROCESADA
    #print("Lista de listas separadas por tabulador: ")
    # Impreso línea a línea
    #for l in lista:
     #   print(l)
    #print("\n\n")

    instancia = [[list(map(int, x[:5])), x[5].replace("\n", "")] for x in lista]

    # VISUALIZA EL CONTENIDO DEL ARCHIVO
    #print("Instancia Procesada: ")
    # Impreso línea a línea
    #for l in instancia:
    #    print(l)
    #print("\n\n")

    NC = vectorP

    K = 7

    estructuraDatos = {}

    for NoCaso, registro in enumerate(instancia):  # por cada elemento/registro de la instancia
        distancia_NC_i = Coseno(NC, registro[0])  # registro[0] = vector carac   -- registro[1] = clase
        # print(distancia_NC_i)
        estructuraDatos[NoCaso] = distancia_NC_i

    # VISUALIZA EL CONTENIDO DE LA ESTRUCTURA DE DATOS (TABLA DE DISTANCIAS)
    #print("TABLA DE DISTANCIAS: ")
    # Impreso línea a línea
    #for key in estructuraDatos:
     #   print("Registro ", key, " - Distancia con NC: ", estructuraDatos[key])
    #print("\n\n")

    ordenado = sorted(estructuraDatos.items(), key=lambda x: x[1], reverse=True)  ## 0 = NoCaso   1 = Distancia  -->> #retorna una lista de tuplas

    # VISUALIZA EL CONTENIDO DE LA ESTRUCTURA DE DATOS (TABLA DE DISTANCIAS) ORDENADA
    #print("TABLA DE DISTANCIAS ORDENADA: ")
    # Impreso línea a línea
    #for r in ordenado:
     #   print("Registro ", r[0], " - Distancia con NC: ", r[1])
    #print("\n\n")

    temporalK = []
    for i in range(K):
        NumDeRegistro = ordenado[i][0]  ##0 = NumDeCaso
        registro = instancia[NumDeRegistro]  # registro correspondiente al indice (NumDeRegistro) consultado
        # print(registro)
        temporalK.append(registro[1])  ##clase/etiqueta asociada al "NumDeRegistro"

    #print("Clases de los K registros más parecidos(cercanos): ")
    # Impreso línea a línea
    #for t in temporalK:
        #print("\t", t)
    #print("\n\n")

    ########################################################################
    ##ENCONTRAR LA MODA EN "TEMPORAL_K" PARA ASIGNAR ESA ETIQUETA/CLASE AL VECTOR "NC"

    from statistics import mode  # , multimode
    claseModa = mode(temporalK)
    # claseModa = multimode(temporalK)
    #print("Clase Asignada:", claseModa)
    #print("\n\n")
    clase = "Clase Asignada: " + claseModa

    return clase

if __name__ == "__main__":
    knn()

