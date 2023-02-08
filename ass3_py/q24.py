# 24.Write a Python function to reverse a string if its length is a multiple of 4.

def reverse_string(str24):
    if len(str24)%4 == 0:
        s24 =str24[::-1]
        print(s24)
    else:
        print("String is not multiple of 4 ")

        
str24 = input("Enter string : ")

reverse_string(str24)