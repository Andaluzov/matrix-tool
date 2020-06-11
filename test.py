# noinspection PyUnresolvedReferences
import matrtools as mt
import print_matrix as pri
a = [
  [1, 2],
  [3, 4],
  [5, 6]
]
b = [
  [0, 2],
  [1, 0],
  [4, 7]
]
#pri.print_matrix(a)
mt.add(a, b)
print(mt.add(a, b))
pri.print_matrix(mt.add(a, b))
# Тест2

a = [
  [0, 2, 9],
  [-5, 1, 1]
]
b = [
  [0, 2, 0],
  [1, 0, 3]
]
mt.add(a,b)
