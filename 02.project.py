from math import sqrt
a=float(input("Enter Side 1:"))
b=float(input("Enter Side 2:"))
c=float(input("Enter Side 3:"))
s=float((a+b+c)/2)
x=float(s*(s-a)*(s-b)*(s-c))
print(sqrt(x))