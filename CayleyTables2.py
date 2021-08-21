def Operation(a,b,n):
    return (a*b)%n

def Cayley(G, n):
    print("The Cayley Table of ",G," is: ")
    for i in range(0,len(G)):
        for j in range(0,len(G)):
            c = Operation(G[i],G[j],n)
            print(c, end="\t")
        print("\n")

Cayley([1,3,7,9,11,13,17,19],20)