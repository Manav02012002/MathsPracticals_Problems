
def AND (a, b):
 
    if a == 1 and b == 1:
        return True
    else:
        return False

def NAND (a, b):
    if a == 1 and b == 1:
        return False
    else:
        return True
 
def OR(a, b):
    if a == 1 or b ==1:
        return True
    else:
        return False

def XOR (a, b):
    if a != b:
        return True
    else:
        return False

def NOT(a):
    return not a

def NOR(a, b):
    if(a == 0) and (b == 0):
        return True
    elif(a == 0) and (b == 1):
        return False
    elif(a == 1) and (b == 0):
        return False
    elif(a == 1) and (b == 1):
        return False

def XNOR(a,b):
    if(a == b):
        return True
    else:
        return False
        
if __name__=='__main__':
    print("1.AND")
    print("2.NAND")
    print("3.OR")
    print("4.XOR")
    print("5.NOT")
    print("6.NOR")
    print("7.XNOR")
    x = int(input("Enter the gate you want to compute:"))
    if x == 1:
        a = int(input("Enter a:"))
        b = int(input("Enter b:"))
        print(AND(a,b))
    if x == 2:
        a = int(input("Enter a:"))
        b = int(input("Enter b:"))
        print(NAND(a,b))
    if x == 3:
        a = int(input("Enter a:"))
        b = int(input("Enter b:"))
        print(OR(a,b))
    if x == 4:
        a = int(input("Enter a:"))
        b = int(input("Enter b:"))
        print(XOR(a,b))
    if x == 5:
        a = int(input("Enter a:"))
        print(NOT(a))
    if x == 6:
        a = int(input("Enter a:"))
        b = int(input("Enter b:"))
        print(NOR(a,b))
    if x == 7:
        a = int(input("Enter a:"))
        b = int(input("Enter b:"))
        print(XNOR(a,b))      

 
 
