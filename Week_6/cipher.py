from string import ascii_letters

mydict = {}
data = ""
op_file=open('./Files/op_file.txt','w')
for i in range(len(ascii_letters)):
    mydict[ascii_letters[i]] = ascii_letters[i-1]

with open("./Files/exfile.txt") as file:
    while True:
        c=file.read(1)
        if not c:
            print("End of File")
            break
        if c in mydict:
            data = mydict[c]
        else:
            data=c
        op_file.write(data)
        print(data)

op_file.close()
        