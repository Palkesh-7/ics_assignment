# 38.Write a Python program to print the following integers with '*' to the right of the specified width 


def print_star(int38_list,specified_width):
    for i in int38_list:
        print(i," "*specified_width,"*"," "*specified_width,end="")



print("Enter number seprated by space : ")
int38_list = list(map(int,(input().split(" "))))
specified_width = int(input("Enter specified width : "))

print_star(int38_list,specified_width)