n=int(input("enter a number :"))
count=0
while n>0:
    a=n%10
    count+=1
    n//=10
print("number of digits :",count)
