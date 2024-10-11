c=input("Enter the cost= ")
c_int=int(c)
d=input("Enter the discount= ")
d_int=int(d)

amount = c_int*(1-(d_int/100))
print("Your total Amount=",amount)