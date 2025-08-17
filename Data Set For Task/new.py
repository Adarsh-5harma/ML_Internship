import pandas as pd


# Loading the dataset named iris.csv from the specified path
# pd.read_csv is used to read the CSV file into a DataFrame
df = pd.read_csv('./Data Set For Task/1) iris.csv')




# Displaying the first few rows, summary statistics, and information about the DataFrame
print(df.head())

print(df.describe())

print('\nDataFrame Info:')
# This prints a concise summary of the DataFrame, including the number of non-null entries and data types
print(df.info())
print("\nMissing values before handling:")
# Checking for missing values in the DataFrame
print(df.isnull().sum())