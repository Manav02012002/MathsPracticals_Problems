def OR(a, b):
    if a == 1 or b ==1:
        return True
    else:
        return False
 
if __name__=='__main__':
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    print(OR(a, b))
 