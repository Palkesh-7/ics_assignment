# *) Write a Python program to print all permutations with a given repetition number of 
# characters of a given string. 


from itertools import product
def permutation_of_string(str12):
    permutaion_list = list(product(str12, repeat = repetition))
    for i in permutaion_list:
        print("".join(i))


if __name__ =="__main__":
    str12 = input("Enter any string : ")
    repetition = int(input("Enter "))
    permutation_of_string(str12,repetition)


