n=int(input("Enter the Order(nxn): "))

def display_matrix(matrix):
    print("Output is:")
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end=' ')
        print()

def magic_square(n:int):
    matrix=[[0 for _ in range(n)] for _ in range(n)]
    
    p,q=int(n/2),int(n-1)
    num = n*n
    count = 1

    while count<= num:
        if p==-1 and q == n:
            p=0
            q=n-2
        else:
            if q == n:
                q = 0
            if p<0:
                p = n - 1
        if matrix[p][q] != 0:
            p += 1
            q -= 2
            continue
        else:
            matrix[p][q] = count
            count += 1
        p -= 1
        q += 1
    display_matrix(matrix)


if __name__ == "__main__":
    magic_square(n)