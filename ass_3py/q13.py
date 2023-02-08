# 13.	Write a Python program to remove the nth index character from a nonempty string.

def function_removing_nth(str13,index_number):
    str13_list = list(str13)
    str13_list.pop(index_number)
    print("".join(str13_list))


str13 = input("Enter your string : ")
index_number = int(input("Enter index number that character you want to remove : "))
function_removing_nth(str13,index_number)