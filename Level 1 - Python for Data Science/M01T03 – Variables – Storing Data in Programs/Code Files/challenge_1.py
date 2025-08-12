import math

a = int(input("Please enter a value for first side of triangle:"))
b = int(input("Please enter a value for second side of triangle:"))
c = int(input("Please enter a value for third side of triangle:"))

s = a+b+c
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(f" The area of the triangle: {area}")