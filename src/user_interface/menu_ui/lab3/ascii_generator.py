"""
Description:
This module implements a user interface menu for an ASCII art generator. It includes the 'AsciiArtGeneratorMenu' class,
facilitating interactions for generating ASCII art based on user-input text.

Example Usage:
```python
# Initialize and run the ASCII art generator menu
ascii_art_menu = AsciiArtGeneratorMenu()
ascii_art_menu.run()
"""
from service.lab3.ascii_generator_service import AsciiArtGeneratorService
from user_interface.menu_builder import Menu


class AsciiArtGeneratorMenu(Menu):
    """Menu for an ASCII art generator."""

    def run(self):
        """Run the ASCII art generator."""
        ascii_art_generator_service = AsciiArtGeneratorService()
        ascii_art_generator_service.display_text()
