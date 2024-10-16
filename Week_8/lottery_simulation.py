from random import randint

account = 0
count = 0
while True:
    bet=randint(1,10)
    print("You bet on:",bet)
    lucky_draw = randint(1,10)
    print("The result is",lucky_draw)


    if bet == lucky_draw:
        account +=800
    else:
        account -=100
    c = input("Do you want to continue y/n: ").capitalize()
    if c == 'N':
        break

print("Your Amount:",account)