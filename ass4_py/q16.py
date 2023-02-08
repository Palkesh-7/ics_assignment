# Write a Python program to find the second most repeated word in a given string. 
 
def count_repeated_characters(str16):
    dict16 = {}
    str16_list = str16.split()
    print(str16_list)
    for i in str16_list:
        if i not in dict16.keys():
            dict16[i] = 1
        else:
            dict16[i] = dict16[i]+1

    sorted_value = sorted(set(dict16.values()),reverse=True)
    print(sorted_value)
    second_most_repeated_ferq = sorted_value[1]

    for i,k in dict16.items():
        if k == second_most_repeated_ferq:
            print(i," ",k)
        
        

str16 = input("Enter any string :")

count_repeated_characters(str16)