from random import randint
import datetime

def birthday_paradox():
    birthday = []

    for i in range(51):
        year = randint(1895,2017)
        leap_year = False
        if year%4 == 0 and year%100 != 0 or year%400 == 0:
            leap_year = True
        month = randint(1,12)
        if month == 2 and leap_year:
            day = randint(1,29)
        elif month == 2:
            day = randint(1,28)
        elif month == 7 or month == 8:
            day = randint(1,31)
        elif month%2 != 0 and month<7:
            day = randint(1,31)
        elif month % 2 == 0 and month>7 and month<12:
            day = randint(1,31)
        else:
            day = randint(1,30)
        dd=datetime.date(year,month,day)
        day_of_year=dd.timetuple().tm_yday
        i += 1
        birthday.append(day_of_year)


    birthday.sort()
    print(birthday)

if __name__ == "__main__":
    birthday_paradox()