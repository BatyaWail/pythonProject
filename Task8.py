import os
import pandas as pd
from document import Document
from numpy.random import random
from pandas.io.sas.sas_constants import magic

class Task8:
    def __init__(self, file_path, directory_path):
        self.file_path = file_path
        self.usernames = self.read_usernames("UsersName.txt") if file_path else None
        self.directory_path = directory_path
    # משימה 8 תרגיל 1

    #8-1
    def create_directory_if_not_exists(self, directory_path: str):
        if os.path.exists(self.file_path):
            return True
        else:
            directory = os.path.join(os.getcwd(), directory_path)
            os.makedirs(directory, exist_ok=True)
            new_file_path = os.path.join(directory, os.path.basename(self.file_path))
            with open(new_file_path, 'w') as file:
                file.write("default_content")
            return False
    #8-2
    @staticmethod
    def read_usernames(file_path):
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    yield line.strip()
        except FileNotFoundError:
            print(f"File not found at {file_path}")
            return None
        except Exception as e:
            print(f"Error occurred while reading file: {e}")
            return None
        # def read_users_from_file(self,file_path:str):
        #     self.create_directory_if_not_exists(file_path)
        #     with open(file_path, 'r') as file:
        #         lines = file.read().splitlines()
        #         for line in lines:
        #             yield line

   # סעיפים 4,3 נמצאים במחלקת SpecialArray

    #8-5
    @staticmethod
    def read_emails(file_path):
        try:
            with open(file_path, 'r') as file:
                emails = [line.strip() for line in file]
                return emails
        except FileNotFoundError:
            print(f"File not found at {file_path}")
            return None
        except Exception as e:
            print(f"Error occurred while reading file: {e}")
            return None
    #8-5
    @staticmethod
    def verify_email_order(usernames_file, emails_file):
        usernames_generator = Task8.read_usernames(usernames_file)
        usernames = list(usernames_generator)
        emails = Task8.read_emails(emails_file)

        if usernames == emails:
            print("Emails are in the correct order.")
        else:
            print("Emails are not in the correct order.")

    #8-6
    @staticmethod
    def get_gmail_addresses(emails_file):
        emails = Task8.read_emails(emails_file)
        gmail_addresses = [email for email in emails if email.endswith('@gmail.com')]
        return gmail_addresses

    #8-7
    @staticmethod
    def match_username_to_email(usernames_file, emails_file):
        usernames_generator = Task8.read_usernames(usernames_file)
        usernames = list(usernames_generator)
        emails = Task8.read_emails(emails_file)

        # Create a dictionary to store emails as keys for O(1) lookup
        email_dict = {email: False for email in emails}

        # Check if each username is present in any of the emails
        for username in usernames:
            for email in email_dict.keys():
                if username in email:
                    email_dict[email] = True

        return email_dict

    #8-8
    @staticmethod
    def check_username_in_list(username, usernames_file):
        # Convert username to Husky code
        husky_code = username.upper().replace('A', 'H').replace('B', 'U').replace('C', 'S').replace('D', 'K').replace(
            'E', 'Y').replace('F', ' ')
        # Convert Husky code back to string
        original_username = husky_code.replace('H', 'A').replace('U', 'B').replace('S', 'C').replace('K', 'D').replace(
            'Y', 'E').replace(' ', 'F')

        usernames_generator = Task8.read_usernames(usernames_file)
        usernames_list = [name.upper() for name in
                          usernames_generator]  # Convert usernames to uppercase for case-insensitive comparison

        if original_username in usernames_list:
            return f"{original_username} is in the list."
        else:
            return f"{original_username} is not in the list."
    @staticmethod
    def count_letter_a_in_name(username):
        return username.upper().count('A')

    #8-9

    @staticmethod
    def capitalize_variable_names(usernames_file):
        # New function to capitalize variable names
        usernames_generator = Task8.read_usernames(usernames_file)
        capitalized_names = [name.capitalize() for name in usernames_generator]
        return capitalized_names

    #8-10

    @staticmethod
    def calculate_earnings(customer_list):
        total_earnings = 0
        last_divisible_by_8 = None
        for i, num in enumerate(customer_list):
            if num % 8 == 0:
                total_earnings += 200
                last_divisible_by_8 = i
            else:
                if last_divisible_by_8 is not None and i > last_divisible_by_8:
                    total_earnings += 50
        return total_earnings


class SpecialArray:
    def __init__(self, usernames):
        self.usernames = usernames
        self.length = len(usernames)
        self.accessible_users = int(self.length * 0.9)  # 90% of users are accessible
    #8-3
    def get_accessible_users(self):
        return self.usernames[self.accessible_users:]
    #8-4
    def even_row_users(self):
        return [self.usernames[i] for i in range(self.accessible_users) if i % 2 == 1]
