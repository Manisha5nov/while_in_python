n=int(input("Enter a number: "))
while n > 0:
    b = n % 10
    if b % 2 == 0:
        print(b, "is even")
    else:
        print(b, "is odd")
    n = n // 10