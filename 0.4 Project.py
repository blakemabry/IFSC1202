x=int(input("Enter Start of Range:"))
y=int(input("Enter End of Range:"))
print("Prime Numbers Between", x, "and", y)
for num in range(x, y + 1):
    n=(num / 2) + 1
    for i in range(2,num):
        if n % num == 0:

