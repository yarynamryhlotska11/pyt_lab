"""
Module docstring for service.lab8.diagrams_service

This module provides a service for creating various diagrams based on user data
using the `matplotlib` library.

Classes:
- DiagramService: Abstract base class for creating diagrams based on user data.
- DiagramServiceImpl: Implementation class for creating diagrams based on user data.
"""
import json
import pandas as pd

from configuration.logger_config import logger

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


class FileProcessor:
    """
    Class FileProcessor interacts with files. It is used for reading and writing
    """

    @staticmethod
    def write_into_file(file_path: str, text: str) -> None:
        """
        Write text into a file. May raise PermissionError or OSError.
        """
        with open(file_path, "w", encoding="utf-8") as file:
            logger.info("Writing into file %s", file_path)
            file.write(text)

    @staticmethod
    def read_from_file(file_path: str) -> str:
        """
            Read text from a file. May raise FileNotFoundError, PermissionError, or OSError.
        """
        with open(file_path, "r", encoding="utf-8") as file:
            logger.info("Reading from file %s", file_path)
            return file.read()

    @staticmethod
    def read_from_json(file_path: str) -> dict:
        """
        Read a JSON file. May raise FileNotFoundError, PermissionError, or OSError.
        """
        with open(file_path, "r", encoding="utf-8") as file:
            logger.info("Writing into file %s", file_path)
            return json.load(file)

    @staticmethod
    def write_into_json(file_path: str, jsons: list) -> None:
        """
        Write a JSON text into a file.
        """
        if not isinstance(file_path, str):
            logger.critical("Wrong data type: %s. It has to be string!", type(file_path))
            raise TypeError("Type of file_path must be string")

        jsons_text_representation = json.dumps(jsons, indent=4)
        json.loads(jsons_text_representation)

        with open(file_path, "w", encoding="utf-8") as file:
            logger.info("Writing into file %s", file_path)
            file.write(jsons_text_representation)

    @staticmethod
    def write_into_csv(file_path: str, data: dict) -> None:
        fieldnames = data.keys()
        filtered_fieldnames = [field for field in fieldnames if type(field) != dict or type(field) != list]

        values = data.values()


class CsvProcessor:
    """
    CsvProcessor is used to interact with csv-files
    """

    @staticmethod
    def read(file_path: str) -> pd.DataFrame:
        """
        Read a CSV file into a pandas DataFrame. May raise FileNotFoundError,
        """
        if not isinstance(file_path, str):
            logger.critical("Wrong data type: %s. It has to be string!",
                            type(file_path))
            raise TypeError("Type of file_path must be string")
        return pd.read_csv(file_path)
