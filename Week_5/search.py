
def linear_search(arr,num):
    flag=0
    for i,a in enumerate(arr):
        if a == num:
            print(num,"Found in position",(i+1))
            flag = 1
            break
    if flag == 0:
        print(num,"Not Found")

def binary_search(arr,num):
    flag = 0
    arr.sort()
    print(arr)
    l,r = 0,len(arr)-1
    while l<r:
        mid = l+(r-l)//2
        if arr[mid] == num:
            print(num,"Found")
            flag = 1
            break
        elif num > arr[mid]:
            l=mid+1
        else:
            r=mid-1
    if flag == 0:
        print(num,"Not Found")



def main():
    n=int(input("Enter the Size: "))
    arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
    num = int(input("Enter the Element to be Searched: "))
    #linear_search(arr,num)
    binary_search(arr,num)

if __name__  == "__main__":
    main()