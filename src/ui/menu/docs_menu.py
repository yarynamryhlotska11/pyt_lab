
from service.docs_service import DocsService


class DocsMenu:

    def __init__(self, folder_path: str):

        self.docs_service = DocsService(folder_path)

    @staticmethod
    def print_menu():

        print("1. Display current page")
        print("2. Change to a specific page")
        print("3. Move to the next page")
        print("4. Move to the previous page")
        print("0. Exit")

    def run(self):

        while True:
            print("Current Page:", self.docs_service.current_page)
            self.print_menu()

            try:
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    self.docs_service.display_page()
                elif choice == 2:
                    page_number = int(input("Enter the page number: "))
                    self.docs_service.change_page(page_number)
                elif choice == 3:
                    self.docs_service.next_page()
                elif choice == 4:
                    self.docs_service.prev_page()
                elif choice == 0:
                    break
                else:
                    print("Invalid choice. Please enter a corresponding number")

            except ValueError:
                print("Invalid input. Please enter a number.")
