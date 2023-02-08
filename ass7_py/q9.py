# 9 Write a function to delete files or directories.

import os 
parent_dir = os.getcwd()
def creating_folder_file():
  directory = "My_folder"
  path = os.path.join(parent_dir, directory)
  os.mkdir(path)
  os.chdir(path)
  with open("demofile.txt","w") as f:
      f.write("New files")


def delete_file():
  if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
    print("file deleted ")
  else:
    print("The file does not exist")
  os.chdir(parent_dir)
  os.rmdir("My_folder")
  print("Print folder deleted ")

if __name__ =="__main__":
  creating_folder_file()
  delete_file()
