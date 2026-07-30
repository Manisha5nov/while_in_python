# Keep taking numbers until the user enters 0, then print the sum.
total = 0
while True:
    n = int(input("Enter a number (0 to stop): "))
    if n == 0:
        break
    total += n
print("The sum of the numbers is:", total)