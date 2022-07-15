from copy import copy
def GS(A,x,b,dec):
    y=[[copy(x)]]
    n=len(b)
    while True:
        for i in range(n):
            d=b[i]
            for j in range(n):
                if j!=i:
                    d=d-A[i][j]*x[j]
            x[i]=d/A[i][i]
        y.append(copy(x))
        err=[]
        for i in range(n):
            a=round(abs(y[-1][i]-y[-2][i],dec))
            err.append(a)
        z=[0 for i in range(n)]
        if err == z:
            break
    itr = len(y)
    print("The solution after ", itr, "iterations is", x)
x0 = [0,0,0]
A =  [[10,2,1],[2,10,1],[2,2,10]]
b = [12,13,14]
GS(A,x0,b,4)