n=int(input("enter a number :"))#20

while n>0:#20>0
    c=0
    
    for i in range(2,n):#2,19
        if n%i==0:#20%2==0
            c+=1#1
            break
    if c==0:#1==0
        print(n,end=" ")#20 19 17 13 11 7 5 3
    n-=1#19
