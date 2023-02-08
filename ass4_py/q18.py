# Write a Python program to move spaces to the front of a given string. 


str17 = input("Enter string ")

count_spaces = str17.count(" ")

str17_new = str17.replace(" ","")

print(" "*count_spaces,str17_new)
