def reta(superficie, inicio, fim, cor):
    xi, yi = round(inicio[0]), round(inicio[1])
    xf, yf = round(fim[0]), round(fim[1])

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


def desenha_eixo(superficie, ponto_a, ponto_b, cor, tamanho_tela):
    xi, yi = round(ponto_a[0]), round(ponto_a[1])
    xf, yf = round(ponto_b[0]), round(ponto_b[1])

    if (xf - xi) != 0:
        m = (yf - yi) / (xf - xi)
        y_0 = m * (0 - xi) + yi
        y_f = m * (tamanho_tela[0] - xi) + yi
    else:
        y_0 = 0
        y_f = tamanho_tela[1]

    if (yf - yi) != 0:
        m = (xf - xi) / (yf - yi)
        x_0 = m * (0 - yi) + xi
        x_f = m * (tamanho_tela[1] - yi) + xi
    else:
        x_0 = 0
        x_f = tamanho_tela[0]

    reta(superficie, (x_0, y_0), (x_f, y_f), cor)


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


# Função não utilizada, ta aqui pra possível uso futuro
def get_centro(face):
    menor_x = 10000
    menor_y = 10000
    maior_x = -10000
    maior_y = -10000

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


# Função não utilizada, ta aqui pra possível uso futuro
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
        novos_vertices.append([v[0]*xumax/xdmax, (v[1]-ydmax)*yumax/(-ydmax), v[2], v[3]])
    return novos_vertices


def parse_num(num):  # "0.5"
    try:
        return float(num.strip())

    except ValueError:
        print("Valor inserido é inválido.")


def parse_ponto(string):  # ex.: "0.1 0.2 0.3"
    coords = string.split(" ")
    if len(coords) != 3:
        print("Não foram inseridas 3 coordenadas para o ponto.")

    coords = [parse_num(coord) for coord in coords]
    return tuple(coords)
