# 25.	Write a Python function to convert a given string to all uppercase if it
#contains at least 2 uppercase characters in the first 4 characters 

def convert_func(str25):
    count = 0
    for i in str25[:4]:
        if i.isupper():
            count+=1
    if count >= 2:
        print(str25.upper())

    

convert_func("PAlkesh")