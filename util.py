from face import *
from vertice import *


def reta(superficie, inicio, fim, cor):
    xi, yi = inicio.x, inicio.y
    xf, yf = fim.x, fim.y

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
    xi, yi = inicio.x, inicio.y
    xf, yf = fim.x, fim.y

    xstep = 1
    if xf < xi:
        xstep = -1

    for x in range(xi, xf + 1, xstep):
        if (xf - xi) != 0:
            m = (yf - yi) / (xf - xi)
            y = m * (x - xi) + yi

            reta(superficie, origem, Vertice(x, int(y)), cor)

    ystep = 1
    if yf < yi:
        ystep = -1
    for y in range(yi, yf + 1, ystep):
        if (yf - yi) != 0:
            m = (xf - xi) / (yf - yi)
            x = m * (y - yi) + xi

            reta(superficie, origem, Vertice(int(x), y), cor)


def translada(face, tx=0, ty=0, tz=0):
    novos_vertices = []

    for vertice in face.vertices:
        novo_vertice = Vertice(vertice.x + tx, vertice.y + ty, vertice.z + tz)
        novos_vertices.append(novo_vertice)

    return Face(face.superficie, novos_vertices, face.cor)
