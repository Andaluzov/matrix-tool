
def zapoln_matr:
   print('Введите размер матрицы')
   n = input('строк = ')
   n = input('столбцов = ')
   a = []
   a_row = []
   for i in range(n):
      for j in range(m):
         elem = input('number')
         a_row.append(int(elem))
      a.append(a_row)
   return(a)