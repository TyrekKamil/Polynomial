def pier(p):
    lista = []
    i = p
    while i > 0:
        if p % i == 0:
            lista.append(i)
        i = i - 1
    return lista


def mieszaj(p, q):
    mieszanka = []
    minusy = []
    for x in range(len(p)):
        for y in range(len(q)):
            a = q[y] / p[x]
            mieszanka.append(a)
    for x in range(len(mieszanka)):
        minusy.append(mieszanka[x]*-1)
    mieszanka.extend(minusy)
    return mieszanka




def sprawdz(pq, polynom):
    trueOrFalse = []
    for x in range(len(pq)):
        wynik = 0;
        print(polynom)
        for y in range(len(polynom)):
            wynik = wynik + polynom[y]*(pq[x] ** (y))
            print(wynik)
        if wynik == 0:
            trueOrFalse.append(pq[x])

    return trueOrFalse


x0 = 6
x1 = -5
x2 = -2
x3 =  1
polynom = [x0, x1, x2, x3]
p = pier(x3)
q = pier(x0)

pq = mieszaj(p, q)
print(sprawdz(pq, polynom))
