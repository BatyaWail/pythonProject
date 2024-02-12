# import os
# import unittest
#
# import pandas as pd
#
# from FileOperation import FileOperation
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here
#
#     def setUp(self):
#         # Initialize a sample DataFrame for testing
#         self.sample_data = {
#             'Product': ['A', 'B', 'C', 'A', 'B'],
#             'Quantity': [10, 20, 30, 40, 50],
#             'Total': [100, 200, 300, 400, 500],
#             'Date': ['01.01.2023', '02.01.2023', '03.01.2023', '04.01.2023', '05.01.2023']
#         }
#         self.test_df = pd.DataFrame(self.sample_data)
#         self.your_class_instance = FileOperation(self.test_df)
#
#     def test_read_csv(self):
#         # Test reading CSV file
#         # Assuming you have a CSV file named 'test_data.csv' with sample_data
#         file_path = 'test_data.csv'
#         result_df = self.your_class_instance.read_csv(file_path)
#         self.assertTrue(result_df.equals(self.test_df))
#
#     def test_save_to_excel(self):
#         # Test saving DataFrame to Excel
#         file_name = 'test_output.xlsx'
#         self.your_class_instance.save_to_excel(self.test_df, file_name)
#         # Check if file exists
#         self.assertTrue(os.path.exists(file_name))
#
#
# if __name__ == '__main__':
#     unittest.main()

import unittest
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

    def test_read_csv(self):
        # Test reading CSV file
        file_path = 'YafeNof.csv'
        result_df = self.your_class_instance.read_csv(file_path)
        self.assertTrue(result_df.equals(self.test_df))

    def test_save_to_excel(self):
        # Test saving DataFrame to Excel
        file_name = 'test_output.xlsx'
        self.your_class_instance.save_to_excel(self.test_df, file_name)
        # Check if file exists
        self.assertTrue(os.path.exists(file_name))

    # Write more test methods for other functions similarly

if __name__ == '__main__':
    unittest.main()
