#  Write a Python program to find the maximum number of characters in a given string. 
 

def count_repeated_characters(str19):
    dict2 = {}
    for i in str19:
        if i not in dict2.keys():
            dict2[i] = 1
        else:
            dict2[i] = dict2[i]+1
    

    sv = sorted(dict2.items(),key = lambda x:x[1],reverse = True )
    check = sv[0][1]
    for i in sv:
        if i[1] == check:

            print(i)

        else:
            break
        
    

str19 = input("Enter any string :")

count_repeated_characters(str19)