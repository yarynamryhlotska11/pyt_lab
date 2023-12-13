
from shared.html_processor import HtmlProcessor


class DocsService:

    def __init__(self, folder_path: str):
        self.__html_processor = HtmlProcessor(folder_path)
        self.__current_page = 1

    @property
    def current_page(self):
        return self.__current_page

    def display_page(self):
        text_data = self.__html_processor.get_text_data(self.__current_page)
        print(text_data)

    def change_page(self, page_number):

        if page_number < 1 or page_number > len(self.__html_processor.files_data):
            print("Invalid page number.")
        else:
            self.__current_page = page_number
            self.display_page()

    def next_page(self):

        if self.__current_page < len(self.__html_processor.files_data):
            self.__current_page += 1
            self.display_page()
        else:
            print("No next page available.")

    def prev_page(self):

        if self.current_page > 1:
            self.__current_page -= 1
            self.display_page()
        else:
            print("Already at the first page.")
