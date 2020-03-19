import math
num = float(input("Please enter a number: "))
try:
    print(math.sqrt(num))
except ValueError:
    print("Please enter a positive number")
except:
    print("Something went wrong!!!")


