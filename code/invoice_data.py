"""
this uses invoice2data to extract text from images
"""

# Importing all the required libraries

from invoice2data import extract_data
from invoice2data.extract.loader import read_templates
from invoice2data.input import pdftotext
import pandas as pd
import json

# Importing custom template
templates = read_templates('./template/')

#print(templates)

# Extract data from PDF
# for now, this filepath need to use the template file ./template/temp.yml
filepath = "./data/pnlsheet.pdf"
# for now, this filepath does not need template file
# filepath = "./data/AmazonWebServices.pdf"
result = extract_data(filepath, templates = templates, input_module = pdftotext)

print("result:")
print(json.dumps(result, indent=2))
# Store the extracted data to a Data-frame
df = pd.DataFrame(data = result)

# Export Data-frame to a csv file
output_file = f"{filepath}-result.csv"
df.to_csv(output_file)


''' 
You can use any desired library to extract data from pdftotext, pdftotext, pdfminer, tesseract. It is optional
and by default pdftotext will be used if not specified.

The custom template named temp.yml is placed in the templates. You can remove the templates parameter in
extract_data(). Default templates will be used

'''

# ex or result from data/pnlsheet/pdf
"""
result:
{
  "issuer": "Arigo Private Limited",
  "invoice_number": null,
  "amount": null,
  "date": null,
  "current_assets": "24,999",
  "cash": [
    "790",
    "16,649"
  ],
  "Petty cash": "16,649",
  "Inventory": "4,235",
  "Fixed assests": "11,229",
  "Leasehold": "225",
  "long-term liabilities": "16,300",
  "Total assets": "36,228",
  "Total liabilities": "20,100",
  "Net assets": "16,128",
  "Working Capital": "21,199",
  "currency": "EUR",
  "lines": [],
  "desc": "Invoice from Arigo Private Limited"
}
"""