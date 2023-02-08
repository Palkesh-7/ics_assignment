#9.	Write a Python program to get a single string from two given strings, separated by a space and swap 
# the first two characters of each string.
txt = "xyz"
txt1 ="abc"
x = txt.replace(txt[:2], txt1[:2])
y = txt1.replace(txt1[:2],txt[:2])
print(y+" "+x)