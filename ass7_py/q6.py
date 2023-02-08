# 6.	Write a function to create a excel sheet file with content.

import pandas as pd

def creating_excel():
    name = ["aparna", "pankaj", "sudhir", "Geeku"]
    deg = ["MBA", "BCA", "M.Tech", "MBA"]
    scr = [90, 40, 80, 98]
    
    dict = {'name': name, 'degree': deg, 'score': scr}
        
    df = pd.DataFrame(dict)
    df.to_excel('file1.xlsx')

if __name__=="__main__":
    creating_excel()