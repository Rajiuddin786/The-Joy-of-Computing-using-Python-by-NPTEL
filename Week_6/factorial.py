def fac_recursion(n):
    if n<=0:
        print('Wrong Input')
    else:
        if n == 1:
            return 1
        return n*fac_recursion(n-1)

def fac_normally(n):
    if n<=0:
        print('Wrong Input')
    else:
        f=1
        for i in range(1,n+1):
            f*=i
        return f

n=int(input("Enter a number to find the Factorial: "))
fac_rec=fac_recursion(n)
fac_nor=fac_normally(n)

if fac_rec:
    print("Factorial Recursively=",fac_rec)
if fac_nor:
    print("Factorial Normally=",fac_nor)