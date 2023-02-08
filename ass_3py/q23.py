# 23.	Write a Python program to get the last part of a string before a specified character 

def last_part_of_string(str23,specified_chr):
    str23_list = str23.split(specified_chr)
    print(str23_list[-2])

specified_chr  = "."

str23 = "www.google.com"

last_part_of_string(str23,specified_chr)