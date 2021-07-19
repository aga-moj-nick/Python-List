# 7. Write a Python program to remove duplicates from a list.


def usuwanie (lista1):
    lista2 = []
    for cyfra in lista1:
        if cyfra not in lista2:
            lista2.append (cyfra)
    return lista2

lista1 = [1, 2, 2, 2, 3, 4, 5]
print (usuwanie (lista1))
