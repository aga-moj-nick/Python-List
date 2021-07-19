# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.


def bez_parzystych (lista):
    lista2 = []
    for liczba in lista:  
        if liczba % 2 != 0:
            lista2.append (liczba)
    return lista2

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print (bez_parzystych (lista))
