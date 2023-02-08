# 12.	Write a Python function that takes a list of words and return the longest word and the length of 
# the longest one. 

def find_longest_word_in_string():
  max_len = 0
  index_num = 0
  str12 = input("Enter your string : ")
  # str12 = "Longest word: Exercises"
  str12_list = str12.split(" ")
  for i in range(0,len(str12_list)):
    if max_len < len(str12_list[i]):
      max_len = len(str12_list[i])
      index_num = i

  print("Longest word :",str12_list[index_num])
  print("Length of the longest word :",max_len)

find_longest_word_in_string()