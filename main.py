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



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
