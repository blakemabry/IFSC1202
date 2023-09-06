x=float(input("Enter First Number:"))
y=input("Enter Operator (+,-.*,/):")
z=float(input("Enter Second Number:"))
if y =='+':
    result = x+z
    print(x,y,z,"=",result)
elif y =='-':
    result = x-z
    print(x,y,z,"=",result)
elif y =='*':
    result = x*z
    print(x,y,z,"=",result)
elif y =='/':
    result = x/z
    print(x,y,z,"=",result)
else:
    print("Invalid Operator")