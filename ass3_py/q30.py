# 30.Write a Python program to display formatted text (width=50) as output 


pera = '''30.Write a Python program to display formatted text (width=50) as output Write a Python program to remove existing indentation from all of the lines in a given text '''

for i in range(0,len(pera),50):
    print(pera[i:i+50],end="\n")