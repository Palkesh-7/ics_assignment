# 19.	Write a Python function to create an HTML string with tags around the word(s).  
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'



def add_tags(tag,string):
    print("<{0}>{1}</{0}>".format(tag,string))


if __name__ =="__main__":

    add_tags('i', 'Python') 
    add_tags('b', 'Python Tutorial') 