x=int(input("Enter start of range:"))
y=int(input("Enter end of range:"))
print("Super Special Numbers between", x, "and", y)
for h in range (x,y):
   n = h
   sum = 0
   while n>0:
      digit=n%10
      prod=1
      for i in range (1,digit+1):
         prod=prod*i
      sum = sum + prod
      n=n//10
      if i == sum:
       print(h)