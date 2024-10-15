import numpy

board = numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s='X'
p2s='O'

def place(symbol):
    print(numpy.matrix(board))
    while True:
        row,col = int(input("Enter the Row: ")),int(input("Enter the Column: "))
        if 0<row<4 and 0<col<4 and board[row-1][col-1] == '-':
            board[row-1][col-1] = symbol
            break
        else:
            print('Wrong Input! Try Again')

def check_row(symbol):
    for r in range(3):
        count=0
        for  c in range(3):
            if board[r][c] == symbol:
                count += 1
        if count == 3:
            print(symbol,"has won")
            return True
    return False

def check_col(symbol):
    for c in range(3):
        count=0
        for  r in range(3):
            if board[r][c] == symbol:
                count += 1
        if count == 3:
            print(symbol,"has won")
            return True
    return False

def check_diagonals(symbol):
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        print(symbol,"has won")
        return True
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        print(symbol,"has won")
        return True
    return False
    

def won(symbol):
    return check_row(symbol) or check_col(symbol) or check_diagonals(symbol)


def play():
    
    for turn in range(9):
        if turn%2 == 0:
            print('X turn')
            place(p1s)
            if won(p1s):
                break
        else:
            print('O turn')
            place(p2s)
            if won(p2s):
                break
    if not(won(p1s)) and not(won(p2s)):
        print("It is a Draw")

if __name__ == "__main__":
    play()