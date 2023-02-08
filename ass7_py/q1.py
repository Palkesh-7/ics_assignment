# 1.Write a function to create simple text file with some text content.


def creat_text_file(txt):
    with open("mytxt_file.txt","w") as f:
        f.write(txt)

txt = '''Write a function to create simple text file with some text content.'''
creat_text_file(txt)