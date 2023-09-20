x=int(input("Enter Start of Range:"))
y=int(input("Enter End of Range:"))
print("Prime Numbers Between", x, "and", y)
for i in range(x, y + 1):
    num=0
    for j in range(2,(i//2 +1)):
        if (i%j==0):
            num=1
            break
    if (num==0):
        print(i)