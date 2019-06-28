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

def unitariza(v):
	soma = 0
	for e in v:
		soma += e ** 2
	soma = sqrt(soma)
	return [e / soma for e in v]


# rotacao (ponto, angulo, eixo_arbritario)
def rotacao(p, teta, eixo=(0, 0, 0)):
	assert len(p) == 3

	eixo = unitariza(eixo)
	r = p
	s = float('%.4f' % (cos(radians(teta/2))))
	v = [float('%.4f' % (sin(radians(teta/2)))) * ni for ni in eixo]

	s2r = produto(s**2, r)
	vv = produto_escalar(v, v)
	vvr = produto(vv, r)
	vr = produto_escalar(v, r)
	dois_vr = 2 * vr
	dois_vrv = produto(dois_vr, v)
	vxr = produto_vetorial(v, r)
	dois_svxr = produto(2*s, vxr)

	sub = subtracao(s2r, vvr)
	ad1 = adicao(sub, dois_vrv)
	qpq = adicao(ad1, dois_svxr)

	return [round(qpq[0]), round(qpq[1]), round(qpq[2])]


print(rotacao((10, -5, 0), 120, (0.5, 0.5, 0.5)))
