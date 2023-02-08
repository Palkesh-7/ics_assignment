# 3.Write a function to add text content to any existing file.
txt = '''Write a function to add text content to any existing file.'''
with open("mytxt_file.txt","a") as f:
    f.write(txt)