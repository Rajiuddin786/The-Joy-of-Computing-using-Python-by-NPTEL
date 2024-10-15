from PIL import Image
from random import randint

end=100

def show_board():
    img=Image.open('xyz.jpg')
    img.show()

def check_ladder_or_snake(cell_no):
    if cell_no == 8:
        print('Ladder')
        return 26
    elif cell_no == 21:
        print('Ladder')
        return 82
    elif cell_no == 43:
        print('Ladder')
        return 77
    elif cell_no == 50:
        print('Ladder')
        return 91
    elif cell_no == 54:
        print('Ladder')
        return 93
    elif cell_no == 62:
        print('Ladder')
        return 96
    elif cell_no == 66:
        print('Ladder')
        return 87
    elif cell_no == 80:
        print('Ladder')
        return 100
    elif cell_no == 44:
        print('Snake')
        return 22
    elif cell_no == 46:
        print('Snake')
        return 5
    elif cell_no == 48:
        print('Snake')
        return 9
    elif cell_no == 52:
        print('Snake')
        return 11
    elif cell_no == 55:
        print('Snake')
        return 7
    elif cell_no == 59:
        print('Snake')
        return 17
    elif cell_no == 64:
        print('Snake')
        return 36
    elif cell_no == 69:
        print('Snake')
        return 33
    elif cell_no == 73:
        print('Snake')
        return 1
    elif cell_no == 83:
        print('Snake')
        return 19
    elif cell_no == 92:
        print('Snake')
        return 51
    elif cell_no == 95:
        print('Snake')
        return 24
    elif cell_no == 98:
        print('Snake')
        return 28
    else:
        return cell_no

def play():
    #show_board()
    #Input player name
    c1,c2=-1,-1
    p1_name = input("Enter your name Player 1: ")
    p2_name = input("Enter your name Player 2: ")

    #Score
    p1_point = 0
    p2_point = 0

    turn = 0

    while True:
        #Player 1 turn
        if turn == 0:
            print(p1_name,"Your Turn")

            c1= input('Do you want to Continue y/n: ')
            dice = randint(1,6) #Our Dice
            print('Dice=',dice)
            p1_point += dice
            #Move p1_point
            p1_point = check_ladder_or_snake(p1_point) #Check for ladder or Snake

            if p1_point > end:
                p1_point = end
            
            print(p1_name,'Your Score:',p1_point)
            if end == p1_point: #Check for Winning 
                print(p1_name,"has Won")
                break
            turn = 1
        else:
            print(p2_name,"Your Turn")

            c2= input('Do you want to Continue y/n: ')
            dice = randint(1,6) #Our Dice
            print('Dice=',dice)
            p2_point += dice
            #Move p2_point
            p2_point = check_ladder_or_snake(p2_point) #Check for ladder or Snake

            if p2_point > end:
                p2_point = end
            
            print(p2_name,'Your Score:',p2_point)
            if end==p2_point:#Check for Winning
                print(p2_name,"has Won")
                break
            turn = 0
        if (c1 == 'n' or c2 == 'n') and turn == 0:
            break



if __name__ == "__main__":
    play()