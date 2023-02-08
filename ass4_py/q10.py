# *) Write a Python program to split a string on the last occurrence of the delimiter. 
def last_occurance_of_delimiter(str10,delimiter):
    for i in range((len(str10)-1),0,-1):
        if str10[i] == delimiter:
            print("Your splited string :",str10[:i],str10[i+1:])
            break


if __name__ =="__main__":
    str10 = input("Enter any string : ")
    delimiter = input("Enter delimiter :")
    last_occurance_of_delimiter(str10,delimiter)

