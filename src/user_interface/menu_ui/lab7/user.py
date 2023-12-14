"""
Module: UserMenu

This module defines a menu class for interacting with user data. It includes options to display
personal profile data, display profiles posts, save data in JSON format, show history, and exit.

Classes:
- UserMenu: A menu class for interacting with user data.
"""
import json

from service.lab7.user_service import DisplayInTableService, UserService
from shared.file_processors import FileProcessor
from shared.json_utility import read_json_file
from user_interface.menu_builder import Menu


class UserMenu(Menu):
    """Menu class for managing user data operations.

    This class presents a menu system to perform operations related to user data. It interacts
    with the UserService and DisplayInTableService classes to retrieve user data, display it in
    different formats (table or JSON), and save the data as JSON files.

    Attributes: None

    Methods:
        run(): Runs the menu system to manage user data operations.
    """
    def run(self):
        """Run the menu system for managing user data operations."""
        history: list = []  # List to store history of performed operations
        successful_result: bool = False  # Flag to track successful retrieval of user data
        jsons: list = []  # List to store retrieved JSON data

        while True:
            print("Choose an option:")
            print("1. Display data of a personal profile")
            print("2. Save data")
            print("0 - Exit")

            option = input("Your choice: ")
            if option == "1":
                jsons = []
                username = input("Enter username: ")
                try:
                    jsons = UserService.get_personal_profile(username)
                    print("Choose an option:")
                    print("1. Display data in a table")
                    print("2. Display data in JSON format")
                    while True:
                        option = input("Your choice: ")
                        if option == "1":
                            user_profile_info = DisplayInTableService.display_personal_profile(json.dumps(jsons))
                            print(user_profile_info)
                            history.append("Data of a personal profile where username is")
                            successful_result = True
                            break
                        elif option == "2":
                            print(json.dumps(jsons, indent=4))
                            history.append("Data of a personal profile where username is")
                            successful_result = True
                            break
                        else:
                            print("Invalid option. Enter again!")
                except ValueError as e:
                    print(e)
                    successful_result = False  # Mark unsuccessful result

            elif option == "2":
                if history.__len__() > 0 and successful_result:
                    FileProcessor.write_into_json("../src/data/lab7/result.json", jsons)
                else:
                    print("No data to save!")
            elif option == "3":
                if successful_result:  # Check if data is available to save
                    try:
                        json_data = read_json_file(file_path="../src/configuration/paths_config.json")
                        FileProcessor.write_into_json(json_data["JSON_FILE_PATH"], jsons)
                    except Exception as e:
                        print(e)
                else:
                    print("No data to save!")
            elif option == "0":
                break  # Exit the menu system
            else:
                print("Invalid option. Enter again!")   # Inform users about invalid inputs
