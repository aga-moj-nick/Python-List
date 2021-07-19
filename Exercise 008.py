# 8. Write a Python program to check a list is empty or not.


def sprawdzanie (lista):
    if len (lista) == 0:
        return 0
    else:
        return 1

lista = [1, 2, 3]

print (sprawdzanie (lista))
