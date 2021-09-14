#20PCM53 Manav Madan Rawal
def f(x):
    return 5*x
def operation(a,b,n):
    return(a+b)%n
def isHomomorphic(G1,G2):
    m,n = len(G1), len(G2)
    for i in G1:
        for j in G1:
            p = f(operation(i,j,m))%n
            q = operation(f(i)%n, f(j)%n, n)
            if p!=q:
                print("f is not a homomorphism")
                return
    print("f is a homomorphism")
z4 = set(range(0,5))
z8 = set(range(0,10))
isHomomorphic(z4,z8)