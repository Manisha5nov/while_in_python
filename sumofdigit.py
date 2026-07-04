n=int(input("enter a number :"))
sum=0
while n>0:
    a=n%10
    sum+=a
    n//=10
print("The sum of the digits is : ",sum)