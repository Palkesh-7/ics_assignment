# 22.	Write a Python function to get a string made of the first three characters of a specified string. 
# If the length of the string is less than 3, return the original string.  
# Sample function and result :
# first_three('ipy') -> ipy
# first_three('python') -> pyt


def first_three(str22):
    print(str22[:3])


if __name__ == "__main__":
    first_three('ip') 
    first_three('python') 