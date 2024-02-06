import pandas as pd;
class FileOperation:
    def read_csv(self,file_path:str):
        return pd.read_csv(file_path)
    def save_to_execl(self,data,file_name:str):
        return pd.DataFrame(data)

class SalesData:
    def __init__(self):
        self.df=FileOperation.read_csv("YafeNof.csv")

    def eliminate_duplicates(self):
        # df=FileOperation.read_csv("YafeNof.csv")
        # csvFile.drop_duplicates(inplace=True)
        self.df.drop_duplicates(inplace=True)
    def calculate_total_sales(self):
        return self.df['Total']
    def  calculate_total_sales_per_month(self):
        self.df.Date=pd.to_datetime(self.df.Date)#להפוך את התאריך לסוג תאריך
        # Group by month and calculate the sum of 'Total' for each month
        monthly_sum = self.df.groupby(self.df['Date'].dt.month)['Total'].sum()

        # Display the result
        return monthly_sum
    def identify_best_selling_product(self):
        maxProudact = self.df.groupby(self.df.product)['Quantity'].sum()
        maxProudact=max(maxProudact)
        return maxProudact
    def identify_month_with_highest_sales(self):
        maxMonth= self.calculate_total_sales_per_month()
        return  max(maxMonth)
    def analys_sales_data(self):
        x=self.identify_best_selling_product()
        y=self.identify_month_with_highest_sales()
        dictonary=dict(best_selling_product= x, month_with_highest_sales= y )
        return dictonary
