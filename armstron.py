n=int(input("enter a number :"))
l=len(str(n))
arm=0
temp=n  
while temp>0:
    a=temp%10
    arm+=a**l
    temp//=10   
if n==arm:
    print("The number is an armstrong number")
else:
    print("the number is not an armstrong number")