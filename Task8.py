import os

import pandas as pd
from document import Document
from pandas.io.sas.sas_constants import magic
class Node:
    def __init__(self, value=None, level=0):
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self):
        self.head = Node()
        self.max_level = 0

    def random_level(self):
        level = 0
        while random.random() < 0.5 and level < self.max_level + 1:
            level += 1
        return level

    def insert(self, value):
        level = self.random_level()
        if level > self.max_level:
            for i in range(self.max_level + 1, level + 1):
                self.head.forward.append(None)
            self.max_level = level

        new_node = Node(value, level)
        update = [None] * (level + 1)
        current = self.head

        for i in range(self.max_level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        for i in range(level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def display(self):
        current = self.head.forward[0]
        while current:
            print(current.value)
            current = current.forward[0]
class Task8:

    # #where to put it????
    # # def read_file(self, file_path):
    # #     # Use python-magic to identify the file type
    # #     mime = magic.Magic(mime=True)
    # #     file_type = mime.from_file(file_path)
    # #
    # #     if 'text/plain' in file_type:
    # #         with open(file_path, 'r') as file:
    # #             return file.read()
    # #     elif 'csv' in file_type:
    # #         return pd.read_csv(file_path)
    # #     elif 'application/msword' in file_type:
    # #         doc = Document(file_path)
    # #         text = [paragraph.text for paragraph in doc.paragraphs]
    # #         return "\n".join(text)
    # #     # Add more file types as needed
    # #     else:
    # #         raise ValueError(f"Unsupported file type: {file_type}")
    # #
    # # def read_create_file(self, file_info):
    # #     # Split file_info into name and extension
    # #     name, extension = os.path.splitext(file_info)
    # #
    # #     # Define file path and folder path
    # #     folder_path = "pages"
    # #     file_path = os.path.join(folder_path, file_info)
    # #
    # #     # Check if folder exists, if not create it
    # #     if not os.path.exists(folder_path):
    # #         os.makedirs(folder_path)
    # #         print(f"Directory '{folder_path}' created.")
    # #
    # #     # Check if the file exists, if not create it
    # #     if not os.path.exists(file_path):
    # #         with open(file_path, 'w') as file:
    # #             print(f"File '{file_path}' created.")
    # #
    # #     # Use read_file function to read the content of the file
    # #     try:
    # #         return self.read_file(file_path)
    # #     except ValueError:
    # #         # If unsupported file type, create a new text file and return its path
    # #         new_file_path = os.path.join(os.path.dirname(file_path), "Kim.txt")
    # #         with open(new_file_path, 'w') as file:
    # #             file.write("New Kim.txt file created.")
    # #         return new_file_path
    # #
    # # def read_users(self, file_info):
    # #     content = self.read_create_file(file_info)
    # #     # Use generator to yield each username
    # #     for username in content.split('\n'):
    # #         yield username.strip()
    # def read_file(self, file_path):
    #     # Use python-magic to identify the file type
    #     mime = magic.Magic(mime=True)
    #     if isinstance(file_path, bytes):
    #         file_path = file_path.decode()  # Decode bytes to string
    #     file_type = mime.from_file(file_path)
    #
    #     if 'text/plain' in file_type:
    #         with open(file_path, 'r') as file:
    #             return file.read()
    #     elif 'csv' in file_type:
    #         return pd.read_csv(file_path)
    #     elif 'application/msword' in file_type:
    #         doc = Document(file_path)
    #         text = [paragraph.text for paragraph in doc.paragraphs]
    #         return "\n".join(text)
    #     # Add more file types as needed
    #     else:
    #         raise ValueError(f"Unsupported file type: {file_type}")
    #
    # # def read_create_file(self, file_info):
    # #     # Split file_info into name and extension
    # #     name, extension = os.path.splitext(file_info)
    # #
    # #     # Define file path and folder path
    # #     folder_path = "pages"
    # #     file_path = os.path.join(folder_path, file_info)
    # #
    # #     # Check if folder exists, if not create it
    # #     if not os.path.exists(folder_path):
    # #         os.makedirs(folder_path)
    # #         print(f"Directory '{folder_path}' created.")
    # #
    # #     # Check if the file exists, if not create it
    # #     if not os.path.exists(file_path):
    # #         with open(file_path, 'w') as file:
    # #             print(f"File '{file_path}' created.")
    # #
    # #     # Use read_file function to read the content of the file
    # #     try:
    # #         return self.read_file(file_path)
    # #     except ValueError:
    # #         # If unsupported file type, create a new text file and return its path
    # #         new_file_path = os.path.join(os.path.dirname(file_path), "Kim.txt")
    # #         with open(new_file_path, 'w') as file:
    # #             file.write("New Kim.txt file created.")
    # #         return new_file_path
    # def read_create_file(self, file_info):
    #     # Split file_info into name and extension
    #     name, extension = os.path.splitext(file_info)
    #
    #     # Define file path and folder path
    #     folder_path = "pages"
    #     file_path = os.path.join(folder_path, file_info)
    #
    #     # Check if folder exists, if not create it
    #     if not os.path.exists(folder_path):
    #         os.makedirs(folder_path)
    #         print(f"Directory '{folder_path}' created.")
    #
    #     # Check if the file exists, if not create it
    #     if not os.path.exists(file_path):
    #         with open(file_path, 'w') as file:
    #             print(f"File '{file_path}' created.")
    #
    #     # Use read_file function to read the content of the file
    #     try:
    #         return self.read_file(file_path)
    #     except ValueError:
    #         # If unsupported file type, create a new text file and return its path
    #         new_file_path = os.path.join(os.path.dirname(file_path), "Kim.txt")
    #         with open(new_file_path, 'w') as file:
    #             file.write("New Kim.txt file created.")
    #         return new_file_path
    # def read_users(self, file_info):
    #     content = self.read_create_file(file_info)
    #     # Use generator to yield each username
    #     for username in content.split('\n'):
    #         yield username.strip()



    # def read_file(self, file_path):
    #     # Use python-magic to identify the file type
    #     mime = magic.Magic(mime=True)
    #     if isinstance(file_path, bytes):
    #         file_path = file_path.decode()  # Decode bytes to string
    #     file_type = mime.from_file(file_path)
    #
    #     if 'text/plain' in file_type:
    #         with open(file_path, 'r') as file:
    #             return file.read()
    #     elif 'csv' in file_type:
    #         return pd.read_csv(file_path)
    #     elif 'application/msword' in file_type:
    #         doc = Document(file_path)
    #         text = [paragraph.text for paragraph in doc.paragraphs]
    #         return "\n".join(text)
    #     # Add more file types as needed
    #     else:
    #         raise ValueError(f"Unsupported file type: {file_type}")

    # def read_create_file(self, file_info):
    #     # Convert file_info to string if it's bytes
    #     if isinstance(file_info, bytes):
    #         file_info = file_info.decode()
    #
    #     # Split file_info into name and extension
    #     name, extension = os.path.splitext(file_info)
    #
    #     # Define file path and folder path
    #     folder_path = "pages"
    #     file_path = os.path.join(folder_path, file_info)
    #
    #     # Check if folder exists, if not create it
    #     if not os.path.exists(folder_path):
    #         os.makedirs(folder_path)
    #         print(f"Directory '{folder_path}' created.")
    #
    #     # Check if the file exists, if not create it
    #     if not os.path.exists(file_path):
    #         with open(file_path, 'w') as file:
    #             print(f"File '{file_path}' created.")
    #
    #     # Use read_file function to read the content of the file
    #     try:
    #         return self.read_file(file_path)
    #     except ValueError:
    #         # If unsupported file type, create a new text file and return its path
    #         new_file_path = os.path.join(os.path.dirname(file_path), "Kim.txt")
    #         with open(new_file_path, 'w') as file:
    #             file.write("New Kim.txt file created.")
    #         return new_file_path

    # def read_users(self, file_info):
    #     content = self.read_users_from_file(file_info)
    #     # Use generator to yield each username
    #     for username in content.split('\n'):
    #         yield username.strip()

    # משימה 8 תרגיל 1
    def check_and_create_directory(self,file_path):
        # בדיקה אם הקובץ קיים
        if not os.path.exists(file_path):
            # יצירת תיקייה חדשה
            directory = os.path.dirname(file_path)
            os.makedirs(directory)
            print(f"The directory {directory} was created.")
        else:
            print("The file exists.")

    def read_users_from_file(self,file_path):
        self.check_and_create_directory(file_path)
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()
            for line in lines:
                yield line

    def __init__(self):
        self.skip_list = SkipList()

    def insert_user_names(self, user_names):
        num_to_skip = int(len(user_names) * 0.1)
        user_names_to_skip = user_names[num_to_skip:]
        for name in user_names_to_skip:
            self.skip_list.insert(name)

    def print_user_names(self):
        print("User Names:")
        self.skip_list.display()

    # def check_and_create_directory(self, folder_path):
    #     if not os.path.exists(folder_path):
    #         os.makedirs(folder_path)
    #         print(f"Directory '{folder_path}' created.")
    # def read_users_from_csv(self, file_path):
    #     df = pd.read_csv(file_path)
    #     user_names = df['UserName'].tolist()
    #     self.insert_user_names(user_names)
    # def read_users_from_csv(self, file_path):
    #     folder_path = os.path.dirname(file_path)
    #     self.check_and_create_directory(folder_path)
    #
    #     df = pd.read_csv(file_path)
    #     user_names = df['UserName'].tolist()
    #     self.insert_user_names(user_names)

    def read_users_from_file(self, file_path):
        folder_path = os.path.dirname(file_path)
        self.check_and_create_directory(folder_path)

        _, file_extension = os.path.splitext(file_path)
        if file_extension == '.csv':
            return self.read_users_from_csv(file_path)
        elif file_extension == '.txt':
            return self.read_users_from_txt(file_path)  # Call read_users_from_txt for .txt files
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")

    def read_users_from_txt(self, file_path):
        return self.read_users_from_file(file_path)