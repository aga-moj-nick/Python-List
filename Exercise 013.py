# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.


import pprint
  
def TrzyD(a, b, c):
    lista = [[ ['*' for col in range(a)] for col in range(b)] for row in range(c)]
    return lista
      

col1 = 3
col2 = 4
row = 6

pprint.pprint(TrzyD(col1, col2, row))
