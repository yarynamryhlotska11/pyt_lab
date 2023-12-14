import json


def read_json_file(file_path: object) -> object:
    """Reads a JSON file and returns its contents as a dictionary.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            dict: A dictionary containing the data from the JSON file.

        Raises:
            FileNotFoundError: If the specified file path does not exist.
            json.JSONDecodeError: If the file does not contain valid JSON data.

        Example:
            file_path = 'data.json'
            data = read_json_file(file_path)
        """
    with open(file_path, 'r') as file:
        data_dict = json.load(file)
    return data_dict
