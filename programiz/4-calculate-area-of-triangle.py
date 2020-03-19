side_1 = int(input("Triangle side 1: "))
side_2 = int(input("Triangle side 2: "))
side_3 = int(input("Triangle side 3: "))

#half the length of the triangle
s = (side_1 + side_2 + side_3) / 2

#formula of area of triangle
area =(s*(s-side_1)*(s-side_2)*(s-side_3)) ** 0.5

print("Area of triangle: %.2f" %area)
