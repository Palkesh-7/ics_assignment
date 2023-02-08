# 16.Write a Python program to count the occurrences of each word in a given sentence.
def count_each_word(sentence):
    count_dict = {}
    sentence_list = sentence.split(" ")
    for i in sentence_list:
        if i not in count_dict.keys():
            count_dict[i] = sentence_list.count(i)
    print(count_dict)


sentence = input("Enter your sentance : ")

count_each_word(sentence)