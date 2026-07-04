n=int(input("enter a number"))#121
m=n#121
c=0
while n!=0:
        b=n%10#1,2,1
        n//=10#12,1,0
        c=c*10+b#1,12,121
if m==c:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")