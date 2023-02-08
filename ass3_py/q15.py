# 15.	Write a Python program to remove characters that have 
# odd index values in a given string.

def remove_odd_index_value(str15):
    new_str15 = ""
    for i in range(0,len(str15),2):
        new_str15 = new_str15 + str15[i]
    print(new_str15)

str15 = input("Enter any string :")
remove_odd_index_value(str15)
