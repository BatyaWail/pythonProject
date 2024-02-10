from typing import List

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
class FileOperation:
    #1
    def read_csv(self,file_path:str):
        return pd.read_csv(file_path)
    #2
    def save_to_execl(self,data,file_name:str):
        return pd.DataFrame(data)

class SalesData:
    def __init__(self,path:str):
        #self.df=FileOperation.read_csv(path)
        x=FileOperation()
        self.df=x.read_csv(path)
        self.numpy_array = self.df.values


    #4
    def eliminate_duplicates(self):
        # df=FileOperation.read_csv("YafeNof.csv")
        # csvFile.drop_duplicates(inplace=True)
        self.df.drop_duplicates(inplace=True)
     #5
    def calculate_total_sales(self):
        return self.df['Total']
    #6

    def calculate_total_sales_per_month(self):
        self.df['Date'] = pd.to_datetime(self.df['Date'], format='%d.%m.%Y',errors='coerce')
        # Group by month and calculate the sum of 'Total' for each month
        monthly_sum = self.df.groupby(self.df['Date'].dt.month)['Total'].sum()
        return monthly_sum

    #7
    #def identify_best_selling_product(self):
       # maxProudact = self.df.groupby(self.df.product)["Quantity"]
       # maxProudact=max(maxProudact.sum())
       # return maxProudact
    def identify_best_selling_product(self):
        # Group by product and sum the quantities sold
        product_sales = self.df.groupby('Product')['Quantity'].sum()
        # Find the product with the maximum total quantity sold
        best_selling_product = product_sales.idxmax()
        # Return the name of the best-selling product
        return best_selling_product

   #8
    def identify_month_with_highest_sales(self):
        maxMonth= self.calculate_total_sales_per_month()
        return  max(maxMonth)
   #9
    def analys_sales_data(self):
        x=self.identify_best_selling_product()
        y=self.identify_month_with_highest_sales()
        dictionary=dict(best_selling_product= x, month_with_highest_sales= y )
        return dictionary
    #10
    def add_to_dict_minimest_seling_and_avg(self):
        product_sales = self.df.groupby('Product')['Quantity'].sum()
        # Find the product with the maximum total quantity sold
        less_selling_product = product_sales.idxmin()
        # Return the name of the best-selling product

        self.df['Date'] = pd.to_datetime(self.df['Date'], format='%d.%m.%Y',errors='coerce')
        # Group by month and calculate the sum of 'Total' for each month
        monthly_sum = self.df.groupby(self.df['Date'].dt.month)['Total'].mean()
        dictionary=self.analys_sales_data()
        dictionary['monthly_sum'] = monthly_sum
        dictionary['less_selling_product'] = less_selling_product
        return dictionary

    #task 3
    #11

    def calculate_cumulative_sales(self):
        # Convert 'Date' column to datetime type if it's not already
        self.df['Date'] = pd.to_datetime(self.df['Date'], format='%d.%m.%Y')

        # Calculate the product of 'Quantity' and 'Price'
        self.df['Total_Sales'] = self.df['Quantity'] * self.df['Price']

        # Group by 'Product' and month, and calculate the cumulative sum of 'Total_Sales' for each group
        cumulative_sales = self.df.groupby(['Product', self.df['Date'].dt.month])['Total_Sales'].sum().groupby(
            level=0).cumsum()

        return cumulative_sales

    #mybe good
    # def calculate_cumulative_sales(self):
    #     # Convert 'Date' column to datetime type if it's not already
    #     self.df['Date'] = pd.to_datetime(self.df['Date'], format='%d.%m.%Y')
    #
    #     # Calculate the product of 'Quantity' and 'Price' and store it in a new column named 'Total'
    #     self.df['Total'] = self.df['Price'] * self.df['Quantity']
    #
    #     # Group by 'Product' and 'Date', and calculate the total sales for each group
    #     monthly_sales = self.df.groupby(['Product', self.df['Date'].dt.month])['Total'].sum()#.reset_index()
    #
    #     # Calculate the cumulative sum of sales for each product across months
    #     cumulative_sales = monthly_sales.groupby('Product')['Total'].cumsum()
    #
    #     return cumulative_sales
    #12
    def calculate_90_percent_values(self):
        self.df['Discount'] = np.round((self.df['Total'] * 0.9))
        return self.df
    #13
        # sns.get_dataset_names()
    # def bar_chart_category_sum(self):
    #     # sns.get_dataset_names()
    #
    #     sns.lineplot(x='Product', y=self.df.calculate_total_sales() ,data=self.df)
    #     y=self.calculate_total_sales()
    #     sns.lineplot(x='Product', y='Total', data=self.df)
    #     plt.show()
#from gpt
    def bar_chart_category_sum(self):
        # Calculate the sum of quantities sold for each product
        product_sales = self.df.groupby('Product')['Quantity'].sum().reset_index()

        # Plot a line chart
        plt.figure(figsize=(10, 6))
        sns.lineplot(x='Product', y='Quantity', data=product_sales, marker='o')
        plt.title('Sum of Quantities Sold for Each Product')
        plt.xlabel('Product')
        plt.ylabel('Sum of Quantity Sold')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    #13
    # def calculate_mean_quantity(self):
    #     numpy_array = self.df.values
    #     sorted_indices = np.argsort(-numpy_array[:, 5])  # Assuming 'Total' is the 6th column (index 5)
    #     # Sort the numpy_array using the sorted indices
    #     sorted_numpy_array = numpy_array[sorted_indices]
    #     mean=sorted_numpy_array.mean(sorted_indices)
    #     max2=sorted_numpy_array.max(sorted_indices,2)
    #     return [mean,max2]
    def calculate_mean_quantity(self):
        sorted_indices = np.argsort(-self.numpy_array[:, 5])  # Assuming 'Total' is the 6th column (index 5)
        # Sort the numpy_array using the sorted indices
        sorted_numpy_array = self.numpy_array[sorted_indices]

        # Calculate mean
        mean = np.mean(sorted_numpy_array[:, 5])  # Assuming 'Total' is the 6th column (index 5)

        # Calculate median
        median = np.median(sorted_numpy_array[:, 5])  # Assuming 'Total' is the 6th column (index 5)

        # Calculate second maximum
        max2 = np.unique(sorted_numpy_array[:, 5])[-2]  # Second maximum

        return mean, median, max2
    #15

    # def filter_by_sellings_or_and(self):
    #     # Condition 1: Number of selling more than 5 or number of selling equals 0
    #     condition_1 = (self.df['Quantity'] > 5) | (self.df['Quantity'] == 0)
    #
    #     # Condition 2: Price above 300 $ and sold less than 2 times
    #     condition_2 = (self.df['Price'] > 300) & (self.df['Quantity'] < 2)
    #
    #     # Combine conditions using logical AND
    #     filtered_df = self.df[condition_1 & condition_2]
    #
    #     return filtered_df
    def filter_by_sellings_or(self):
        # Condition 1: Number of selling more than 5 or number of selling equals 0
        condition_1 = (self.df['Quantity'] > 5) | (self.df['Quantity'] == 0)
        # Combine conditions using logical AND
        filtered_df = self.df[condition_1 ]
        return filtered_df
    def filter_by_sellings_and(self):
        # Condition 2: Price above 300 $ and sold less than 2 times
        condition_2 = (self.df['Price'] > 300) & (self.df['Quantity'] < 2)

        # Combine conditions using logical AND
        filtered_df = self.df[condition_2]

        return filtered_df
    #16
    def divide_by_2(self):
        self.df['BlackFridayPrice'] = self.df['Total'] / 2
        return self.df
        # x = FileOperation()
        # self.df = x.save_to_execl()
    #17
    # def calculate_stats(self, columns: str = None):
    #     if(columns!=None):
    #         max= self.numpy_array.max(columns)
    #         sum=self.numpy_array.sum(columns)
    #         asc=self.numpy_array.__abs__(columns)
    #     else:
    #         max= self.numpy_array.max()
    #         sum=self.numpy_array.sum()
    #         asc=self.numpy_array.__abs__()
    #     return max,sum,asc
    def calculate_stats(self, columns: str = None):
        if columns is not None:
            # Calculate stats for specific columns
            column_indices = [self.df.columns.get_loc(col) for col in columns.split(',')]
            max_vals = self.numpy_array[:, column_indices].max(axis=0)
            sums = self.numpy_array[:, column_indices].sum(axis=0)
            abs_vals = np.abs(self.numpy_array[:, column_indices])
        else:
            # Calculate stats for all columns
            max_vals = self.numpy_array.max(axis=0)
            sums = self.numpy_array.sum(axis=0)
            abs_vals = np.abs(self.numpy_array)

        return max_vals, sums, abs_vals
    #18
    #def convert_date_format(self, date_columns:List=None):
        #self.df['Date'] = pd.to_datetime(self.df['Date'], format='%d.%m.%Y %H:%M:%S')
        #return self.df
    def convert_date_format(self, date_columns: List = None):
        if date_columns is None:
            date_columns = ['Date']  # Assuming 'Date' is the name of the column containing dates

        for column in date_columns:
            #self.df[column] = pd.to_datetime(self.df[column], format='%d.%m.%Y %H:%M:%S')
            self.df[column] = pd.to_datetime(self.df[column], format='%d.%m.%Y %H:%M:%S', errors='coerce')

            print(self.df[column])
        return self.df


