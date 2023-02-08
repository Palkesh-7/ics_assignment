# 40.	Write a Python program to format a number with a percentage.

input40_list = []
dict40 ={}
for i in range(0,10):
    input40 = int(input("Enter any number 10 number  :"))
    input40_list.append(input40)

print(input40_list)
list_sum = sum(input40_list)

for i in input40_list:
    per  = ((i/list_sum)*100)
    print("number : ",i,end="")
    print("There percentage : %.2f"%per)