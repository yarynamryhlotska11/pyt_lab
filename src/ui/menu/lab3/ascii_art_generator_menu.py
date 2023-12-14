from service.lab3.ascii_art_generator_service import AsciiArtGeneratorService
from ui.menu_builder import Menu


class AsciiArtGeneratorMenu(Menu):

    def run(self):
        ascii_art_generator_service = AsciiArtGeneratorService()
        ascii_art_generator_service.display_text()
