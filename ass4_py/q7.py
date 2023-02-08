# *) Write a Python program to lowercase the first n characters in a string. 
 

def lowercase_first_chaeacter(str7,n):
    lower_str7 = str7[:n].lower()
    
    print(lower_str7+str7[n:])




if __name__ =="__main__":
    str7 = input("Enter any string :")
    n =int(input("Enter number of character you want in lowercase :"))
    lowercase_first_chaeacter(str7,n)