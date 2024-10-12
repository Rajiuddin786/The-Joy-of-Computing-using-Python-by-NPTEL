#Fizzbuzz Code
num=input("Enter a Maximum Range= ") #Enter the Maximum Range to check if it is Fizz or Buzz or FizzBuzz
num=int(num)

def fizzbuzz(n:int):
    if(n%3==0 or n%5 == 0):
        if(n%3 == 0 and n%5 == 0):
            print(n,"is FizzBuzz")
        elif n%3 == 0:
            print(n,"is Fizz")
        else:
            print(n,"is Buzz")
    else:
        print(n,"is None")

def main():
    for i in range(1,num):
        fizzbuzz(i)

if __name__ == "__main__":
    main()