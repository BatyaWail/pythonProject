# import magic
import pandas as pd
from document import Document
from pandas.io.sas.sas_constants import magic
import random


class Hebrow:
    def __init__(self):
        print("yyyyyyyyyyyyyyyy")
    def read_file(file_path):
        # Use python-magic to identify the file type
        mime = magic.Magic(mime=True)
        file_type = mime.from_file(file_path)

        if 'text/plain' in file_type:
            with open(file_path, 'r') as file:
                return file.read()
        elif 'csv' in file_type:
            return pd.read_csv(file_path)
        elif 'application/msword' in file_type:
            doc = Document(file_path)
            text = [paragraph.text for paragraph in doc.paragraphs]
            return "\n".join(text)
        # Add more file types as needed
        else:
            raise ValueError(f"Unsupported file type: {file_type}")

    def draw_random_number(df, product_name):
        # Filter the DataFrame to get data for the specified product
        product_data = df[df['Product'] == product_name]

        # Get the number of sales for the product
        sales = product_data['Quantity'].tolist()

        # Get the highest amount paid for the product
        highest_amount_paid = product_data['Total'].max()

        # Draw a random number from the sales data
        random_sales_number = random.choice(sales)

        return random_sales_number, highest_amount_paid
