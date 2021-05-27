
def AND (a, b):
 
    if a == 1 and b == 1:
        return True
    else:
        return False
 
# Driver code
if __name__=='__main__':
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    print(AND(a, b))