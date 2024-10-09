import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)
print(df)
print("-----------------------------------------------------")
# Accessing data in a DataFrame
print(df['Name'])                 # Access a specific column
print(".....................................................")
print(df.loc[0])                  # Access a specific row using label-based indexing
print("-----------------------------------------------------")
print(df.iloc[1])                 # Access a specific row using integer-based indexing
print(".....................................................")
print(df.loc[0, 'Age'])            # Access a specific element using label-based indexing
print("-----------------------------------------------------")
# Writing data to a CSV file
df.to_csv('data.csv', index=False)

# Reading data from a CSV file into a DataFrame
df = pd.read_csv('data.csv')
print(df)
