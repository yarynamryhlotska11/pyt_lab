import json


def read_json_file(file_path: object) -> object:
    with open(file_path, 'r') as file:
        data_dict = json.load(file)
    return data_dict
