
#  Write a Python program to count and display vowels in text. 

def count_vowel(str9):
    check_list = ['a','e','i','o','u']
    vowels_dict ={}
    for i in check_list:
        vowels_dict[i] = str9.count(i)
    return vowels_dict
 
if __name__ =="__main__":
    str9 = input("Enter any string : ")
    print(count_vowel(str9))