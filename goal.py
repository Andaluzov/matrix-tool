# noinspection PyUnresolvedReferences
import matrtools as mt
print('сложение матриц')
matr_a = [[1, 2],[3, 4],[5, 6]]
matr_b = [[0, 2],[1, 0],[4, 7]]

rez_matr = mt.add(matr_a, matr_b)
mt.print_matrix(rez_matr)

#2
print('умножение матриц')
matr_a  = [ [1, 2, 1], [3, 4, 5]]
matr_b = [ [0, 2], [1, 0], [1, 5]]

rez_matr = mt.multiply(matr_a, matr_b)
print('multiply of matrix AxB')
mt.print_matrix(rez_matr)
rez_matr = mt.multiply(matr_b, matr_a)
print('multiply of matrix BxA')
mt.print_matrix(rez_matr)

#3
print('Транспонирование матриц')
matr_a = [
 [1, 0],
 [4, 1]
]
print('1')
a_transp = mt.transpose(matr_a)
mt.print_matrix(a_transp)
matr_a = [
 [1, 2],
 [3, 4],
 [5, 6]
]
print('2')
a_transp = mt.transpose(matr_a)
mt.print_matrix(a_transp)

matr_a = [
 [1, 2],
 [3, 4],
 [5, 6]
]
print('3')
matr_b= mt.transpose(mt.transpose(matr_a))
mt.print_matrix(matr_b)