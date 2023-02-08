# 8.	Write a Python program to get a string from a given string where all occurrences of 
# its first char have been changed to '$', except the first char itself.


string8 = 'restart'

string8_list = list(string8)
check_point = string8_list[0]

for i in range(1,len(string8_list)):
  
  if check_point == string8_list[i]:
    string8_list[i] = "$"

string81 = "".join(string8_list)
print(string81)