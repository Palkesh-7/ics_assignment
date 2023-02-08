# 10.	Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing', add 'ly' instead. 
# If the string length of the given string is less than 3, leave it unchanged.


def string_check_function():
  string9 = input("Enter any string : ")
  if len(string9) >3:
    if string9[-3:] == "ing":
      list9 = list(string9)
      list91 = list9[:-3]+['l','y']
      print("".join(list91))

    else:
      list9 = list(string9)
      list91 = list9+['i','n','g']
      print("".join(list91))

string_check_function()


