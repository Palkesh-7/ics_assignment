# 4.	Write a program to accept 10 different strings and convert it into tuple and print it.

use_list = []
for i in range(1,11):
  print("Enter",i, "string")
  use_list.append(input())
  user_tuple = tuple(use_list)

print(user_tuple)
print(type(user_tuple))
