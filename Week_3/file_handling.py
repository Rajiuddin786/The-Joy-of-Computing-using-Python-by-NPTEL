
with open('./Files/exfile.txt','r+') as file:
    print(file.read())
    file.write("\nI am Fine")
file.close()