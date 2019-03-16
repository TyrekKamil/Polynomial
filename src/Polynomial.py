from src.ulamek import *


def pier(p):
    lista = []
    i = p - 1
    while i > 1:
        if p % i == 0:
            lista.append(i)
        i = i - 1
    return lista


# def mieszaj(p, q):
#     mieszanka = []
#     minusy = []
#     for x in range(len(p)):
#         for y in range(len(q)):
#             a = q[y] / p[x]
#             mieszanka.append(a)
#     for x in range(len(mieszanka)):
#         minusy.append(mieszanka[x] * -1)
#     mieszanka.extend(minusy)
#     return mieszanka

# def sprawdz(pq, polynom):
#     trueOrFalse = []
#     for x in range(len(pq)):
#         wynik = 0;
#         print(polynom)
#         for y in range(len(polynom)):
#             wynik = wynik + polynom[y] * (pq[x] ** (y))
#             print(wynik)
#         if wynik == 0:
#             trueOrFalse.append(pq[x])
#
#     return trueOrFalse

def mieszaj(p, q):
    mieszanka = []
    minusy = []
    for x in range(len(p)):
        for y in range(len(q)):
            a = Ulamek(q[y], p[x])
            mieszanka.append(a)
    for x in range(len(mieszanka)):
        minusy.append(mnozenieUlamek(mieszanka[x], Ulamek(-1, 1)))
    mieszanka.extend(minusy)
    return mieszanka


def sprawdz(pq, polynom):
    trueOrFalse = []
    for x in range(len(pq)):
        wynik = 0;
        print(polynom)
        for y in range(len(polynom)):
            wynik = dodajUlamek(wynik, mnozenieUlamek(Ulamek(polynom[y], 1), potegujUlamek(pq[x], Ulamek(y, 1))))
            print(wynik)
        if wynik.licznik == 0:
            trueOrFalse.append(pq[x])

    return trueOrFalse


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
            item = float(item)
            polynom.append(item)
    # print(polynom)
    p = pier(polynom[len(polynom) - 1])
    q = pier(polynom[0])

    pq = mieszaj(p, q)

    pq.append(Ulamek(1, polynom[0]))
    pq.append(Ulamek(polynom[len(polynom) - 1], polynom[0]))

    pq.append(Ulamek(-1, polynom[0]))
    pq.append(Ulamek(-1 * polynom[len(polynom) - 1], polynom[0]))

    for i in range(len(pq)):
        print(pq[i].getUlamek())
    print("Pierwiastki rownania to:", sprawdz(pq, polynom))


main()
