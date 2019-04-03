from Crypto.Util.number import bignum


def pier(p):
    lista = []
    i = abs(p);
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
            if a not in mieszanka:
                mieszanka.append(a)
    for x in range(len(mieszanka)):
        minusy.append(mieszanka[x] * -1)
    mieszanka.extend(minusy)
    return mieszanka

def sprawdz(pq, polynom):
    trueOrFalse = []
    for x in range(len(pq)):
        wynik = 0;
        for y in range(len(polynom)):
            wynik = wynik + polynom[y] * (pq[x] ** (y))
        if wynik == 0:
            trueOrFalse.append(pq[x])

    return trueOrFalse

def der(p):
    pom = []
    p.remove(p[0])
    for i in range(0,len(p)):
        pom.append(p[i]*(i+1))
    return pom

########################################          MAIN        ##############################################################################

def main():
    i = -1
    polynom = []
    print("Wypisz kolejne współczynniki. Aby zakończyć pozostaw puste pole i wciśnij ENTER.")
    while 1:
        i += 1
        item = input('x{} = '.format(i))
        if item == '':
            break
        else:
            item = bignum(item)
            polynom.append(item)
    # print(polynom)
    p = pier(polynom[len(polynom) - 1])
    q = pier(polynom[0])
    pq = mieszaj(p, q)

    wynik = sprawdz(pq, polynom)
    print("Pierwiastki rownania to:\n", wynik)

    while(len(wynik) > 0):
        polynom = der(polynom)
        wynik2 = sprawdz(wynik, polynom)
        if len(wynik2) >= 1:
            print(wynik2)
        wynik = wynik2;




main()
