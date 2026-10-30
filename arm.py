n=int(input("enter a number :"))
count=0
temp=n 
arm=0
while n>0:
    n=n//10
    count+=1
   
while temp>0:
    a=temp%10
    arm+=a**count
    temp//=10   
if arm==n:
    print("The number is an armstrong number")
else:
    print("the number is not an armstrong number")
    
