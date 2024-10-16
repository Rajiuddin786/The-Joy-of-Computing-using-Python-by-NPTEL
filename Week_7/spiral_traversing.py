#Spiral Matrix

def spiral(m,n,a):
    k,l = 0,0

    """
    k = index of staring row
    l = index of stating column
    """

    while(k<m and l<n):

        #from left to right
        for i in range(l,n):
            print(a[k][i],end=" ")
        
        k += 1
        #from top to bottom
        for i in range(k,m):
            print(a[i][n-1],end=" ")

        n -= 1
        #from right to left
        if(k<m):
            for i in range(n-1,l-1,-1):
                print(a[m-1][i],end=" ")
            m -= 1
        #from bottom to top
        if l<n:
            for i in range(m-1,k-1,-1):
                print(a[i][l],end=" ")
            l+=1

m,n = int(input("Enter row= ")),int(input("Enter col= "))
a = [[int(input(f"Enter the Element A[{i+1}][{j+1}]: ")) for j in range(n)] for i in range(m)]
spiral(m,n,a)