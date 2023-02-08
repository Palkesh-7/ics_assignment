# Write a Python program to count repeated characters in a string. 
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2



def count_repeated_characters(str2):
    dict2 = {}
    for i in str2:
        if i not in dict2.keys():
            dict2[i] = 1
        else:
            dict2[i] = dict2[i]+1
    

    sv = sorted(dict2.items(),key = lambda x:x[1],reverse = True )

    for i in sv:
        if i[1]>1:
            print(i[0]," ",i[1])
        
    

str2 = input("Enter any string :")

count_repeated_characters(str2)