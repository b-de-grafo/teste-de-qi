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


def multiplicacao_matriz(mat1, mat2):
    #  TODO: testar
    linhas_1 = len(mat1)
    colunas_1 = len(mat1[0])
    linhas_2 = len(mat2)
    colunas_2 = len(mat2[0])

    if colunas_1 != linhas_2:
        print("Erro [multiplicacao_matriz] : colunas_1 != linhas_2")
        return

    resultado = [[0 for row in range(colunas_2)] for col in range(linhas_1)]

    for i in range(linhas_1):
        for j in range(colunas_2):
            for k in range(colunas_1):
                resultado[i][j] += mat1[i][k] * mat2[k][j]
    return resultado


def transpoe_vetor(vetor):
    resultado = []
    for item in vetor:
        resultado.append([item])
    return resultado

def d_transpoe_vetor(vetor):
    resultado = []
    for item in vetor:
        for valor in item:
            resultado.append(valor)
    return resultado
