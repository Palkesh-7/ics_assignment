# 13.Write a function to display content of directory.
import os

path = os.getcwd()


files = os.listdir(path)

for i in files:
    print(i)