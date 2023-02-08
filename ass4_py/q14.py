# *) Write a Python program to find the first repeated character in a given string 
# where the index of the first occurrence is smallest. 

def first_repeting_chracter(str14):
    for i in range(len(str14)):
        check_point = 0
        for k in range((i+1),len(str14)):
            if str14[i] == str14[k]:
                check_point = 1
                break
        if check_point:
            print("the first repeating character : ",str14[i])
            break

if __name__ =="__main__":
    str14 = input("Enter any string : ")
    first_repeting_chracter(str14)
