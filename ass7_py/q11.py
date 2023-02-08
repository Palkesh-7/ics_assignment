# 11.Write a function to copy data from one directory to another directory.

import os
import shutil

present_working_dir = os.getcwd()

dir_name1 = "folder_1"
dir_name2 = "folder_2"

path1=os.path.join(present_working_dir,dir_name1)
path2=os.path.join(present_working_dir,dir_name2)


os.mkdir(path1)
os.mkdir(path2)

os.chdir(path1)
with open("folder_1_file.txt","w") as f:
    f.write("first folder")

os.chdir(present_working_dir)
# files = os.listdir(path1)

# print(files)
 
shutil.copy(path1, path2)


