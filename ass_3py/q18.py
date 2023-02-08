# 18.	Write a Python program that accepts a comma-separated sequence of words as 
# input and prints the distinct words in sorted form (alphanumerically). 

# Sample Words : red, white, black, red, green, black
# Expected Result : black,black,green,red,red,white

def word_sorted_function(words):
    words_list = words.split(",")
    words_list.sort()
    print("Sorted words are : ")
    for i in range(len(words_list)):
        if i < len(words_list)-1:
            print(words_list[i],end=", ")
        else:
            print(words_list[i],end="")

words = input("Enter comma-separated words :")
word_sorted_function(words)