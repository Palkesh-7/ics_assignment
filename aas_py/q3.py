n = int(input("Enter Number of line : "))

if n > 0:
    for i in range(1,n+1):
        print("*"*(n-i+1))
else:
    print("Incorrect Input")