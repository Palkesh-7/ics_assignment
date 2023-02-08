def input_from_user():
    print("Enter the range in which you want to print Multiplication table")

    lower_limit = int(input("Enter Lower limit : "))
    upper_limit = int(input("Enter Upper limit : "))
    return lower_limit,upper_limit


def multiplication_table(lower_limit,upper_limit):
    for i in range(lower_limit,upper_limit+1):
        print("|",end="")
        for j in range(1,11):
            print("\t",i*j,end ="")
        print("  |")
    

def multiplication_table2(lower_limit,upper_limit):
    for i in range(1,11):
        for j in range(lower_limit,upper_limit+1):
            print("\t",i*j,end ="")
        print()
    
    

if __name__ == "__main__":
    lower_limit,upper_limit = input_from_user()
    multiplication_table2(lower_limit,upper_limit)