# 7 Write a function to create CSV file with content.

import pandas as pd

def creating_CSV():
    name = ["aparna", "pankaj", "sudhir", "Geeku"]
    deg = ["MBA", "BCA", "M.Tech", "MBA"]
    scr = [90, 40, 80, 98]
    
    dict = {'name': name, 'degree': deg, 'score': scr}
        
    df = pd.DataFrame(dict)
    df.to_csv('file_csv.csv')

if __name__=="__main__":
    creating_CSV()