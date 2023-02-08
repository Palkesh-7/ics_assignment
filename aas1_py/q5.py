n = int(input("Enter Number of line : "))

if n > 0:
    for i in range(0,n+1):
        print(" "*i+" *"*(n-i))

else:
    print("Incorrect Input")