# 11.	Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. 
# If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. 

def string_replace_function(str_11):
    p1 = str_11.index("not")
    p2 = str_11.index('poor!')
    new_str= str_11[p1:(p2+len("poor!"))]
    if ('not' and 'poor' in str_11):
        print(str_11.replace(new_str,'good!'))
    else:
        print(str_11)


str_11 = input("Enter any string : ")
# str_11 = 'The lyrics is not that poor!'
string_replace_function(str_11)