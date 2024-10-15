#Binary Search Using Recursion


def binary_search(arr,ele,l,r):
    if l<r:
        mid=l+(r-l)//2

        if arr[mid] == ele:
            return mid
        elif arr[mid] > ele:
            binary_search(arr,ele,l,mid-1)
        else:
            binary_search(arr,ele,mid+1,r)



def main():
    n=int(input("Enter the Array Size: "))
    print("Enter the Array in Sorted Order")
    arr = [int(input(f"Enter the Element {i+1}: ")) for i in range(n)]
    ele = int(input("Enter the Element to be Searched: "))
    found = binary_search(arr,ele,0,len(arr)-1)

    if found:
        print(ele,"Found is pos:",found+1)
    else:
        print("Not Found")

if __name__ == "__main__":
    main()