import requests

file_url = 'file:///C:/Users/91915/Desktop/python/demo.pdf'
api_key = 'K84230161688957'

payload = {
  'apikey': api_key,
  'url': file_url
}

r = requests.post('https://api.ocr.space/parse/image', data=payload)

# Step 2: Use a parsing API to convert the extracted text into a structured format.
import json

json_data = json.loads(r.text)
parsed_text = json_data['ParsedResults'][0]['ParsedText']

# Step 3: Use an Excel or CSV API to write the structured data into an Excel or CSV file.
import pandas as pd

df = pd.read_csv(parsed_text)

# Write the dataframe to an Excel file
df.to_excel('myfile.xlsx', index=False)

# Write the dataframe to a CSV file
df.to_csv('myfile.csv', index=False)