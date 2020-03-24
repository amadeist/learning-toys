number = int(input("Enter a number: "))

def check_prime(num):
#smallest prime number is 2 so we need to do this control
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

check_prime(number)
