n = int(input("Enter Number of line : "))
if n > 0:
    if n%2 != 0:
        n = n//2+1
        for i in range(0,n):
            print(" "*i +" *"*(n-i))

        for i in range(2,n+1):
            print(" "*(n-i)+" *"*i)
    else:
        print("Input must be odd :")
else:
    print("Incorrect Input")


