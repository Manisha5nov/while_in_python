n=int(input("enter a number: "))
r=0
while n>0:
    rev=n%10
    r=r*10+rev
    n//=10
    print(r)
    
