# LCM = least common multiple

def find_lcm(num1,num2):
    lcm = 0
    if num1 > num2:
        greater = num1
    else:
        greater = num2
    while True:
        if (greater % num1 == 0) and (greater % num2 == 0):
            lcm = greater
            break
        greater += 1
    print(lcm)

num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))

find_lcm(num1,num2)


