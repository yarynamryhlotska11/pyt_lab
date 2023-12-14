"""
Module: user_interface.menu.lab5.figures_generator
A module for handling 3D figures and their representations.
Classes:
- FigureMenu: A menu class for managing 3D figures and their representations.
"""
from service.lab5.generate_figures_service import Figure3D, Cube
from shared.color_font_processor import colors, ColorProcessor
from shared.file_processors import FileProcessor
from shared.json_utility import read_json_file
from user_interface.menu_builder import Menu


class FigureMenu(Menu):
    """Menu class for managing 3D figures and their representations."""

    def __init__(self):
        """
        Initialize FigureMenu class.
        Initializes various flags and variables for figure and representation availability.
        Retrieves file paths for 2D and 3D representations from paths_config.json.
        """
        self.__is_figure_available = False
        self.__is_2d_representation_available = False
        self.__is_3d_representation_available = False
        self.__figure = None

        # Retrieving file paths for 2D and 3D representations from paths_config.json
        json_data = read_json_file(file_path="../src/configuration/paths_config.json")
        self.__representation_2d_file = json_data["FIGURE_2D"]
        self.__representation_3d_file = json_data["FIGURE_3D"]

    # Helper methods for user input validation
    @staticmethod
    def __get_character_input():
        while True:
            character = input("Enter a character to represent in the shape: ")
            if Figure3D.is_appropriate_character(character) is False:
                print("You should have entered one character!")
            else:
                return character

    @staticmethod
    def __get_color_position_input():
        while True:
            try:
                color = int(input("Enter a number of color: "))
                if color not in range(len(colors)):
                    print("You should have entered a color option which is available!")
                else:
                    return color
            except ValueError:
                print("You should have entered an integer number!")

    @staticmethod
    def __get_length_input():
        while True:
            try:
                length = int(input("Enter a length: "))
                if length <= 0:
                    print("You should have entered a length greater than 0!")
                else:
                    return length
            except ValueError:
                print("You should have entered an integer number!")

    @staticmethod
    def __get_scale_input():
        while True:
            try:
                scale = float(input("Enter a scale for figure: "))
                if scale <= 0:
                    print("You should have entered a scale greater than 0!")
                else:
                    return scale
            except ValueError:
                print("You should have entered a float number!")

    def __create_cube(self):
        character = self.__get_character_input()
        print("There are such colors available:")
        ColorProcessor.display_colors()
        color_position = self.__get_color_position_input()
        length = self.__get_length_input()
        try:
            self.__figure = Cube(length, character, color_position)
            self.__is_figure_available = True  # Set flag if cube creation is successful
        except ValueError as e:
            print(e)
            self.__is_figure_available = False  # Set flag if cube creation fails

    def __display_2d(self):
        """Display the 2D representation of the figure."""
        if self.__is_figure_available is True:
            representation_2d = self.__figure.get_2d_representation()
            for item in representation_2d:
                print(item)
            self.__is_2d_representation_available = True
        else:
            print("There is no figure available!")

    def __display_3d(self):
        """
        Display the 3D representation of the figure.
        If a figure is available, this method retrieves and prints its 3D representation based on the given scale.
        """
        if self.__is_figure_available is True:
            representation_3d = self.__figure.get_3d_representation(scale=self.__get_scale_input())
            print(representation_3d)
            self.__is_3d_representation_available = True
        else:
            print("There is no figure available!")

    def __save_2d_representation(self):
        """
        Save the 2D representation of the figure to a file.
        If a 2D representation is available, it attempts to save it to the specified file path.
        """
        if self.__is_2d_representation_available is True:
            try:
                FileProcessor.write_into_file(self.__representation_2d_file, ""
                                              .join(self.__figure.get_2d_representation()))
            except PermissionError:
                print("You do not have permission to write to the file!")
            except FileNotFoundError:
                print("The file does not exist!")
        else:
            print("There is no figure available!")

    def __save_3d_representation(self):
        """
        Save the 3D representation of the figure to a file.
        If a 3D representation is available, it attempts to save it to the specified file path based on the given scale.
        """
        if self.__is_3d_representation_available is True:
            try:
                FileProcessor.write_into_file(
                    self.__representation_3d_file,
                    self.__figure.get_3d_representation(scale=self.__get_scale_input()))
            except PermissionError:
                print("You do not have permission to write to the file!")
            except FileNotFoundError:
                print("The file does not exist!")
        else:
            print("There is no figure available!")

    def run(self):
        while True:
            print("1 - Create figure")
            print("2 - Display figure in 2D")
            print("3 - Display figure in 3D")
            print("4 - Save figure in 2D")
            print("5 - Save figure in 3D")
            print("0 - Exit")
            option = str(input("Enter an option: "))

            if option == "1":
                self.__create_cube()
            elif option == "2":
                self.__display_2d()
            elif option == "3":
                self.__display_3d()
            elif option == "4":
                self.__save_2d_representation()
            elif option == "5":
                self.__save_3d_representation()
            elif option == "0":
                break
            else:
                print("Invalid option!")  # Inform users about invalid inputs
