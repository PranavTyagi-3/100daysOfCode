n=int(input("Enter a number: "))
temp=n
s=0
while n>0:
    a=n%10
    s=s+(a*a*a)
    n=n//10

if s==temp:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")
