# *) Write a Python program to swap commas and dots in a string. 

def swap_commas_and_dots(str8):
    list_str8 = list(str8)
    for i in range(len(list_str8)):
        if list_str8[i] == ",":
            list_str8[i] = "."
        elif list_str8[i] ==".":
            list_str8[i] = ","


    return ("".join(list_str8))



 




if __name__ =="__main__":
    str8 = input("Enter any string : ")
    print(swap_commas_and_dots(str8))