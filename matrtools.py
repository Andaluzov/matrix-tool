def add(A,B):
    Crow=[]
# comment
    for i in range(len(A)):
        ccol=[]
        for j in range(len(A[0])):
            ccol.append(A[i][j]+B[i][j])

        Crow.append(ccol)
    print(Crow)
    return Crow