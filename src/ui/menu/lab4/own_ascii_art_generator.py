from service.lab4.data_processors import TxtProcessor
from shared.color_processor import ColorProcessor
from shared.file_processors import FileProcessor
from shared.json_utility import read_json_file
from ui.menu_builder import Menu


class OwnAsciiArtGeneratorMenu(Menu):

    def run(self):
        try:
            json_output_data = read_json_file(file_path="../../configuration/paths_config.json")
            initial_text = str(input("Enter text in order to display: "))
            ColorProcessor.display_colors()
            color_position = int(input("Enter position of color you would like to use: "))
            width = int(input("Enter width of text you would like to display: "))
            txt_processor = TxtProcessor(json_output_data["OWN_ASCII_ART_GENERATOR_OUTPUT_FONT"])
            text = txt_processor.retrieve(initial_text, color_position, width)
            print(text)
            FileProcessor.write_into_file(json_output_data["ASCII_ART_GENERATOR_OUTPUT"], text)
        except KeyError:
            print("Key error! You have entered a wrong value for key of colors, "
                  "or symbols are absent in the file which contains alphabet")
        except ValueError as e:
            print(e)
        except FileNotFoundError:
            print("File not found! Please, check the path to the file")


