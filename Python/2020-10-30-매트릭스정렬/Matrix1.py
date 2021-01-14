def matrixMult(A):
    row=len(A)
    col=len(A[0])    
    
    B = [[0 for row in range(row)]for col in range(col)]
    
    for i in range(row):
        for j in range(col):
            B[j][i]=A[i][j]
    return B
 
           
A = [[3,15,-27,-24],[1,7,5,4],[-2,-11,7,18]]
print(matrixMult(A))