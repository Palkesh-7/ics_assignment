# 31. Write a Python program to remove existing indentation from all of the lines in a given text 

prog = '''for i in range(0,10):
                print(i)'''


prog_list = prog.split("\n")

for i in range(len(prog_list)):
    prog_list[i] = prog_list[i].strip()


print("\n".join(prog_list))