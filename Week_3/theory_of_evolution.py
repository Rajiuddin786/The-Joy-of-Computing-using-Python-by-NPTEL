from random import randint,randrange
    

with open('./File/dna.txt') as file:
    x=file.read()
    x=list(x)
for _ in range(0,10000):
    ind = randrange(0,len(x))
    p = randint(1,100)
    if p==1:
        if(x[ind] == '0'):
            x[ind] = '1'
        else:
            x[ind] = '0'
print(x)
