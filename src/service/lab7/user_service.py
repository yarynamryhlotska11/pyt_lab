import json

import requests
from prettytable import PrettyTable
import regex
from configuration.logger_config import logger
from shared.json_utility import read_json_file


class UserService:

    @staticmethod
    def get_personal_profile(linkedin_url: str):
        if linkedin_url is None or not isinstance(linkedin_url, str):
            raise ValueError("URL has to be a string and nonempty!")
        if regex.match("^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b(["
                       "-a-zA-Z0-9@:%._\\+~#?&//=]*)$", linkedin_url) is None:
            raise ValueError("URL doesn't match the pattern!")
        querystring = {"linkedin_url": linkedin_url, "include_skills": "false"}

        data = read_json_file(file_path="./configuration/urls_config.json")
        data_json = read_json_file(file_path="./configuration/credentials_config.json")

        headers = {

            "X-RapidAPI-Key": data_json["X_RAPID_API_KEY"],
            "X-RapidAPI-Host": data_json["X_RAPID_API_HOST"]
        }
        response = requests.get(data["GET_PERSONAL_PROFILE"],
                                headers=headers, params=querystring, timeout=15)
        if response.status_code != 200:
            message: str = response.json()['message']
            logger.error("The status of the response is not 200, it is %s", message)
            raise ValueError(f"Error occurred! {message}")

        return response.json()

    @staticmethod
    def get_profiles_posts(linkedin_url: str):
        if linkedin_url is None or not isinstance(linkedin_url, str):
            raise ValueError("URL has to be a string and nonempty!")
        if regex.match("^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b(["
                       "-a-zA-Z0-9@:%._\\+~#?&//=]*)$", linkedin_url) is None:
            raise ValueError("URL doesn't match the pattern!")

        querystring = {"linkedin_url": linkedin_url, "type": "posts"}

        data = read_json_file(file_path="./configuration/urls_config.json")
        data_json = read_json_file(file_path="./configuration/credentials_config.json")
        headers = {
            "X-RapidAPI-Key": data_json["X_RAPID_API_KEY"],
            "X-RapidAPI-Host": data_json["X_RAPID_API_HOST"]
        }
        response = requests.get(data["GET_PROFILES_PHOTO"], headers=headers,
                                params=querystring, timeout=15)

        if response.status_code != 200:
            message: str = response.json()['message']
            logger.info("The status of the response is not 200, it is %s", message)
            raise ValueError(f"Error occurred! {message}")

        return response.json()


class DisplayInTableService:
    @staticmethod
    def display_personal_profile(json_data: str):
        data = json.loads(json_data)
        is_experiences = False
        is_educations = False

        # Create an outer PrettyTable
        outer_table = PrettyTable()
        outer_table.field_names = ["Attribute", "Value"]

        # Add simple attributes to the outer table
        for key, value in data['data'].items():
            if key not in ['educations', 'experiences']:
                outer_table.add_row([key, value])

        # Create an inner PrettyTable for educations if present
        if 'educations' in data['data']:
            inner_educations_table = PrettyTable()
            inner_educations_table.field_names = ["School", "Degree", "Date Range"]

            # Add educations to the inner table
            for education in data['data']['educations']:
                is_educations = True
                inner_educations_table.add_row(
                    [education.get('school', ''), education.get('degree', ''),
                     education.get('date_range', '')])

            if is_educations:
                outer_table.add_row(["Educations", inner_educations_table.get_string()])

        # Create an inner PrettyTable for experiences if present
        if 'experiences' in data['data']:
            inner_experiences_table = PrettyTable()
            inner_experiences_table.field_names = ["Company", "Title", "Duration"]

            # Add experiences to the inner table
            for experience in data['data']['experiences']:
                inner_experiences_table.add_row([experience.get('company', ''),
                                                 experience.get('title', ''),
                                                 experience.get('duration', '')])

            if is_experiences:
                outer_table.add_row(["Experiences", inner_experiences_table.get_string()])

        return outer_table.get_string()

    @staticmethod
    def display_profiles_posts(json_data: str, result=""):
        data = json.loads(json_data)

        outer_table = PrettyTable()
        outer_table.field_names = ["Attribute", "Value"]

        # Create a table for each post
        for post in data['data']:
            post_table = PrettyTable()
            post_table.field_names = ["Attribute", "Value"]

            for key, value in post.items():
                if isinstance(value, str) and len(value) > 50:
                    # Truncate long strings for better display
                    value = value[:50] + '...'

                post_table.add_row([key, value])

            result += "\nPost:\n"
            result += post_table.get_string()
        return result
