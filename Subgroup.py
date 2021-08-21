def Operation(a,b,n):
    return (a+b)%n

def Subgroup(H, e, n):
    for i in range(0,len(H)):
        flag = False
        for j in range(0,len(H)):
            if Operation(H[i],H[j],n) not in H:
                print(H[i],"*",H[j]," not in ", H)
                print(H, "is not a subgroup")
                return False
            if Operation(H[i],H[j],n)==e:
                flag = True
        if flag == False:
            print("No inverse for the element ", H[i])
            print(H, "is not a subgroup")
            return False
    print(H, "is a subgroup")
    return True
Subgroup([0,2,4,6,8],0,10)