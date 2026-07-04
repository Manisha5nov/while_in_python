n=int(input("enter a number: "))
s=9
while n>0:
    r=n%10
    if r<s:
        s=r
    n//=10
print("smallest digit is:",s)