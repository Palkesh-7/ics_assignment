# 9 Write a function to delete files or directories.

import os 

directory = "My_folder"
  
parent_dir = os.getcwd()
  
path = os.path.join(parent_dir, directory)
  
os.mkdir(path)

os.chdir(path)

with open("demofile.txt","w") as f:
    f.write("delete files")

if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
  print("file deleted ")
else:
  print("The file does not exist")

os.chdir(parent_dir)
os.rmdir("My_folder")
print("Print folder deleted ")
