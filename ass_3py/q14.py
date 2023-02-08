# 14.	Write a Python program to change a given string to a newly string 
# where the first and last chars have been exchanged.
def exxhange_character(str14):
    new_str14 = str14[-1] + str14[1:-1]+str14[0]
    print(new_str14)
str14 = input("Enter your string : ")
exxhange_character(str14)