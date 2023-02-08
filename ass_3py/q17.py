# 17.	Write a Python script that takes input from the user and displays that input back in 
# upper and lower cases
def display_string_in_upper_and_lower(str17):
    upper_case = str17.upper()
    lower_case = str17.lower()
    print("Upper case string : ",upper_case)
    print("lower case string : ",lower_case)

str17  = input("Enter any string : ")
display_string_in_upper_and_lower(str17)