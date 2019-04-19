from face import *


def reta(superficie, inicio, fim, cor):
    xi, yi = inicio[0], inicio[1]
    xf, yf = fim[0], fim[1]

    xstep = 1
    if xf < xi:
        xstep = -1

    for x in range(xi, xf + 1, xstep):
        if (xf - xi) != 0:
            m = (yf - yi) / (xf - xi)
            y = m * (x - xi) + yi

            superficie.set_at([x, int(y)], cor)

    ystep = 1
    if yf < yi:
        ystep = -1
    for y in range(yi, yf + 1, ystep):
        if (yf - yi) != 0:
            m = (xf - xi) / (yf - yi)
            x = m * (y - yi) + xi

            superficie.set_at([int(x), y], cor)


def preenchimento(superficie, origem, inicio, fim, cor):
    xi, yi = inicio[0], inicio[1]
    xf, yf = fim[0], fim[1]

    xstep = 1
    if xf < xi:
        xstep = -1

    for x in range(xi, xf + 1, xstep):
        if (xf - xi) != 0:
            m = (yf - yi) / (xf - xi)
            y = m * (x - xi) + yi

            reta(superficie, origem, [x, int(y)], cor)

    ystep = 1
    if yf < yi:
        ystep = -1
    for y in range(yi, yf + 1, ystep):
        if (yf - yi) != 0:
            m = (xf - xi) / (yf - yi)
            x = m * (y - yi) + xi

            reta(superficie, origem, [int(x), y], cor)


def multiplica_matrizes(matA, matB):
    n_linhasA = len(matA)
    n_colunasA = len(matA[0])
    n_linhasB = len(matB)
    n_colunasB = len(matB[0])

    if n_colunasA != n_linhasB:
        return

    resultado = [[0 for row in range(n_colunasB)] for col in range(n_linhasA)]

    for i in range(n_linhasA):
        for j in range(n_colunasB):
            for k in range(n_colunasA):
                resultado[i][j] += matA[i][k] * matB[k][j]

    return resultado


def transpoe_vetor(vetor):
    resultado = []

    if type(vetor[0]) == list:  # Vetor na vertical
        for item in vetor:
            resultado.append(item[0])
    else:  # Vetor na horizontal (normal)
        for item in vetor:
            resultado.append([item])

    return resultado
