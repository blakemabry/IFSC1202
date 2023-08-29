x=int(input("Enter length of time in days:"))
years=x//365
print("years:",years)
weeks=(x%365//7)
print("weeks:",weeks)
days=int(x%365%7)
print("days:",days)