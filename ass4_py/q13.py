# Write a Python program to find the first repeated character in a given string. 


def first_repeting_chracter(str13):
    for i in range(len(str13)):
        check_point = 0
        for k in range((i+1),len(str13)):
            if str13[i] == str13[k]:
                check_point = 1
                break
        if check_point:
            print("the first repeating character : ",str13[i])
            break

if __name__ =="__main__":
    str13 = input("Enter any string : ")
    first_repeting_chracter(str13)
