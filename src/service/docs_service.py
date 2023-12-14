"""
The `DocsService` class facilitates navigating through pages of text data stored in HTML files.
The `DocsService` class manages the display and navigation of text pages stored in HTML files within a specified folder.
"""
from shared.html_processor import HtmlProcessor


class DocsService:

    def __init__(self, folder_path: str):
        """
        Initialize the DocsService object.

        Parameters:
        - folder_path (str): Path to the folder containing HTML files.
        """
        self.__html_processor = HtmlProcessor(folder_path)
        self.__current_page = 1

    @property
    def current_page(self):
        """
        Retrieve the current page number.

        Returns:
        - int: Current page number.
        """
        return self.__current_page

    def display_page(self):
        """
        Display the text data of the current page.
        """
        text_data = self.__html_processor.get_text_data(self.__current_page)
        print(text_data)

    def change_page(self, page_number):
        """
        Change the current page to the specified page number and display its text data.

        Parameters:
        - page_number (int): Page number to navigate to.
        """

        if page_number < 1 or page_number > len(self.__html_processor.files_data):
            print("Invalid page number.")
        else:
            self.__current_page = page_number
            self.display_page()

    def next_page(self):
        """ Move to the next page (if available) and display its text data."""

        if self.__current_page < len(self.__html_processor.files_data):
            self.__current_page += 1
            self.display_page()
        else:
            print("No next page available.")

    def prev_page(self):
        """ Move to the previous page (if available) and display its text data. """
        if self.current_page > 1:
            self.__current_page -= 1
            self.display_page()
        else:
            print("Already at the first page.")
