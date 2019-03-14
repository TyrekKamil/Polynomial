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

    wynik = 0
    polynom[::-1]
    for x in range(len(pq)):
        print(polynom)
        for y in range(len(polynom)):
            wynik = wynik + pq[x]*(polynom[y]) ** y
            print(wynik)
        if wynik == 0:
            trueOrFalse.append(True)
        else:
            trueOrFalse.append(False)
    return trueOrFalse


x0 = 1
x1 = -2
x2 = -1
x3 =  2
polynom = [x0, x1, x2, x3]
p = pier(x3)
q = pier(x0)

print(q)
print(p)

pq = mieszaj(p, q)
print(sprawdz(pq, polynom))

print(pq)
