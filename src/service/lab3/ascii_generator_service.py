"""
The `pyfiglet` module provides ASCII art text generation functionality, while the `colorama` module enables
cross-platform colored terminal text output in Python.

The `AsciiArtGeneratorService` class facilitates the creation and display of ASCII art text based on user input for
phrase or word, font selection, text color, and width.
Methods:
- __init__(self): Initializes an instance of AsciiArtGeneratorService with a FileProcessor object.
- __get_text(text, font, color_position, width) -> str: Generates ASCII art text based on the provided input text, font,
 color position, and width.
- display_text(self): Allows the user to input a phrase or word, select a font, choose a text color, specify text width,
 generates and displays the ASCII art text, and writes it to a file.

Example:
       .'|
     .'  |
     |   |
___  |   |
`._|=|__.
"""

import pyfiglet
from colorama import Fore
from shared.color_font_processor import colors, fonts, FontProcessor, ColorProcessor
from shared.file_processors import FileProcessor
from shared.json_utility import read_json_file


class AsciiArtGeneratorService:
    def __init__(self):
        self.__file_processor = FileProcessor()

    @staticmethod
    def __get_text(text, font, color_position, width) -> str:
        fig = pyfiglet.Figlet(font)
        fig.width = width
        formatted_text = fig.renderText(text)
        return getattr(Fore, colors[color_position]) + formatted_text

    def display_text(self):
        while True:
            try:
                initial_text = str(input("Enter a phrase or word for asci art: "))
                if not initial_text.isascii():
                    print("Text must contain only ASCII characters")
                    continue
                FontProcessor.display_fonts()
                font_position = int(input("Enter font position you want to use: "))
                ColorProcessor.display_colors()
                color_position = int(input("Enter color position you want to use: "))
                width = int(input("Enter text width you want to display: "))
                modified_text = self.__get_text(initial_text, fonts[font_position], color_position, width)
                print(modified_text)
                json_data = read_json_file(file_path="../src/configuration/paths_config.json")
                self.__file_processor.write_into_file(json_data["ASCII_ART_GENERATOR"], modified_text)

                if input(
                        "Would you like to continue? Enter 'y' if you do. Your response is ").lower() != "y":
                    break
            except ValueError:
                print("Cannot be parsed into an int value")
            except KeyError:
                print("You have entered a wrong value for the key of fonts or color")
            except pyfiglet.CharNotPrinted as e:
                print(str(e))
