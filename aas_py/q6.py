n = int(input("Enter any Number of line that must be positive integer : "))

if n > 0:
    if n%2 != 0:
        n = n//2+1
        for i in range(1,n+1):
            print(" "*(n-i)+"* "*i)

        for i in range(1,n+1):
            print(" "*i+"* "*(n-i))
    else:
        print("Enter any odd positive integer ")
    

else:
    print("Incorrect Input")