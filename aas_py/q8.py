n = int(input("Enter any Number of line that must be positive integer : "))

if n > 0:
    if n%2 != 0:
        n = n//2+1
        for i in range(1,n+1):
            print(" "*(n-i),end=(""))
            print("*"*i)

        for i in range(2,n+1):
            print(" "*(i-1),end=(""))

            print("*"*(n-i+1))

    else:
        print("Incorrect Input")
else:
    print("Incorrect Input")