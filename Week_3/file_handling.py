
with open('./Files/exfile.txt','r+') as file:
    print(file.read())
    file.write("I am Fine")
file.close()