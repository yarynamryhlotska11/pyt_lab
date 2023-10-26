import pyfiglet  # Import the library to generate ASCII-Art
from colorama import Fore  # Import for Color Leaning Text

# Creating a vocabulary with all the fonts available
fonts = dict(enumerate(sorted(pyfiglet.FigletFont.getFonts())))
# Creating a vocabulary with some colors for the text
colors = {
    1: 'WHITE',
    2: 'RED',
    3: 'BLUE',
    4: 'YELLOW',
    5: 'GREEN',
    6: 'MAGENTA'
}


# Function to output all the fonts available
def display_fonts() -> None:
    for i in fonts:
        print(str(i) + ". " + fonts[i])


# Function to output all colors available
def display_colors() -> None:
    for i in colors:
        print(str(i) + ". " + colors[i])


# Function to generates ASCII-Art from the text entered
def get_text(text, font, color_position, width) -> str:
    fig = pyfiglet.Figlet(font)
    fig.width = width
    formatted_text = fig.renderText(text)
    return getattr(Fore, colors[color_position]) + formatted_text


# Function to write text in file
def write_in_file(file_path, text) -> None:
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)

