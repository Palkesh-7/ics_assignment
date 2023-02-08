# 36.	Write a Python program to print the following positive and negative numbers with no decimal places 


in36 = float(input("Enter any float number :"))
x = int(in36)
print(x)

# Second way 
print(int(round(in36, 0)))