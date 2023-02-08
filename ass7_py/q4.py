# 4.	Write a function to read excel sheet file and display data on terminal.

import pandas as pd
 
dataframe1 = pd.read_excel('height.xlsx')
 
print(dataframe1)