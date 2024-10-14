import random
def bubble_sort(mylist):
    l = len(mylist)

    for i in range(l):
        for j in range(0,l-i-1):
            if mylist[j] > mylist[j+1]:
                temp = mylist[j]
                mylist[j]=mylist[j+1]
                mylist[j+1]=temp
    print(mylist)

def main():
    n = int(input("Enter the Size: "))
    arr = [random.randint(0,500) for _ in range(n)]
    print("Before Sorting")
    print(arr)
    print("After Sorting")
    bubble_sort(arr)

if __name__ == "__main__":
    main()