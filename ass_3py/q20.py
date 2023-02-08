# 20.	Write a Python function to insert a string in the middle of a string.  
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}



def insert_sting_middle(tag,string):
    print("{0}{1}{2}".format(tag[:2],string,tag[2:4]))


if __name__ =="__main__":
    insert_sting_middle('[[]]<<>>', 'Python')
    insert_sting_middle("{{}}", 'PHP')
