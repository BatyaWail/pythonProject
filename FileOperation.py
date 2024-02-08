import pandas as pd;
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

    #3
    def eliminate_duplicates(self):
        # df=FileOperation.read_csv("YafeNof.csv")
        # csvFile.drop_duplicates(inplace=True)
        self.df.drop_duplicates(inplace=True)
     #4
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

   #7
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
   #def calculate_cumulative_sales(self):


