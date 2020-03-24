limit = int(input("Enter a limit for sequence: "))

n1, n2 = 0, 1

for i in range(0,limit):
    print(n1)
    temp = n2
    n2 += n1
    n1 = temp
