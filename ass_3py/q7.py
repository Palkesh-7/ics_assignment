#7.	Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
#If the string length is less than 2, return the empty string instead.

string7 = input("Enter any string :")

if len(string7) > 2:
  print(string7[:2]+ string7[-2:])
elif len(string7) == 2:
  print("Empty String")
