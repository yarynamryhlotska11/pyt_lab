from colorama import Fore
from service import (UserService as user_service, DisplayOnTable)
import json

from src.utility import FileProcessor


def main():
    json_file_path = "./files/result.json"
    history: list = []
    successful_result: bool = False
    jsons: dict = {}
    user_profile_info = None

    while True:
        print("Choose an option:")
        print("1. Display data of a personal profile")
        print("2 - Show history")
        print("3 - Save data into a file")
        print("0 - Exit")

        option = input("Your choice: ")
        if option == "1":
            username = input("Enter username: ")
            try:
                jsons = user_service.get_personal_profile(username)
                print("Choose an option:")
                print("1. Display data in a table")
                print("2. Display data in JSON format")
                while True:
                    option = input("Your choice: ")
                    if option == "1":
                        jsons = user_service.get_personal_profile(username)
                        user_profile_info = DisplayOnTable.display_profile(json.dumps(jsons))
                        print(user_profile_info)
                        history.append(
                            f"Data of a personal profile where username is {username}:\n{user_profile_info}")
                        successful_result = True
                        break
                    elif option == "2":
                        jsons = user_service.get_personal_profile(username)
                        user_profile_info = json.dumps(jsons, indent=4)
                        print(user_profile_info)
                        history.append(
                            f"Data of a personal profile where username is {username}:\n{user_profile_info}")
                        successful_result = True
                        break
                    else :
                        print("Invalid option. Enter again!")
            except ValueError as e:(
                print(e))
            successful_result = False

        elif option == "2":
            if len(history) == 0:
                print("No history!")
            else:
                for counter, item in enumerate(history):
                    print(f"{counter + 1}: {item}")
        elif option == "3":
            if history.__len__() > 0 and successful_result:
                print("Choose an option in order to save into a file:")
                print("1. Save into a txt file")
                print("2. Save into a jsons file")
                print("3. Save into a csv file")
                inner_option = input("Your choice: ")
                if inner_option == "1":
                    FileProcessor.write_into_file("./files/result.txt", user_profile_info)
                elif inner_option == "2":
                    FileProcessor.write_into_json(json_file_path, jsons)
                elif inner_option == "3":
                    FileProcessor.write_into_csv("./files/result.csv", jsons)
                else:
                    print("No data to save!")
        elif option == "0":
            exit(0)
        else:
            print("Invalid option. Enter again!")


if __name__ == '__main__':
    main()
