import camelot 
import pandas as pd
from camelot import extract_tables

# Extract the tables from the PDF file
tables = extract_tables('demo.pdf', method='lattice')

# Create a list to store the DataFrames
df_list = []

# Iterate over the tables
for i, table in enumerate(tables):
    # Convert the table to a DataFrame
    df = table.df

    # Duplicate the DataFrame and append it to the list
    df_list.append(df)
    df_list.append(df)

# Concatenate all the DataFrames into a single DataFrame
df = pd.concat(df_list, ignore_index=True)

# Convert the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False, header=False)