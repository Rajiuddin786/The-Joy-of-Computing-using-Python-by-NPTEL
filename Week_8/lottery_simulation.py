from random import randint
import matplotlib.pyplot as mlt

account = 0
count = 1
x=[]
y=[]
while count<366:
    x.append(count)
    bet=randint(1,10)
    # print("You bet on:",bet)
    lucky_draw = randint(1,10)
    #print("The result is",lucky_draw)


    if bet == lucky_draw:
        account +=800
    else:
        account -=100
    # c = input("Do you want to continue y/n: ").capitalize()
    # if c == 'N':
    #     break
    y.append(account)
    count+=1

print("Your Amount:",account)
mlt.plot(x,y)
mlt.show()