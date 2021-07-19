# 9. Write a Python program to clone or copy a list.


# Sposób1:
def kopiowanie (lista1):
    lista2 = []
    for cyfra in lista1:
        if cyfra not in lista2:
            lista2.append (cyfra)
    return (lista2)

lista1 = [1, 2, 3, 4, 5]
print (kopiowanie (lista1))


# Sposób2:
import copy

lista1 = [1, 2, 3, 4, 5]

lista2 = lista1

lista3 = copy.copy (lista1)

print (lista1)
print (lista2)
print (lista3)
