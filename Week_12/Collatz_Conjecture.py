def collatz_conjecture(n,count=0):
    count+=1
    if n==1:
        return count
    elif n&1:
        return collatz_conjecture(3*n+1,count)
    else:
        return collatz_conjecture(n//2,count)
    
n=input("Enter a number: ")
print(collatz_conjecture(int(n)))