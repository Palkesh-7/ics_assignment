import pandas as pd

def create_dataframes(n):
    dataframes = []
    for i in range(n):
        df = pd.DataFrame({'col1': [i, i+1, i+2], 'col2': [i**2, (i+1)**2, (i+2)**2]})
        dataframes.append(df)
    return dataframes

if __name__ == '__main__':
    n = 5
    dataframes = create_dataframes(n)
    print(dataframes[1])
    for i, df in enumerate(dataframes):
        print(f"DataFrame {i}:")
        print(df)