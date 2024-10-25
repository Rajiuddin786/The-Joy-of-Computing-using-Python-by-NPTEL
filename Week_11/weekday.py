import calendar

valid_y=True
valid_m=True
valid_d=True

weekdays=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

while valid_y:
    year=int(input("Enter the year: "))
    if year<1970:
        print("Invalid Input! Must be in range of 1970-2018")
    else:
        valid_y=False
while valid_m:
    month=int(input("Enter the month: "))
    if 0<month<=12:        
        valid_m=False
    else:
        print("Invalid Month!")

while valid_d:
    day=int(input("Enter the day: "))
    if month in [4,6,9,11]:
        if 0<day<=30:
           valid_d=False
        else:
            print("Invalid Day!")
    elif month in [1,3,5,7,8,10,12]:
        if 0<day<=31:
            valid_d=False
        else:
            print("Invalid Day!")
    else:
        if calendar.isleap(year):
            if 0<day<=29:
                valid_d=False
            else:
                print("Invalid Day!")
        else:
            if 0<day<=28:
                valid_d=False
            else:
                print("Invalid Day!")


day_index=calendar.weekday(year,month,day)
weekday=weekdays[day_index]
print(f"The WeekDay of {day}-{month}-{year} is {weekday}")