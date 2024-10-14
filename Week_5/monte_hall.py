from random import randint,choice

doors = ["0"]*3
goat_door = []
swap = 0
no_swap = 0
x = randint(0,2)
doors[x] = "BMW"

for i in range(3):
    if i == x:
        continue
    else:
        doors[i] = "goat"
        goat_door.append(i)

player_choice = int(input("Enter your Choice: "))
door_open = choice(goat_door)
while door_open == player_choice:
    door_open = choice(goat_door)

swap_choice = input("Do you Want to Swap Y/N: ").capitalize()


if swap_choice == "Y":
    if(doors[player_choice] == 'goat'):
        print("Player Wins")
        swap += 1
    else:
        print("Player Lost")
else:
    if(doors[player_choice] == 'goat'):
        print("Player Lost")
    else:
        print("Player Won")
        no_swap += 1
    
print("Swap=",swap,"\nNo Swap=",no_swap)