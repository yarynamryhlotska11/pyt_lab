def load_ascii_art(file_path):
    ascii_dict = {}
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read().strip().split('@symbol::')
        for item in content[0:]:
            symbol, *lines = item.split('\n')
            ascii_dict[symbol] = [line.strip('^$') for line in lines[0:]]
    return ascii_dict


def select_color():
    color_choice = input("Select text color (white, gray): ").lower()
    if color_choice in ['white', 'gray']:
        return color_choice
    else:
        return None


def apply_color(text, color):
    color_codes = {'white': '\u001b[97m', 'gray': '\u001b[90m'}
    reset_color = '\u001b[0m'
    return color_codes[color] + text + reset_color


def get_valid_text(ascii_dict):
    while True:
        text = input("Enter a word or phrase: ")
        if all(c in ascii_dict or c == ' ' for c in text):
            return text
        else:
            print("Error. The input contains invalid characters. Please enter a valid phrase.")


def print_ascii_art(ascii_dict, text, alignment, max_width, symbol_set, color):
    output_lines = [""] * 6

    for symbol in text:
        if symbol == ' ':
            for i in range(6):
                output_lines[i] += ' '
        elif symbol in ascii_dict:
            symbol_lines = ascii_dict[symbol]
            for i in range(6):
                output_lines[i] += symbol_lines[i]

    if len(output_lines[0]) > max_width:
        raise ValueError("Error. Maximum width is too small for the input phrase.")

    if alignment == 'center':
        output_lines = [line.center(max_width) for line in output_lines]
    elif alignment == 'right':
        output_lines = [line.rjust(max_width) for line in output_lines]

    colored_output_lines = [apply_color(line, color) for line in output_lines]

    for line in colored_output_lines:
        print(line)

    return output_lines


def save_to_text_file(output_lines, output_file_name):
    with open(output_file_name, 'w') as file:
        for line in output_lines:
            file.write(line + '\n')
