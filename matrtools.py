def add(a, b):
    c_row=[]

# add of matrix
    for i in range(len(a)):
        c_col=[]
        for j in range(len(a[0])):
            c_col.append(a[i][j]+b[i][j])

        c_row.append(c_col)
    return c_row

def add_row(a, b):
    # add of rows of matrix
    c_row=[]
    for i in range(len(a)):
        c_row.append(a[i]+b[i])
    return c_row


def print_matrix(a):
    for i in range(len(a)):
       print(a[i])


def multiply(a,b):
    '''
    # A
    # m x p
    #B
    #p x n

    '''

    matr_c = []
    m = len(a)
    p1 = len(a[0])
    p = len(b)
    n = len(b[0])
    if p != p1:
        raise ValueError('Матрицы должны быть  размера mxp и pxn')
    for i in range(m):
        c = []
        for j in range(n):
            sum_elem = 0
            for k in range(p):
                sum_elem = sum_elem+a[i][k]*b[k][j]
            c.append(sum_elem)
        matr_c.append(c)

    return matr_c

def transpose(a):
    ''''
    Transponirovanie
    '''
    n = len(a)
    m = len(a[0])
    a_transp = []
    for j in range(m):
        c = []
        for i in range(n):
            c.append(a[i][j])
        a_transp.append(c)

    return(a_transp)

def trace(a):
    '''
     след квадратной матрицы (сумму элементов на главной диагонали)
    :param a:
    :return:
    '''
    n = len(a)
    m = len(a[0])
    if n != m:
        raise ValueError('Матрица должна быть  квадратной')
    sum_elem = 0
    for i in range(n):
        sum_elem = sum_elem+a[i][i]

    return(sum_elem)

def zapoln_matr():
    '''
    Заполнение матрицы
    необходимо ввести размеры матрицы nxm
    :return:
    '''
    print('Введите размер матрицы')
    n_row = int(input('строк = '))
    m_col= int(input('столбцов = '))
    a = []
    for i in range(n_row):
        a_row = []
        print('строка',i)
        for j in range(m_col):

            elem_m = int(input('number='))
            a_row.append(elem_m)

        a.append(a_row)

    return(a)

def change_row(a,col1,col2):
    '''
    change of rows col1 and col2  of matrix
    :param a:
    :param col1:
    :param col2:
    :return:
    '''
    n = len(a)
    dop_row=[]
    print(col1,col2)
    dop_row = a[col1]
    a[col1] = a[col2]
    a[col2] = dop_row
    return a

def div_num(a,number):
    n = len(a)
    matr_rez = []
    for i in range(n):
        matr_rez.append(a[i] / number)
    return matr_rez

def mult_num(a,number):
    n = len(a)
    matr_rez = []
    for i in range(n):
        matr_rez.append(a[i] * number)
    return matr_rez


def echelon_form(a):
    '''
    Metod Gaussa
    :param a:
    :return:
    '''

    n = len(a)
    m = len(a[0])
    row_unz = 0
    col_unz = 0

    j = 0
    while  (j <= m):
        i = 0
        while (a[i][j] == 0)  and (i <= n):
            i+=1
        else:
            row_unz = i
            col_unz = j
            break
        j+=1

    print('rc=', row_unz, col_unz)
    if row_unz != 0:
        a = change_row(a,row_unz,0)
##############

    row_unz = 0
    a[row_unz] = div_num(a[row_unz], a[row_unz][col_unz])
    #############


    i = row_unz+1
    while i <n:
        dop_row = []
        dop_row = mult_num(a[row_unz], -a[i][col_unz])
        a[i] = add_row(a[i],dop_row)

        i += 1


    return a