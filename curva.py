# De bezier
# P(t) = (1-t)^3 * P0 + 3*t*(1-t)^(2)*P1 + 3*t^(2)*(1-t)*P2+t^(3)*P3
# t pertence a [0,1]


import numpy as np
from objeto import Objeto
from face import Face


def bezier(intervalo, passo, pontos, superficie,cor):
    curva = []
    for t in np.arange(intervalo[0], intervalo[1], passo):
        ponto_curva = []
        for i in range(3):
            item_curva = ((1-t)**3)*pontos[0][i] + 3*t*((1-t)**2)*pontos[1][i] + 3*(t**2)*(1-t)*pontos[2][i]+(t**3)*pontos[3][i]
            ponto_curva.append(item_curva)
        ponto_curva.append(1)
        curva.append(ponto_curva)
    print(curva)
    curva_obj = Objeto([Face(superficie,
                             curva,
                             cor=cor,
                             preenchido=False),
                        Face(superficie,
                             curva,
                             cor=cor,
                             preenchido=False)])
    return curva_obj

#print(bezier([0, 1], 0.1, [[100,400,15],[300,400,5],[100,200,0],[300,200,-10]]))
