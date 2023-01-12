# pip install tabula
import tabula
# Read a PDF File
df = tabula.read_pdf("sam.pdf", pages='all')
# convert PDF into CSV
tabula.convert_into("sam.pdf", "sam.csv", output_format="csv", pages='all')
print(df)