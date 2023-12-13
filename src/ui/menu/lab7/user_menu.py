import json

from service.lab7.user_service import DisplayInTableService, UserService
from shared.color_processor import ColorProcessor
from shared.file_processors import FileProcessor
from shared.json_processor import JSONProcessor
from shared.json_utility import read_json_file
from ui.menu_builder import Menu


class UserMenu(Menu):

    def run(self):
        history: list = []
        successful_result: bool = False
        jsons: list = []

        while True:
            print("Choose an option:")
            print("1. Display data of a personal profile")
            print("2. Display data of profiles posts")
            print("3. Save data in JSON format")
            print("4 - Show history")
            print("0 - Exit")

            option = input("Your choice: ")
            if option == "1":
                jsons = []
                linkedin_url = input("Enter LinkedIn URL: ")
                try:
                    jsons = UserService.get_personal_profile(linkedin_url)
                    print("Choose an option:")
                    print("1. Display data in a flattened way")
                    print("2. Display data in JSON format")
                    print("3. Display data in a table")
                    while True:
                        option = input("Your choice: ")
                        if option == "1":
                            ColorProcessor.display_colors()
                            color_position = int(input("Enter a color position: "))
                            JSONProcessor.display_flattened_json(jsons, color_position)
                            break
                        elif option == "2":
                            print(json.dumps(jsons, indent=4))
                            break
                        elif option == "3":
                            print(DisplayInTableService.display_personal_profile(
                                json.dumps(jsons, indent=4)))
                            break
                        else:
                            print("Invalid option. Enter again!")
                    history.append(
                        f"Data of a personal profile where URL is "
                        f"{linkedin_url}:\n{json.dumps(jsons, indent=4)}")
                    successful_result = True
                except ValueError as e:
                    print(e)
                    successful_result = False

            elif option == "2":
                jsons = []
                linkedin_url = input("Enter LinkedIn URL: ")
                try:
                    jsons = UserService.get_profiles_posts(linkedin_url)
                    print("Choose an option:")
                    print("1. Display data in a flattened way")
                    print("2. Display data in JSON format")
                    print("3. Display data in a table")
                    while True:
                        option = input("Your choice: ")
                        if option == "1":
                            ColorProcessor.display_colors()
                            color_position = int(input("Enter a color position: "))
                            JSONProcessor.display_flattened_json(jsons, color_position)
                            break
                        elif option == "2":
                            print(json.dumps(jsons, indent=4))
                            break
                        elif option == "3":
                            print(DisplayInTableService.display_profiles_posts(
                                json.dumps(jsons, indent=4)))
                            break
                        else:
                            print("Invalid option. Enter again!")
                    history.append(
                        f"Data of a personal profile where URL is "
                        f"{linkedin_url}:\n{json.dumps(jsons, indent=4)}")
                    successful_result = True
                except ValueError as e:
                    print(e)
                    successful_result = False
            elif option == "3":
                if successful_result:
                    try:
                        json_data = read_json_file(file_path="../../configuration/paths_config.json")
                        FileProcessor.write_into_json(json_data["JSON_FILE_PATH"], jsons)
                    except Exception as e:
                        (
                            print(e))
                else:
                    print("No data to save!")
            elif option == "4":
                if len(history) == 0:
                    print("No history!")
                else:
                    for counter, item in enumerate(history):
                        print(f"{counter + 1}: {item}")
            elif option == "0":
                break
            else:
                print("Invalid option. Enter again!")
