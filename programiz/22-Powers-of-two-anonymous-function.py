LastNum = int(input("Enter a number: "))

list_ = map(lambda x: 2**x,range(LastNum))

for i in list_:
    print(i)
