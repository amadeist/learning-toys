Year = int(input("Enter the year that you want to check it is a leap year: "))

#https://www.wikihow.com/Calculate-Leap-Years

if Year % 100 == 0:
    if Year % 400 == 0:
        print("This is a leap year")
    else:
        print("This is not a leap year")
elif Year % 4 == 0 and Year % 100 != 0:
    print("This is a leap year")
