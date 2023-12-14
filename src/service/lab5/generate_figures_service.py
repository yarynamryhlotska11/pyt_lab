"""
The `abc` module provides functionality for Abstract Base Classes, while the `colorama` module enables cross-platform
colored terminal text output in Python.

The `Figure3D` class represents an abstract base class for 3D figures and defines abstract methods for obtaining 2D and
3D representations of the figure.
The `Cube` class represents a specific 3D figure, inheriting from the Figure3D abstract base class.

Example:
         2  2  2  2  2  2
      2              2  2
   2              2     2
2  2  2  2  2  2        2
2              2        2
2              2        2
2              2     2
2              2  2
2  2  2  2  2  2
"""
from abc import ABC, abstractmethod
from colorama import Fore
from shared.color_font_processor import colors


class Figure3D(ABC):

    def __init__(self, character: str, color_position: int):
        if not colors.__contains__(color_position):
            raise ValueError("Position color have to be in range of available colors")
        if self.is_appropriate_character(character) is False:
            raise ValueError("It supposed to be only one character instead")
        self._character = character
        self._color_position = color_position

    @abstractmethod
    def get_2d_representation(self) -> list:

        pass

    @abstractmethod
    def get_3d_representation(self) -> str:

        pass

    @staticmethod
    def is_appropriate_character(character: str) -> bool:

        return len(character) == 1


class Cube(Figure3D):

    def __init__(self, length: int, character: str, color_position: int):
        if length <= 0:
            raise ValueError("Length must be greater than 0")
        super().__init__(character, color_position)
        self.__length = length

    def get_2d_representation(self) -> list:

        result = ""
        for row in range(self.__length):
            for col in range(self.__length):
                if row == 0 or row == self.__length - 1:
                    result += f"{self._character}  "
                elif col == 0 or col == self.__length - 1:
                    result += f"{self._character}  "
                else:
                    result += "   "
            result += "\n"

        return [getattr(Fore, colors[self._color_position]) + "\n" + result for _ in range(6)]

    def get_3d_representation(self, scale: float = 1.0) -> str:

        modified_length = int(self.__length * scale) \
            if self.__length * scale >= 2 else self.__length
        modified_offset = int(modified_length / 2 + 1)
        result = ""

        for row in range(modified_offset - 1):
            for col in range(modified_length + modified_offset - 1):
                if (row + col == modified_offset - 1) or (row == 0 and col > modified_offset - 1):
                    result += f"{self._character}" + (
                        "" if col == modified_length + modified_offset - 2 and row == 0 else "  ")
                elif modified_length + modified_offset - row == col + 2:
                    result += f"{self._character}"
                elif col == modified_length + modified_offset - 2:
                    result += f"  {self._character}"
                else:
                    result += "   "
            result += "\n"

        for row in range(modified_length):
            for col in range(modified_length + modified_offset):
                if ((row == 0 or row == modified_length - 1) and col < modified_length or (
                        col == 0 or col == modified_length - 1) and
                        row < modified_length and col < modified_length):
                    result += f"{self._character}" + (
                        "" if row == modified_length - 1
                              and col == modified_length - 1 else "  ")
                elif (row + col == (modified_length - 1) * 2 and col < modified_length
                      + modified_offset - 1):
                    result += "   " * (modified_length - row - 2) + f"{self._character}"
                elif col < modified_length and row < modified_length:
                    result += "   "
                elif row < modified_length - modified_offset and col > modified_length:
                    if col == modified_offset + modified_length - 1:
                        result += f"{self._character}"
                    else:
                        result += "   "

            result += "\n"

        return getattr(Fore, colors[self._color_position]) + "\n" + result
