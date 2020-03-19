import cmath

a = int(input("Enter x's exponent: "))
b = int(input("Enter y's factor: "))
c = int(input("Enter constant: "))

# calculate the discriminant
delta = (b**2) - (4*a*c)
if delta < 0:
    print("There is no real root")
# find two solutions
sol1 = (-b-cmath.sqrt(delta))/(2*a)
sol2 = (-b+cmath.sqrt(delta))/(2*a)

print(f'The solution are {sol1} and {sol2}')
