# *) Write a Python program to find the first non-repeating character in a given string. 
def non_repeting_chracter(str11):
    for i in range(len(str11)):
        check_point = 1
        for k in range((i+1),len(str11)):
            if str11[i] == str11[k]:
                check_point = 0
                break
        if check_point:
            print("the first non-repeating character : ",str11[i])
            break

if __name__ =="__main__":
    str11 = input("Enter any string : ")
    non_repeting_chracter(str11)
