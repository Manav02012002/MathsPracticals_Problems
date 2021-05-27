def XNOR(a,b):
    if(a == b):
        return True
    else:
        return False
# Driver code
if __name__=='__main__':
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    print(XNOR(a, b))
 