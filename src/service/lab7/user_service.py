"""
The `json` module provides functionality for encoding and decoding JSON data, while the `requests` module allows sending
 HTTP requests. `prettytable` facilitates creating visually appealing ASCII tables. `regex` is used for regular
 expression matching. Other modules contain configurations, logging setups, and shared utilities.

The `UserService` class interacts with an external API to fetch personal profile data based on a given username.
The `DisplayInTableService` class formats personal profile data into a visually organized table using the `
PrettyTable` library.
"""
import json

import requests
from prettytable import PrettyTable
import regex
from configuration.logger_config import logger
from shared.json_utility import read_json_file


class UserService:

    def get_personal_profile(username: str):
        if username is None or not isinstance(username, str) or not regex.match("^[\w](?!.*?\.{2})[\w.]{1,28}[\w]$",
                                                                          username):
            raise ValueError(
                "Username is supposed to be a string, or it has an incorrect value according to the rules!")
        querystring = {"username": username}

        data = read_json_file(file_path="./configuration/urls_config.json")
        data_json = read_json_file(file_path="./configuration/credentials_config.json")

        headers = {

            "X-RapidAPI-Key": data_json["X_RAPID_API_KEY"],
            "X-RapidAPI-Host": data_json["X_RAPID_API_HOST"]
        }
        response = requests.get(data["GET_PERSONAL_PROFILE"],
                                headers=headers, params=querystring)
        if response.status_code != 200:
            message: str = response.json()['message']
            logger.error("The status of the response is not 200", message)
            raise ValueError(f"Error occurred! {message}")

        return response.json()


class DisplayInTableService:
    def display_personal_profile(json_data: str):
        data = json.loads(json_data)
        outer_table = PrettyTable()
        outer_table.field_names = ["Attribute", "Value"]

        for key, value in data.items():
            if key in {"id", "biography", "full_name", "is_business_account", "category_name", "is_private",
                       "username"}:
                outer_table.add_row([key, value])

        return outer_table.get_string()
