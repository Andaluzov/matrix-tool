# noinspection PyUnresolvedReferences
'''
test program
'''
import matrtools as mt
print(' Метод Гаусса')
matr_a = [[0,2,3], [2,4,6]]
#matr_a = mt.zapoln_matr()
mt.print_matrix(matr_a)
print('test1')


a_gauss = mt.echelon_form(matr_a)
mt.print_matrix(a_gauss)





