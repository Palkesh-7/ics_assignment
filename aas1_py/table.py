def input_function():
    print("Enter the range of number : ")
    l = int(input("Enter Lower limit : "))
    u = int(input("Enter Upper limit : "))
    return l,u


def table_function(l,u):
    for t in range(l,u+1):
        print(t," Multiplication table")
        for i in range(1,11):
            print(t," x ",i," = ",i*t)


if __name__ == "__main__":
    l,u = input_function()
    table_function(l,u)
    