# 11.Write a function to copy data from one directory to another directory.

import os
import shutil

present_working_dir = os.getcwd()

dir_name1 = "folder_1"
dir_name2 = "folder_2"

path1=os.path.join(present_working_dir,dir_name1)
path2=os.path.join(present_working_dir,dir_name2)

try:
    os.mkdir(path1)
except OSError as error:
    pass

try:
    os.mkdir(path2)
except OSError as error:
    pass


os.chdir(path1)
with open("folder_1_file.txt","w") as f:
    f.write("first folder")


os.chdir(path2)
with open("folder_2_file.txt","w") as f:
    pass

os.chdir(present_working_dir)

path1 = os.path.join(path1,"folder_1_file.txt")
path2 = os.path.join(path2,"folder_2_file.txt")

 
shutil.copy(path1,path2) # shutil.copy use for copy data only need create file in destination path aslo.




