

def result(choice1,choice2,bit1,bit2):
    p1=int(choice1[bit1])%3
    p2=int(choice2[bit2])%3

    print("Player 1 Choose",player_1[p1],"\nPlayer 2 Choose",player_2[p2])

    if player_1[p1] == player_2[p2]:
        print("Draw")
    elif player_1[p1] == 'Rock' and player_2[p2] == 'Scissor': 
        print("Player 1 Wins!")
    elif player_1[p1] == 'Rock'and player_2[p2] == 'Paper':
        print("Player 2 Wins!")
    elif player_1[p1]  == 'Paper' and player_2[p2] == 'Scissor':
        print('Player 2 Wins!')
    elif player_1[p1] == 'Paper' and player_2[p2] == 'Rock':
        print('Player 1 Wins!')
    elif player_1[p1] == 'Scissor' and player_2[p2] == 'Rock':
        print('Player 2 Wins!')
    elif player_1[p1] == 'Scissor' and player_2[p2] == 'Paper':
        print('Player 1 Wins!')


player_1={0:'Rock',1:'Paper',2:'Scissor'}
player_2={0:'Rock',1:'Paper',2:'Scissor'}

while True:
    choice1=input("Enter your Choice Player 1: ")
    choice2=input("Enter your Choice Player 2: ")
    bit1 = int(input("Player 1,Enter the secret bit position: "))
    bit2 = int(input("Player 2,Enter the secret bit position: "))

    result(choice1,choice2,bit1,bit2)

    ch=input("Do you want conitnue Y/N: ").capitalize()
    if ch == 'N':
        break
    