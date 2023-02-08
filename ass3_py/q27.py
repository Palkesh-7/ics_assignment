# 27.Write a Python program to remove a newline in Python.

# str27 = input("Enter any string : ")
def remove_newline(str27):
    s = ''.join(str27.splitlines())
    return s


 
str27 = "\n name \n palkesh \n malviya \n"
print("Original string:", str27)
print("After deleting the new line:", remove_newline(str27))