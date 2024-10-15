def fac(n):
    if n==0:
        return f'Wrong Input'
    if n == 1:
        return 1
    return n*fac(n-1)

n=int(input("Enter a number to find the Factorial: "))
print(fac(n))