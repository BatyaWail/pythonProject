# This is a sample Python script.
from FileOperation import FileOperation


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from FileOperation import SalesData, FileOperation


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
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
