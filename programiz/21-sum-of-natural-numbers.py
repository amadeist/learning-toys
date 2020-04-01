number = int(input("Please enter a number for limit: "))
sum = 0
if number <= 0:
    print("Please enter a number greater than zero")
else:
    while number:
       sum += number
       number -= 1
    print(f"Sum of natural numbers between 0 and {number} = {sum} ")
