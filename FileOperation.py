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

    #13
    def bar_chart_category_sum(self):
        # sns.get_dataset_names()
        # sns.lineplot(x='Product', y=self.df.calculate_total_sales(() ,data=self.df)
        y=self.calculate_total_sales()
        sns.lineplot(x='Product', y='Total', data=self.df)
        plt.show()
#from gpt
    # def bar_chart_category_sum(self):
    #     # Calculate the sum of quantities sold for each product
    #     product_sales = self.df.groupby('Product')['Quantity'].sum().reset_index()
    #
    #     # Plot a bar chart
    #     plt.figure(figsize=(10, 6))
    #     sns.barplot(x='Product', y='Quantity', data=product_sales)
    #     plt.title('Sum of Quantities Sold for Each Product')
    #     plt.xlabel('Product')
    #     plt.ylabel('Sum of Quantity Sold')
    #     plt.xticks(rotation=45, ha='right')
    #     plt.tight_layout()
    #    plt.show()
    #13
    # def calculate_mean_quantity(self):