import math

def input_from_user():
    print("Enter the range in which you want to print Natural Number table")

    n = input("Enter any Number")
    l = len(n)
    n = int(n)
    return n

def print_Number2(n):
        for i in range(n+1):
            print("\t",i,end="")
            if i%10 == 0:
                print()
                if i%100 == 0:
                    print()

            




def print_Number(n):
    number_of_table = int(math.ceil((n/100)))
    for t in range(0,number_of_table):
        for i in range(1,11):
            count = i + t*(100)
            for j in range(1,11):
                print("\t",count,end="")
                
                if count == n:
                    break
                count+=10
            print()
            if count == n+10:
                    break
        print()
        if count == n+100:
                    break
        # count+=100
    


if __name__ =="__main__":
    n = input_from_user()
    print_Number2(n)




