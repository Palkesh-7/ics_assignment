# 3.	Write a program to accept 10 different strings and convert it into dictionary and print it.
user_dict = {}
for i in range(1,11):
  print("Enter",i, "string")
  user_dict[i] = input()

print(user_dict)