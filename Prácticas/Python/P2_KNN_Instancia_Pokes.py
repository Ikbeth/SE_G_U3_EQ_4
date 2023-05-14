import math

def Coseno(A, B):
    dot_product = sum(a * b for a, b in zip(A, B))
    magnitude1 = math.sqrt(sum(a ** 2 for a in A))
    magnitude2 = math.sqrt(sum(b ** 2 for b in B))
    return 1 - dot_product / (magnitude1 * magnitude2)

###CARGAR INSTANCIA
archivo = open("InstanciaPokes.txt","r")  #ABRE EL ARCHIVO
contenido = archivo.readlines()  #LEE TODO EL CONTENIDO DEL ARCHIVO

#VISUALIZA EL CONTENIDO DEL ARCHIVO
print('\nArchivo Completo: ') #Impreso línea a línea
for l in contenido:
    print(l, end="") #por el formato en que se lee el archivo se quita el terminador (salto de linea) para evidar un doble salto
print("\n\n")

#CREA UNA LISTA EN LA QUE CADA ELEMENTO SEA UNA LINEA DEL ARCHIVO CONVERTIDA EN LISTA SEPARADA POR TABULADOR
lista = [linea.split("\t") for linea in contenido]

#VISUALIZA LISTA PROCESADA
print("Lista de listas separadas por tabulador: ")
#Impreso línea a línea
for l in lista:
    print(l)
print("\n\n")

#Pasar a ... Ejemplo:
# [ [ [ '80', '90' ,..., '90' ], 'Guerrero'],
#   [ [ '75', '59' ,..., '90' ], 'Duelista']
# ]

#CONVIERTE LA LISTA DE LISTAS EN LA INSTANCIA NECESARIA PARA TRABAJAR CON EL KNN
instancia = [ [ list(map(int,x[:5])), x[5].replace("\n","") ] for x in lista ]

#VISUALIZA EL CONTENIDO DEL ARCHIVO
print("Instancia Procesada: ")
#Impreso línea a línea
for l in instancia:
    print(l)
print("\n\n")
##############################################################################
##SELECCIÓN / CREACIÓN DEL VECTOR A CLASIFICAR
NC = [54,58,80,65,80] #NC = No Clasificado
# 54,58,80,65,80 = Fuego

##############################################################################
###DEFINIR EL VALOR DE "K"  - Un número entre 1 y el total de registros de la instancia
K = 7  #por ejemplo, k = 5
##############################################################################

estructuraDatos = {} ##diccionario que fungira como estructura de datos para las distancias

for NoCaso, registro in enumerate(instancia):  #por cada elemento/registro de la instancia
    distancia_NC_i = Coseno(NC, registro[0]) #registro[0] = vector carac   -- registro[1] = clase
    #print(distancia_NC_i)
    estructuraDatos[NoCaso] = distancia_NC_i

#VISUALIZA EL CONTENIDO DE LA ESTRUCTURA DE DATOS (TABLA DE DISTANCIAS)
print("TABLA DE DISTANCIAS: ")
#Impreso línea a línea
for key in estructuraDatos:
  print ("Registro ",key, " - Distancia con NC: ", estructuraDatos[key])
print("\n\n")

ordenado = sorted(estructuraDatos.items(), key=lambda x: x[1], reverse=True) ## 0 = NoCaso   1 = Distancia  -->> #retorna una lista de tuplas

#VISUALIZA EL CONTENIDO DE LA ESTRUCTURA DE DATOS (TABLA DE DISTANCIAS) ORDENADA
print("TABLA DE DISTANCIAS ORDENADA: ")
#Impreso línea a línea
for r in ordenado:
  print ("Registro ",r[0], " - Distancia con NC: ", r[1])
print("\n\n")


temporalK = []
for i in range(K):
    NumDeRegistro = ordenado[i][0] ##0 = NumDeCaso
    registro = instancia[NumDeRegistro] #registro correspondiente al indice (NumDeRegistro) consultado
    #print(registro)
    temporalK.append(registro[1]) ##clase/etiqueta asociada al "NumDeRegistro"

print("Clases de los K registros más parecidos(cercanos): ")
#Impreso línea a línea
for t in temporalK:
  print ("\t",t)
print("\n\n")

########################################################################
##ENCONTRAR LA MODA EN "TEMPORAL_K" PARA ASIGNAR ESA ETIQUETA/CLASE AL VECTOR "NC"

from statistics import mode #, multimode
claseModa = mode(temporalK)
#claseModa = multimode(temporalK)
print("Clase Asignada:", claseModa)
print("\n\n")

#
#Investigación. Tipos de Validación:
#
#   CrossValidation - Validación Cruzada
#   SplitValidation - Validación Segmentada  80%/20%  70%/30% 60%/40% => entrenamiento/prueba

