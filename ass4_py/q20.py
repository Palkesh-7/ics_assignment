# Write a Python program to capitalize the first and last letters of each word in a given string.

def capitalize_first_and_last_letters(str20_list):
    for str20 in str20_list:
        s1 = str20[0].upper()
        s2 = str20[-1].upper()
        k = len(str20)-2

        print(s1+str20[1:-1]+s2,end=" ")



if __name__ =="__main__":
    str20 = input("Enter any string : ")
    str20_list =  str20.split()
    capitalize_first_and_last_letters(str20_list)
