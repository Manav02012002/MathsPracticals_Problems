def NAND (a, b):
    if a == 1 and b == 1:
        return False
    else:
        return True
 
# Driver code
if __name__=='__main__':
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    print(NAND(a, b))