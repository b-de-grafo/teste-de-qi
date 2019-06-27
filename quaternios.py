from math import *


def produto_escalar(v1, v2):
    assert len(v1) == len(v2)
    
    soma = 0
    for i in range(len(v1)):
        soma += v1[i] * v2[i]
    
    return soma


def modulo(v):
    soma = 0
    for i in v:
        soma += i**2
    
    return sqrt(soma)


def produto_vetorial(a, b):
    i = a[1]*b[2]-a[2]*b[1]
    j = a[2]*b[0]-a[0]*b[2]
    k = a[0]*b[1]-a[1]*b[0]

    return i, j, k


def produto(x, v=(0, 0, 0)):
    return [x * vi for vi in v]


def conjugado(q):
    return q[0], -q[1], -q[2], -q[3]


def subtracao(v1, v2):
    vf = []
    for i in range(len(v1)):
        vf.append(v1[i] - v2[i])
    return vf


def adicao(v1, v2):
    vf = []
    for i in range(len(v1)):
        vf.append(v1[i] + v2[i])
    return vf


# rotacao (ponto, angulo, eixo_arbritario)
def rotacao(p, teta, eixo=(0, 0, 0)):
    assert len(p) == 3
    
    r = p
    s = cos(radians(teta/2))
    v = [sin(radians(teta/2)) * ni for ni in eixo]

    print(teta)
    print(eixo)
    print(r)
    print(s)
    print(v)
    
    s2r = produto(s**2, r) # vetor
    print(f"s2r: {s2r}")
    vv = produto_escalar(v, v) # escalar
    print(f"vv: {vv}")
    vvr = produto(vv, r) # vetor
    print(f"vvr: {vvr}")
    vr = produto_escalar(v, r) # escalar
    print(f"vr: {vr}")
    dois_vr = 2 * vr # escalar
    print(f"2vr: {dois_vr}")
    dois_vrv = produto(dois_vr, v) # vetor
    print(f"2vrv: {dois_vrv}")
    vxr = produto_vetorial(v, r)
    print(f"vxr: {vxr}")
    dois_svxr = produto(2*s, vxr)
    print(f"2svxr: {dois_svxr}")

    segunda_parte = adicao(vvr, dois_vrv) # vvr + dois_vrv
    segunda_parte = adicao(segunda_parte, dois_svxr) # vvr + dois_vrv + dois_svxr
    qpq = subtracao(s2r, segunda_parte)

    # qpq = subtracao(produto(s**2, r),
    #                 adicao((produto(produto_escalar(v, v), r)),
    #                        adicao(produto(2 * produto_escalar(v, r), v),
    #                               produto(2 * s, produto_vetorial(v, r)))))
    print(qpq)
    exit()
    
    return [qpq[0], qpq[1], qpq[2]]
