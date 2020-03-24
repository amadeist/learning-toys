num1 = int(input("Enter a small number for interval: "))
num2 = int(input("Enter a large number for interval: "))

for i in range(num1,num2):
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                print(f"{i} is not prime number")
                break
        else:
            print(f"{i} is prime number")
    else:
        print(f"{i} is not prime number")

