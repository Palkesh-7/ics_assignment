# Write a Python program to convert a given string into a list of words. 
# Sample Output:
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']

def convert_string_into_list(str6):
    x = str6.split()
    print(x)

if __name__ == "__main__":

    str6 = input("Enter any string :")
    convert_string_into_list(str6)