
def Multiples():
    lista = [0]
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            lista.append(i)
    print(sum(lista))
    return lista

Multiples()