import pandas as pd


# Loading the dataset named iris.csv from the specified path
# pd.read_csv is used to read the CSV file into a DataFrame
df = pd.read_csv('./Data Set For Task/1) iris.csv')


# Since we dont have missing values but for practice we are doing below task

# to work with missing we have dataframes dropna(), drop () and fillna() methods



# Separate numerical and categorical columns

numerical_cols = df.select_dtypes(include = ["number"]).columns
categorical_cols = df.select_dtypes(include = ["object"]).columns

# Impute numerical missing values with mean
# we have used fillna() method to fill missing values with the mean of the column

for col in numerical_cols:
    if df[col].isnull().any():
        df[col].fillna(df[col].mean(), inplace = True)

# Impute Categorical missing values with the mode

for col in categorical_cols:
    if df[col].isnull().any():
        df[col].fillna(df[col].mode()[0], inplace = True)


print("\n Dataframe after Imputation: ")
print(df.head())

print("Missing Values after Handling")
print(df.isnull().sum())