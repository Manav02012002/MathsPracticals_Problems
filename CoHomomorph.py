#20PCM53 Manav Madan Rawal
n = 12
G = set(range(0,n))
H = {0,4,8}
F = []
for i in G:
    C = {(i+j)%n for j in H}
    if C not in F: 
        F.append(C)
print("The Cosets are: ", F)