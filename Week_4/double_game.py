from string import ascii_letters
from random import randint,choice,randrange

symbols=list(ascii_letters)
card1=[0]*5
card2=[0]*5

pos1=randrange(0,5)
pos2=randrange(0,5)

samesymbol=choice(symbols)
symbols.remove(samesymbol)

if pos1 == pos2:
    card2[pos1] = samesymbol
    card1[pos2] = samesymbol
else:
    card1[pos1] = samesymbol
    card2[pos2] = samesymbol
    card1[pos2] = choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1] = choice(symbols)
    symbols.remove(card2[pos1])

i=0
while(i<5):
    if i!=pos1 and i!=pos2:
        alphabet1=choice(symbols)
        symbols.remove(alphabet1)
        alphabet2=choice(symbols)
        symbols.remove(alphabet2)
        card1[i] = alphabet1
        card2[i] = alphabet2
    i += 1

print(card1)
print(card2)

ch=input("Can you spot the Similar Symbol: ")
if ch == samesymbol:
    print("Correct :)")
else:
    print("Wrong :(")