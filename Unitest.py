import unittest
from unittest import mock
from unittest.mock import patch, Mock

import pandas as pd
import os
from FileOperation import FileOperation,SalesData  # Replace 'your_module' with the actual module name



class TestFileOperation(unittest.TestCase):

    def setUp(self):
        # Initialize a sample DataFrame for testing
        self.sample_data = {
            'Customer ID': [3, 5, 2, 6, 8, 7, 9, 15, 6, 2, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20],
            'Date': ['15.01.2023', '16.01.2023', '17.01.2023', '10.02.2023', '05.03.2023', '19.01.2023', '13.02.2023', '05.03.2023', '13.02.2023', '17.01.2023', '01.04.2023', '02.04.2023', '03.04.2023', '04.04.2023', '05.04.2023', '06.04.2023', '07.04.2023', '08.04.2023', '09.04.2023', '10.04.2023'],
            'Product': ['Sidur', 'Teilim', 'Sidur', 'Chumash', 'Tanach', 'Sidur', 'Tanach', 'Chumash', 'Gmara', 'Gmara', 'Sidur', 'Teilim', 'Chumash', 'Tanach', 'Gmara', 'Sidur', 'Teilim', 'Chumash', 'Tanach', 'Gmara'],
            'Price': [60, 400, 50, 300, 80, 50, 30, 800, 300, 500, 40, 450, 200, 70, 600, 45, 350, 250, 90, 550],
            'Quantity': [3, 5, 10, 2, 20, 5, 9, 30, 9, 10, 8, 4, 15, 12, 7, 6, 8, 5, 18, 3],
            'Total': [180, 2000, 600, 800, 1800, 250, 2900, 24200, 2900, 5000, 320, 1800, 3000, 840, 4200, 270, 2800, 1250, 1620, 1650]
        }
        self.test_df = pd.DataFrame(self.sample_data)
        self.your_class_instance = FileOperation()  # Instantiate without passing any arguments

    #def test_read_csv(self):
        ## Test reading CSV file
        #file_path = 'YafeNof.csv'
        #result_df = self.your_class_instance.read_csv(file_path)
        #self.assertTrue(result_df.equals(self.test_df))

    # def test_save_to_excel(self):
    #     # Test saving DataFrame to Excel
    #     file_name = 'test_output.xlsx'
    #     self.your_class_instance.save_to_excel(self.test_df, file_name)
    #     # Check if file exists
    #     self.assertTrue(os.path.exists(file_name))


    @patch("pandas.read_csv")
    def test_read_excel_file_found(self, mock_read_csv):
        # בדיקה שהפונקציה פועלת תקין כאשר הקובץ קיים
        file_op = FileOperation()
        file_path = "YafeNof.csv"
        mock_read_csv.return_value = Mock()  # מסימול חזרה של pandas.DataFrame
        result = file_op.read_csv(file_path)
        self.setUp()
        mock_read_csv.assert_called_once_with(file_path)

    @patch("pandas.DataFrame.to_excel")
    def test_save_to_excel(self, mock_to_excel):
        # Sample data
        data = {
            'Customer ID': [3, 5, 2, 6, 8],
            'Date': ['15.01.2023', '16.01.2023', '17.01.2023', '10.02.2023', '05.03.2023'],
            'Product': ['Sidur', 'Teilim', 'Sidur', 'Chumash', 'Tanach'],
            'Price': [60, 400, 50, 300, 80],
            'Quantity': [3, 5, 10, 2, 20],
            'Total': [180, 2000, 600, 800, 1800]
        }

        # Instantiate FileOperation
        file_op = FileOperation()

        # Call save_to_excel method
        file_op.save_to_execl(data, "YafeNof.csv")

        # Assert that to_excel method is called with the correct arguments
        mock_to_excel.assert_called_once_with("YafeNof.csv", index=False)

    def test_eliminate_duplicates2(self):
        # Test eliminating duplicates from DataFrame
        # Create a sample DataFrame with duplicates
        sample_data = {
            'Customer ID': [3, 5, 2, 6, 8, 7, 9, 15, 6, 2, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20],
            'Date': ['15.01.2023', '16.01.2023', '17.01.2023', '10.02.2023', '05.03.2023', '19.01.2023', '13.02.2023',
                     '05.03.2023', '13.02.2023', '17.01.2023', '01.04.2023', '02.04.2023', '03.04.2023', '04.04.2023',
                     '05.04.2023', '06.04.2023', '07.04.2023', '08.04.2023', '09.04.2023', '10.04.2023'],
            'Product': ['Sidur', 'Teilim', 'Sidur', 'Chumash', 'Tanach', 'Sidur', 'Tanach', 'Chumash', 'Gmara', 'Gmara',
                        'Sidur', 'Teilim', 'Chumash', 'Tanach', 'Gmara', 'Sidur', 'Teilim', 'Chumash', 'Tanach',
                        'Gmara'],
            'Price': [60, 400, 50, 300, 80, 50, 30, 800, 300, 500, 40, 450, 200, 70, 600, 45, 350, 250, 90, 550],
            'Quantity': [3, 5, 10, 2, 20, 5, 9, 30, 9, 10, 8, 4, 15, 12, 7, 6, 8, 5, 18, 3],
            'Total': [180, 2000, 600, 800, 1800, 250, 2900, 24200, 2900, 5000, 320, 1800, 3000, 840, 4200, 270, 2800,
                      1250, 1620, 1650]
        }
        # Convert to DataFrame
        test_df = pd.DataFrame(sample_data)

        # Set up the FileOperation instance with the test DataFrame
        your_class_instance = FileOperation(test_df)

        # Call the eliminate_duplicates method
        your_class_instance.eliminate_duplicates()

        # Check if there are any duplicates in the resulting DataFrame
        has_duplicates = your_class_instance.df.duplicated().any()

        # Assert that there are no duplicates
        self.assertFalse(has_duplicates)

    @patch("pandas.DataFrame.drop_duplicates")
    def test_eliminate_duplicates(self, mock_drop_duplicates):
        # Mocking the drop_duplicates method of DataFrame
        file_op = SalesData("YafeNof.csv")
        file_op.eliminate_duplicates()
        # Assert that drop_duplicates method was called on the DataFrame
        mock_drop_duplicates.assert_called_once()

    def test_calculate_total_sales(self):
        # Initialize a sample DataFrame for testing
        sample_data = {
            'Customer ID': [3, 5, 2],
            'Date': ['15.01.2023', '16.01.2023', '17.01.2023'],
            'Product': ['Sidur', 'Teilim', 'Sidur'],
            'Price': [60, 400, 50],
            'Quantity': [3, 5, 10],
            'Total': [180, 2000, 500]
        }
        file_op = SalesData("YafeNof.csv")
        file_op.df = pd.DataFrame(sample_data)

        # Calculate total sales
        total_sales = file_op.calculate_total_sales().sum()  # Sum up the total sales

        # Assert that the total sales value matches the expected value
        expected_total_sales = sum(sample_data['Total'])
        self.assertEqual(total_sales, expected_total_sales)

    #not-run-good
    def test_calculate_total_sales_per_month(self):
        # Initialize a sample DataFrame for testing
        sample_data = {
             'Customer ID': [3, 5, 2, 6, 8, 7, 9],
             'Date': ['15.01.2023', '16.01.2023', '17.01.2023', '10.02.2023', '05.03.2023', '19.01.2023', '13.02.2023'],
             'Product': ['Sidur', 'Teilim', 'Sidur', 'Chumash', 'Tanach', 'Sidur', 'Tanach'],
             'Price': [60, 400, 50, 300, 80, 50, 30],
             'Quantity': [3, 5, 10, 2, 20, 5, 9],
             'Total': [180, 2000, 600, 800, 1800, 250, 2900]
         }
        file_op = SalesData("YafeNof.csv")
        file_op.df = pd.DataFrame(sample_data)

        # Calculate total sales per month
        result = file_op.calculate_total_sales_per_month()

        # Expected result based on the sample data
        expected_result = pd.Series([830, 800, 2900], index=pd.Int64Index([1, 2, 3]))

        # Assert that the calculated total sales per month matches the expected result
        pd.testing.assert_series_equal(result, expected_result)
    # def test_calculate_total_sales_per_month(self):
    #     # Initialize a sample DataFrame for testing
    #     sample_data = {
    #         'Customer ID': [3, 5, 2, 6, 8, 7, 9],
    #         'Date': ['15.01.2023', '16.01.2023', '17.01.2023', '10.02.2023', '05.03.2023', '19.01.2023', '13.02.2023'],
    #         'Product': ['Sidur', 'Teilim', 'Sidur', 'Chumash', 'Tanach', 'Sidur', 'Tanach'],
    #         'Price': [60, 400, 50, 300, 80, 50, 30],
    #         'Quantity': [3, 5, 10, 2, 20, 5, 9],
    #         'Total': [180, 2000, 600, 800, 1800, 250, 2900]
    #     }
    #     file_op = SalesData("YafeNof.csv")
    #     file_op.df = pd.DataFrame(sample_data)
    #
    #     # Calculate total sales per month
    #     result = file_op.calculate_total_sales_per_month()
    #
    #     # Expected result based on the sample data
    #     expected_result = pd.Series([830, 800, 2900], index=pd.Int64Index([1, 2, 3]))
    #
    #     # Assert that the calculated total sales per month matches the expected result
    #     pd.testing.assert_series_equal(result, expected_result)
    def test_identify_best_selling_product(self):
        # Initialize a sample DataFrame for testing
        sample_data = {
            'Customer ID': [3, 5, 2, 6, 8, 7, 9],
            'Date': ['15.01.2023', '16.01.2023', '17.01.2023', '10.02.2023', '05.03.2023', '19.01.2023', '13.02.2023'],
            'Product': ['Sidur', 'Teilim', 'Sidur', 'Chumash', 'Tanach', 'Sidur', 'Tanach'],
            'Price': [60, 400, 50, 300, 80, 50, 30],
            'Quantity': [3, 5, 10, 2, 20, 5, 9],
            'Total': [180, 2000, 600, 800, 1800, 250, 2900]
        }
        file_op = SalesData("YafeNof.csv")
        file_op.df = pd.DataFrame(sample_data)

        # Call the identify_best_selling_product method
        best_selling_product = file_op.identify_best_selling_product()

        # Expected result based on the sample data
        expected_best_selling_product = 'Tanach'

        # Assert that the identified best selling product matches the expected result
        self.assertEqual(best_selling_product, expected_best_selling_product)

if __name__ == '__main__':
    unittest.main()
