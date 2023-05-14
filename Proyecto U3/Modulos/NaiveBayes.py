if __name__ == '__main__':
    file2read = open("../Archivos/instanciaDiscretizada.csv")
    file_content = file2read.readlines()

    dataset = []
    for i in file_content:
        dataset.append((i.replace("\n", "")).split(","))
    headers = dataset[0]
    del dataset[0]
    # print(dataset)

    ##count registers per class

    probabilities = []
    auxiliar = {}
    for register_index in range(len(dataset)):
        label = dataset[register_index][-1]
        if label in auxiliar:
            auxiliar[label] += 1
        else:
            auxiliar[label] = 1
    probabilities.append(auxiliar)
    # print(probabilities)

    ##count registers per attribute

    for attribute_index in range(len(dataset[0]) - 1):
        auxiliar = {}
        for register_index in range(len(dataset)):
            v_label = dataset[register_index][attribute_index]
            v_class = dataset[register_index][-1]
            if (v_label, v_class) in auxiliar:
                auxiliar[(v_label, v_class)] += 1
            else:
                auxiliar[(v_label, v_class)] = 1
                # print(v_label, "  ", v_class)
        probabilities.append(auxiliar)
    # list(map(print,probabilities))

    for index in range(1, len(probabilities)):
        for c in probabilities[index]:  # per attribute

            probabilities[index][c] = probabilities[index][c] / probabilities[0][c[1]]

    for c in probabilities[0]:
        probabilities[0][c] = probabilities[0][c] / len(dataset)
    # list(map(print,probabilities))

    # TESTING

    file2read = open("../Archivos/instanciaDiscretizada.csv") # CAMBIAR A DATOS DEL ARDUINO
    file_content = file2read.readlines()

    dataset = []
    for i in file_content:
        dataset.append((i.replace("\n", "")).split(","))
    headers = dataset[0]
    del dataset[0]

    # DE PREFERENCIA CAMBIAR LECTURA A VARIABLE DE LISTA/ QUITAR FORs

    correct_classify = 0

    for k in range(len(dataset)):
        register = dataset[k]
        sum = 0
        probabilities_per_class = {}
        for c in probabilities[0]:
            # print(c)
            auxiliar = probabilities[0][c]
            for index in range(1, len(probabilities)):
                if (register[index - 1], c) in probabilities[index]:
                    auxiliar *= probabilities[index][(register[index - 1], c)]
                else:
                    auxiliar = 0  # nullify the product
            sum += auxiliar
            probabilities_per_class[c] = auxiliar
        # print(probabilities_per_class)

        max = -9999
        c_toAssign = ""
        for p in probabilities_per_class:
            probabilities_per_class[p] = probabilities_per_class[p] / sum
            if probabilities_per_class[p] > max:
                max = probabilities_per_class[p]
                c_toAssign = p

    res = 'calse asignada: ' + c_toAssign