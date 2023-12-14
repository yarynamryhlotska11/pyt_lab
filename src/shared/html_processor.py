"""
Module: html_processor

This module defines the HtmlProcessor class, which is responsible for processing HTML files.

Classes:
    - HtmlProcessor: Processes HTML files to extract content and convert it to text.
"""
import os
import html2text

from configuration.logger_config import logger


class HtmlProcessor:
    """
    HtmlProcessor class processes HTML files to extract content and convert it to text.

    Methods:
         __init__(folder_path: str)
         Initializes an HtmlProcessor instance with a specified folder path.

        read_files_in_folder(folder_path: str)
         Reads the contents of all HTML files in the specified folder.

        get_text_data(page_number: int)
        Converts the HTML content of a specified page to text.
 """
    def __init__(self, folder_path: str):
        """
        Initializes an HtmlProcessor instance with a specified folder path.
        """
        self.__files_data = self.read_files_in_folder(folder_path)
        logger.info("Read %s HTML files.", len(self.__files_data))

    @property
    def files_data(self):
        """
        Property: Gets the list of tuples containing file names and HTML contents.
        """
        return self.__files_data

    @staticmethod
    def read_files_in_folder(folder_path: str):
        """
        Reads the contents of all HTML files in the specified folder.
        """

        try:
            html_contents = []
            logger.info("Sorted HTML files in folder: %s", folder_path)
            files = sorted(os.listdir(folder_path))

            for file_name in files:
                file_path = os.path.join(folder_path, file_name)

                if os.path.isfile(file_path) and file_name.lower().endswith('.html'):
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        html_contents.append((file_name, content))
                        logger.info("Read HTML file: %s", file_name)

            return html_contents
        except Exception as e:
            print(f"An error occurred while reading files: {e}")
            logger.error("HTML files weren't read", e)
            return []

    def get_text_data(self, page_number: int):
        """
        Converts the HTML content of a specified page to text.
        """
        if 1 <= page_number <= len(self.__files_data):
            _, content = self.__files_data[page_number - 1]
            return html2text.html2text(content)
        logger.error("Invalid page number: %s", page_number)
        return "Invalid page number."
