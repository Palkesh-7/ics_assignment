# Write a Python program to find the first repeated word in a given string. 
def repeated_word(str15):
    str15_list = str15.split()
    for i in range(len(str15_list)):
        check_point = 0
        for k in range((i+1),len(str15_list)):
            if str15_list[i] == str15_list[k]:
                check_point = 1
                break
        if check_point:
            print("the first repeating character : ",str15_list[i])
            break


def repated_word_by_dict(str15):
    check_list = []
    str15_list = str15.split()
    for i in range(len(str15_list)):
        if str15_list[i] not in check_list:
            check_list.append(str15_list[i])
        else:
            print("the first repeating character : ",str15_list[i])
            break
    

if __name__ =="__main__":
    str15 = input("Enter your sentance :")
    repeated_word(str15)
    repated_word_by_dict(str15)






