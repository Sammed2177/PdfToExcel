import tabula
import pandas as pd

# Read the PDF file into a list of DataFrames
dfs = tabula.read_pdf("demo.pdf", multiple_tables=True, pages="all", guess=False, lattice=True)

# Create an Excel file and write each DataFrame to a separate sheet
with pd.ExcelWriter("demo.xlsx", engine="openpyxl", mode="w") as writer:
    for i, df in enumerate(dfs):
        df.to_excel(writer, index=False, sheet_name=f"Sheet {i+1}")
