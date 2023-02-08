# 33.	Write a Python program to set the indentation of the first line.  

import textwrap
  
str33 = 'hello\n\n \nworld'
str331 = textwrap.indent(text=str33, prefix='   ')

print(str331)
  