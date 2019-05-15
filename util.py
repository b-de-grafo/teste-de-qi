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


def multiplica_matrizes(matA, matB):
    n_linhasA = len(matA)
    n_colunasA = len(matA[0])
    n_linhasB = len(matB)
    n_colunasB = len(matB[0])

    if n_colunasA != n_linhasB:
        return 'deu erro n_colunasA != n_linhasB'

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


# Função não utilizada, ta aqui pra talvez uso futuro
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


# Função não utilizada, ta aqui pra talvez uso futuro
def get_centro(face):
    menor_x = 10000
    menor_y = 10000
    maior_x = 0
    maior_y = 0

    for vertice in face.vertices:
        if vertice[0] < menor_x:
            menor_x = vertice[0]
        if vertice[0] > maior_x:
            maior_x = vertice[0]
        if vertice[1] < menor_y:
            menor_y = vertice[1]
        if vertice[1] > maior_y:
            maior_y = vertice[1]

    largura = maior_x - menor_x
    altura = maior_y - menor_y

    return menor_x + (largura // 2), menor_y + (altura // 2)


# Função não utilizada, ta aqui pra talvez uso futuro
def get_canto(face):
    menor_x = 10000
    menor_y = 10000

    for vertice in face.vertices:
        if vertice[0] < menor_x:
            menor_x = vertice[0]
        if vertice[1] < menor_y:
            menor_y = vertice[1]

    return menor_x, menor_y


def srd_sru(vertices, xdmax, xumax, ydmax, yumax):
    novos_vertices = []
    for v in vertices:
        print(v[0]*xumax/xdmax)
        print((v[1]-ydmax)*yumax/(-ydmax))
        novos_vertices.append([v[0]*xumax/xdmax, (v[1]-ydmax)*yumax/(-ydmax), v[2], v[3]])
    return novos_vertices

# print(srd_sru([[0, 0, 1, 1], [75, 75, 1, 1], [0, 150, 1, 1], [0, 100, 1, 1], [-100, 100, 1, 1], [-100, 50, 1, 1], [0, 50, 1, 1]], 600, 1000, 600, 1500)) # seta
# print(srd_sru([[0, 0, 100, 1], [50, 0, 100, 1], [75, 25, 100, 1], [25, 100, 100, 1], [-25, 25, 100, 1]], 600, 1000, 600, 1500)) # diamante
# print(srd_sru([[0, 0, 1, 1], [100, 0, 1, 1], [50, 50, 1, 1], [100, 100, 1, 1], [0, 100, 1, 1], [-75, 50, 1, 1]], 600, 1000, 600, 1500)) # bandeira
# print(srd_sru([[0, 0, 1, 1], [25, 25, 1, 1], [25, 50, 1, 1], [50, 50, 1, 1], [25, 75, 1, 1], [0, 75, 1, 1], [0, 100, 1, 1], [-25, 75, 1, 1], [-25, 50, 1, 1], [-50, 50, 1, 1], [-25, 25, 1, 1], [0, 25, 1, 1]], 600, 1000, 600, 1500)) # cata_vento
# print(srd_sru([[0, 0, 1, 1], [50, 0, 1, 1], [50, 50, 1, 1], [100, 50, 1, 1], [100, 100, 1, 1], [50, 100, 1, 1], [50, 150, 1, 1], [0, 150, 1, 1], [0, 100, 1, 1], [-50, 100, 1, 1], [-50, 50, 1, 1], [0, 50, 1, 1]], 600, 1000, 600, 1500)) # cruz

# print(srd_sru([[0, 0, 1, 1], [20, 0, 1, 1], [15, 30, 1, 1], [50, 35, 1, 1], [0, 125, 1, 1], [10, 50, 1, 1], [-25, 50, 1, 1]], 600, 1000, 600, 1500)) # raio
# print(srd_sru([[0, 0, 1, 1], [18, -67, 1, 1], [67, -116, 1, 1], [134, -134, 1, 1], [201, -116, 1, 1], [250, -67, 1, 1], [268, 0, 1, 1], [250, 67, 1, 1], [201, 116, 1, 1], [134, 134, 1, 1], [67, 116, 1, 1], [18, 67, 1, 1]], 600, 1000, 600, 1500)) # dodecagono
# print(srd_sru([[0, 0, 1, 1], [15, 25, 1, 1], [50, 25, 1, 1], [25, 40, 1, 1], [35, 75, 1, 1], [0, 55, 1, 1], [-35, 75, 1, 1], [-25, 40, 1, 1], [-50, 25, 1, 1], [-15, 25, 1, 1]], 600, 1000, 600, 1500)) # estrela
# print(srd_sru([[0, 0, 1, 1], [15, 25, 1, 1], [50, 25, 1, 1], [25, 50, 1, 1], [50, 75, 1, 1], [15, 75, 1, 1], [0, 100, 1, 1], [-15, 75, 1, 1], [-50, 75, 1, 1], [-25, 50, 1, 1], [-50, 25, 1, 1], [-15, 25, 1, 1]], 600, 1000, 600, 1500)) # estrela de davi