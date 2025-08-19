# Pandas is used for data manipulation and analysis
# It provides data structures and functions to work with structured data
import pandas as pd

# creating data 
# two core objects in pandas are Series and DataFrame

# Dataframe is a table-like data structure with rows and columns
# we use pd.dataframe to generate a DataFrame

# Here we used dictionary to create a DataFrame
# {
#     'key': 'value',
#     'key2': 'value2',
# }

# Key are column names and values are the data in those columns

sample = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']},
    index = ['A', 'B', 'C']
)

print(sample)
