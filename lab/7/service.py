import json
import colorama
import pyfiglet
from colorama import Fore
import requests
from prettytable import PrettyTable
import regex
import config as config

colorama.init(autoreset=True)

fonts = dict(enumerate(sorted(pyfiglet.FigletFont.getFonts())))
colors = dict(enumerate(sorted(Fore.__dict__.keys())))


class UserService:

    @staticmethod
    def get_personal_profile(username: str):
        if username is None or not isinstance(username, str) or not regex.match("^[\w](?!.*?\.{2})[\w.]{1,28}[\w]$",
                                                                                username):
            raise ValueError(
                "Username is supposed to be a string, or it has an incorrect value according to the rules!")

        querystring = {"username": username}

        headers = {
            "X-RapidAPI-Key": config.X_RapidAPI_Key,
            "X-RapidAPI-Host": config.X_RapidAPI_Host
        }

        response = requests.get(config.get_personal_profile, headers=headers, params=querystring)
        if response.status_code != 200:
            message: str = response.json().get('message', 'Unknown error occurred!')
            raise ValueError(f"Error occurred! {message}")
        else:
            return response.json()


class DisplayOnTable:
    @staticmethod
    def display_profile(json_data: str):
        data = json.loads(json_data)
        outer_table = PrettyTable()
        outer_table.field_names = ["Attribute", "Value"]
        for key, value in data.items():
            if key in {"id", "biography", "full_name", "is_business_account", "category_name", "is_private", "username"}:
                outer_table.add_row([f"{Fore.GREEN + key + Fore.RESET}", value])

        return outer_table.get_string()
