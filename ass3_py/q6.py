# 6.	Write a Python program to count the number of characters (character frequency) in a string
frequency = {}
string6 = input("Enter any string :")
for i in string6:
  if i not in frequency.keys():
    frequency[i] = 1
  elif i in frequency.keys():
     frequency[i] = frequency[i]+1

print(frequency)
