# 2.	Write a program to accept 10 different strings and convert it into list and print it.
def list_forming_function():
  user_list = []
  for i in range(1,11):
    print("Enter",i, "string")
    user_list.append(input())

  print(user_list)

list_forming_function()