# 1.Write a function to create simple text file with some text content.
txt = '''Write a function to create simple text file with some text content.'''
with open("mytxt_file.txt","w") as f:
    f.write(txt)