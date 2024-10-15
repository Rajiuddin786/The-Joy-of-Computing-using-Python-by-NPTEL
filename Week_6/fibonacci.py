
def fibo(n):
    if n<2:
        return  n
    else:
        return fibo(n-1) + fibo(n-2)

def main():
    n=int(input("Enter a number: "))
    if n<0:
        print("Wrong Input!")
    else:
        print(f"{n}th fibonacci number=",fibo(n))

if __name__ == "__main__":
    main()