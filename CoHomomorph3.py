#20PCM53 Manav Madan Rawal
n = 16
G = set(range(0,n))
H = {0,2,4,6,8,10,12,14}
F = []
for i in G:
    C = {(i+j)%n for j in H}
    if C not in F: 
        F.append(C)
print("The Cosets are: ", F)