# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Sample List : ['abc', 'xyz', 'aba', '1221']


def zliczanie_słów(słowa):
  ctr = 0

  for słowo in słowa:
    if len(słowo) > 1 and słowo[0] == słowo[-1]:
      ctr += 1
  return ctr

print(zliczanie_słów(['abc', 'xyz', 'aba', '1221']))
