n=int(input("enter a number: "))
s=0
while n>0:
    r=n%10
    if r>s:
        s=r
    n//=10
print("largest digit is:",s) 
            
    
