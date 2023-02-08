# 2.Write a function to read an existing text file and display its contents in terminal

with open("mytxt_file.txt","r") as f:
    print(f.read())
