# Write a Python program to check whether a string contains all letters of the alphabet. 

def alphabet(str5):
    check = "abcdefghijklmnopqrstuvwxyz"
    check_point = 1
    for j in check:
        if j not in str5:
            check_point = 0
            print("Your string not is not have all Characters ")
            break
    
    if check_point == 1:
        print("Your string having all characters : ")
        

if __name__ =="__main__":

    str5 = input("Enter any string :")

    str5 = str5.replace(" ","")

    alphabet(str5)
