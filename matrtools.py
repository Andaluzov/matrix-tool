def add(a, b):
    c_row=[]
# add of matrix
    for i in range(len(a)):
        c_col=[]
        for j in range(len(a[0])):
            c_col.append(a[i][j]+b[i][j])

        c_row.append(c_col)
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
            sum = 0
            for k in range(p):
                sum = sum+a[i][k]*b[k][j]
            c.append(sum)
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