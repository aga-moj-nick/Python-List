# 10. Write a Python program to find the list of words that are longer than n from a given list of words.



def lista_słów (n, str):
    długość_słowa = []
    tekst = str.split (" ")
    for i in tekst:
        if len (i) > n:
            długość_słowa.append (i)
    return długość_słowa

print (lista_słów (5, "Król Karol kupił królowej Karolinie korale koloru koralowego"))



