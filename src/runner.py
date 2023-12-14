"""
User_interface Module for Project_labs Menus
Example:
    To run the module and start the menu facade, execute the script as follows:
        $ python module_name.py
Functions:  None
If __name__ == '__main__':
    Creates a MenuFacade instance with a list of menu tuples and starts the menu.
Author: Mryhlotska Yaryna
"""
from user_interface.menu_ui.facade_menu import MenuFacade


if __name__ == '__main__':
    # Creating an instance of the MenuFacade class
    menuFacade = MenuFacade()
    # Starting the menu system
    menuFacade.start()
