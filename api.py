import requests
import pandas as pd

# Step 1: Use an OCR API to extract text, images, and tables from the PDF file
file_url = 'file:///C:/Users/91915/Desktop/python/demo.pdf'
api_key = 'K84230161688957'

payload = {
  'apikey': api_key,
  'url': file_url,
  'isTable': True,
  'isImage': True
}

r = requests.post('https://api.ocr.space/parse/image', data=payload)

# Step 2: Use a parsing API to convert the extracted text and tables into a structured format
import json

json_data = json.loads(r.text)
parsed_text = json_data['ParsedResults'][0]['ParsedText']
parsed_tables = json_data['ParsedResults'][0]['TextOverlay']['Lines']

# Step 3: Use the Pandas library to read the structured data into a DataFrame
df = pd.read_csv(parsed_text, sep='\n', header=None)

# Step 4: Iterate through the parsed tables and add them to the DataFrame
for i, table in enumerate(parsed_tables):
    df_table = pd.DataFrame(table)
    df = df.append(df_table, ignore_index=True)

# Step 5: Write the DataFrame to an Excel file
df.to_excel('myfile.xlsx', index=False)
