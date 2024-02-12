# This is a sample Python script.
import sys

from FileOperation import FileOperation


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from FileOperation import SalesData, FileOperation
from Hebrow import Hebrow
import pandas as pd
from document import Document
from pandas.io.sas.sas_constants import magic
import random
def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    # def main():
    # FileOperation.read_csv("")
    x = SalesData("YafeNof.csv")
    print(x.df)
    x.eliminate_duplicates()
    print("eliminate_duplicates()",x.df)
    print("5", x.calculate_total_sales())
    print("6",x.calculate_total_sales_per_month())
    print("7",x.identify_best_selling_product())
    print("8",x.identify_month_with_highest_sales())
    print("9",x.analys_sales_data())
    print("10",x.add_to_dict_minimest_seling_and_avg())
    print("11",x.calculate_cumulative_sales())
    print("12",x.calculate_90_percent_values())
    #13
    # x.bar_chart_category_sum()
    print("14",x.calculate_mean_quantity())
    # print("15",x.filter_by_sellings_or_and())
    print("15-a",x.filter_by_sellings_and())
    print("15-b",x.filter_by_sellings_or())
    print("16",x.divide_by_2())
    # y=x.calculate_stats()
    # print("17","max",y[0],"sum",y[1],"abs",y[2] )
    print("18",x.convert_date_format()['Date'])
    #task 6
    #1?
    # x.draw_calculate_total_sales()
    #not good
    #x.draw_calculate_total_sales_per_month()
    #2
    # x.draw_identify_best_selling_product()
    #not good
    # x.draw_calculate_total_sales_per_month()
    #3
    # x.draw_analys_sales_data()
    #4
    # x.draw_add_to_dict_minimest_seling_and_avg()
    #5
    # x.draw_calculate_cumulative_sales()
    #6
    # x.draw_calculate_mean_quantity()
    #7
    # x.draw_filter_by_sellings_or()
    #not good
    # x.draw_filter_by_sellings_and()
    #8
    # x.draw_divide_by_2()
    #seabron
    #1--not good
    # x.draw_calculate_stats()
    #1
    # x.draw2_identify_best_selling_product()
    #not good
    # x.draw2_analys_sales_data()
    #not good
    # x.draw2_add_to_dict_minimest_seling_and_avg()
    #2
    # x.draw2_cumulative_sales()
    #not good!
    # x.draw2_90_percent_values()
    #3
    # x.draw2_mean_quantity()
    #not good
    # x.draw2_filter_by_sellings_and()
    # x.Seaborn_Bar_Plot()
    # x.Seaborn_Box_Plot()
    # x.draw_sales_and_highest_amount()
    # x.print_python_version()
    #hebrow
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
    def print_python_version():
        print("Python version:", sys.version)



    # Example usage:
    # handle_parameters(10, 20, value1=30, value1_tag='tag', value2=40, value2_tag='tag')

    random_sales_number, highest_amount_paid =draw_random_number(x.df, 'Sidur')
    print("Random sales number:", random_sales_number)
    print("Highest amount paid:", highest_amount_paid)
    print_python_version()

    def handle_parameters(*args, **kwargs):
        tagged_params = {}
        for arg in args:
            # Check if the parameter is tagged
            if isinstance(arg, str) and arg.endswith('tag'):
                # If tagged, add it to the dictionary with its name as the key
                tagged_params[arg[:-4]] = kwargs[arg[:-4] + '_value']
            else:
                # If not tagged, print its value
                print(arg)

        # Return the dictionary containing tagged parameters
        return tagged_params

    # Example usage:
    result = handle_parameters(10,13, 20, value1=30, value1_tag='tag', value2=40, value2_tag='tag')
    print(result)
    def print_table_slices():
        # Print the first 3 rows
        print("First 3 rows:")
        print(x.df.head(3))

        # Print the last 2 rows
        print("\nLast 2 rows:")
        print(x.df.tail(2))

        # Print a random row
        print("\nRandom row:")
        random_index = random.randint(0, len(x.df) - 1)
        print(x.df.iloc[random_index])

    print_table_slices()
    def iterate_numeric_values():
        for col in x.df.select_dtypes(include=['number']):
            for value in x.df[col]:
                print(value)
    iterate_numeric_values()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
