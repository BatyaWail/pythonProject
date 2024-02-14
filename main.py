#קראנו את ההוראות בקול רם ובצומת לב מרבית, תודה רבה!!
import sys
from FileOperation import SalesData, FileOperation
import pandas as pd
from document import Document
from pandas.io.sas.sas_constants import magic
import random
from Task8 import Task8, SpecialArray
def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    x = SalesData("YafeNof.csv")
    print(x.df)
    #task1
    #2-4
    x.eliminate_duplicates()
    print("eliminate_duplicates()",x.df)
    #2-5
    print("5", x.calculate_total_sales())
    #2-6
    print("6",x.calculate_total_sales_per_month())
    #2-7
    print("7",x.identify_best_selling_product())
    # 2-8
    print("8",x.identify_month_with_highest_sales())
    # 2-9
    print("9",x.analys_sales_data())
    # 2-10
    print("10",x.add_to_dict_minimest_seling_and_avg())
    #task 3
    # 3-11
    print("11",x.calculate_cumulative_sales())
    # 3-12
    print("12",x.calculate_90_percent_values())
    # 3-13
    x.bar_chart_category_sum()
    # 3-14
    print("14",x.calculate_mean_quantity())
    #3-15
    print("15-a",x.filter_by_sellings_and())
    print("15-b",x.filter_by_sellings_or())
    #3-16
    print("16",x.divide_by_2())
    # y=x.calculate_stats()
    # print("17","max",y[0],"sum",y[1],"abs",y[2] )
    # 4-18
    print("18",x.convert_date_format()['Date'])
    #task 6
    print()
    #Matplotlib
    #1?
    # x.draw_calculate_total_sales()
    #not good
    #x.draw_calculate_total_sales_per_month()
    #2
    x.draw_identify_best_selling_product()
    #not good
    # x.draw_calculate_total_sales_per_month()
    #3
    x.draw_analys_sales_data()
    #4
    x.draw_add_to_dict_minimest_seling_and_avg()
    #5
    x.draw_calculate_cumulative_sales()
    #6
    x.draw_calculate_mean_quantity()
    #7
    x.draw_filter_by_sellings_or()
    #not good
    # x.draw_filter_by_sellings_and()
    #8
    x.draw_divide_by_2()

    #seabron
    #not good
    # x.draw_calculate_stats()
    #1
    x.draw2_identify_best_selling_product()
    #not good
    # x.draw2_analys_sales_data()
    #not good
    # x.draw2_add_to_dict_minimest_seling_and_avg()
    #2
    x.draw2_cumulative_sales()
    #not good!
    # x.draw2_90_percent_values()
    #3
    x.draw2_mean_quantity()
    #not good
    # x.draw2_filter_by_sellings_and()
    #4
    x.Seaborn_Bar_Plot()
    #5
    x.Seaborn_Box_Plot()
    #not good
    # x.draw_sales_and_highest_amount()
    #task-7
    #1-נמצא תוך כדי הפונקציות
    #2
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
    #3
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
    #4
    def print_python_version():
        print("Python version:", sys.version)

    random_sales_number, highest_amount_paid =draw_random_number(x.df, 'Sidur')
    print("Random sales number:", random_sales_number)
    print("Highest amount paid:", highest_amount_paid)
    print_python_version()

    #5
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
    #6
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
    #7
    def iterate_numeric_values():
        for col in x.df.select_dtypes(include=['number']):
            for value in x.df[col]:
                print(value)

    iterate_numeric_values()

    #task-8
    # 8-1
    directory_path=r"C:\Users\User\Documents\!תכנות\שנה ב\Python\pythonProject-Batya&Yeudit"
    task8 = Task8("UsersName.txt", directory_path)
    task8.create_directory_if_not_exists(directory_path)

    #8-2
    usernames_generator = task8.read_usernames("UsersName.txt")
    for username in usernames_generator:
        print(username)

    #8-3
    # Example usage:
    usernames_generator = task8.read_usernames("UsersName.txt")
    usernames = list(usernames_generator)
    special_array = SpecialArray(usernames)

    # Accessible users
    print("Accessible Users:", special_array.get_accessible_users())

    #8-4
    # Even row users among the accessible ones
    print("Even Row Users:", special_array.even_row_users())

    #8-5
    # Example usage:
    task8.verify_email_order("UsersName.txt", "UsersEmail.txt")

    #8-6
    # Get Gmail addresses
    gmail_addresses = task8.get_gmail_addresses("UsersEmail.txt")
    print("Gmail Addresses:", gmail_addresses)

    #8-7
    # Match username to email
    email_username_matches = task8.match_username_to_email("UsersName.txt", "UsersEmail.txt")
    print("Emails matched to username:", email_username_matches)

    #8-8
    # Check if a username is in the list
    username_check_result = task8.check_username_in_list("Dina", "UsersName.txt")
    print(username_check_result)

    # Count the number of 'A's in a username
    a_count = task8.count_letter_a_in_name("Dina")
    print("Number of 'A's in the username:", a_count)

    #8-9
    # Capitalize variable names
    capitalized_names = task8.capitalize_variable_names("UsersName.txt")
    print("Capitalized variable names:", capitalized_names)

    #8-10
    # Example usage:
    customer_list = [9, 5, 19, 43, 4, 88, 76, 20, 15]
    total_earnings = Task8.calculate_earnings(customer_list)
    print("Total earnings:", total_earnings)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#קראנו את ההוראות בקול רם ובצומת לב מרבית, תודה רבה!!

