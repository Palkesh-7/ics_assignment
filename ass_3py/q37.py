# 37.Write a Python program to print the following integers with zeros to the left of the specified width 


def print_star(int38_list,specified_width):
    for i in int38_list:
        print("0"*specified_width+str(i),end="\n")



print("Enter number seprated by space : ")
int38_list = list(map(int,(input().split(" "))))
specified_width = int(input("Enter specified width : "))

print_star(int38_list,specified_width)