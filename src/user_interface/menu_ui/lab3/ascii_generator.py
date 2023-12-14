"""
Module docstring for user_interface.menu.lab3.ascii_generator

Module for implementing a simple menu for an ASCII art generator.

This module contains the `AsciiArtGeneratorMenu` class, providing a menu for an ASCII art generator.
Users can run the program to generate ASCII art based on the provided text.
"""
from service.lab3.ascii_generator_service import AsciiArtGeneratorService
from user_interface.menu_builder import Menu


class AsciiArtGeneratorMenu(Menu):
    """Menu for an ASCII art generator."""

    def run(self):
        """
        Run the ASCII art generator.

        Initializes the ASCII art generator service and displays text in ASCII art.
        """
        ascii_art_generator_service = AsciiArtGeneratorService()
        ascii_art_generator_service.display_text()
