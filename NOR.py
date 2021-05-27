def NOR(a, b):
    if(a == 0) and (b == 0):
        return True
    elif(a == 0) and (b == 1):
        return False
    elif(a == 1) and (b == 0):
        return False
    elif(a == 1) and (b == 1):
        return False

if __name__=='__main__':
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    print(NOR(a, b))
 