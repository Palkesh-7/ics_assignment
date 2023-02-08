# 21.	Write a Python function to get a string made of 4 copies of the last two characters of a
# specified string (length must be at least 2).  
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses


def insert_end(str21):
    print(str21[-2:]*4)


if __name__ =="__main__":
    insert_end('Python')
    insert_end('Exercises')