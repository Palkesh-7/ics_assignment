#  Write a Python program to strip a set of characters from a string. 

def strip_characters(str1,ch):
    new_str1=str1.replace(ch,"")
    print(new_str1)



str1 = input("Enter any string :")
ch = input("Enter character That you want to print :")

strip_characters(str1,ch)