from math import*
def p_cal(p,n):
    temp = p 
    for i in range(1,n):
        temp = temp*(p-i)
    return temp
x = [45,50,55,60]
value = 52
p = (value-x[0])/(x[1]-x[0])
n=4
y=[[0 for i in range(n)] for j in range(n)]
y[0][0]=0.7071
y[1][0]=0.766
y[2][0]=0.8192
y[3][0]=0.866

for i in range(1,n):
    for j in range(n-i):
        y[j][i]=y[j+1][i-1]-y[j][i-1]

for i in range(n):
    print(x[i], end="\t")
    for j in range(n-i):
        print(y[i][j], end="\t")
    print("")

sum = y[0][0]
for i in range(1,n):
    sum+=(p_cal(p,i)*y[0][i]/factorial(i))
print("Value at ",value," is ", round(sum,4))