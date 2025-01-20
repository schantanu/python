import pandas as pd

def print_list(my_list):
    print(my_list)

def print_dataframe():
    data = {"name": ["John", "James", "Jim"], "age": [20, 25, 30]}
    df = pd.DataFrame(data)
    print(df)