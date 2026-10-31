n=int(input("enter a number :"))
mul=1
while n>0:
    a=n%10
    mul*=a
    n//=10
print("The product of the digits is : ",mul)
