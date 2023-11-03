from colorama import Fore, init
init(autoreset=True)

colors = {
    1: 'WHITE',
    2: 'RED',
    3: 'BLUE',
    4: 'YELLOW',
    5: 'GREEN',
    6: 'MAGENTA'
}


class RectangleArt:
    def __init__(self, width, height, outer_color='BLUE', middle_color='MAGENTA', inner_color='RED', symbol_count=1, symbol_color='*'):
        if width < 1 or height < 1:
            print("Error: Rectangle dimensions are less than 1.")
        else:
            self.width = width
            self.height = height
            self.outer_rectangle_color = outer_color if outer_color in colors.values() else 'BLUE'
            self.middle_rectangle_color = middle_color if middle_color in colors.values() else 'MAGENTA'
            self.inner_rectangle_color = inner_color if inner_color in colors.values() else 'RED'
            self.symbol_count = symbol_count
            self.symbol_color = symbol_color
            self.outer_rectangle = self.generate_outer_rectangle()
            self.middle_rectangles = self.generate_middle_rectangles()
            self.inner_rectangle = self.generate_inner_rectangle()

    def set_outer_rectangle_color(self, color):
        self.outer_rectangle_color = color

    def set_middle_rectangle_color(self, color):
        self.middle_rectangle_color = color

    def set_inner_rectangle_color(self, color):
        self.inner_rectangle_color = color

    def generate_outer_rectangle(self):
        rectangle = [[Fore.WHITE + ' ' for _ in range(self.width)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                if j == 0 or i == 0:
                    rectangle[i][j] = getattr(Fore, self.outer_rectangle_color) + '*'
        return rectangle

    def generate_middle_rectangles(self):
        middle_rectangles = []
        if self.width > 2 and self.height > 2:
            offset = 1
            for _ in range(self.height // 2 - 1):
                rectangle = [[Fore.WHITE + ' ' for _ in range(self.width)] for _ in range(self.height)]
                for i in range(self.height):
                    for j in range(self.width):
                        if i == 0 and (j == 0 or j == self.width - 1):
                            rectangle[i][j] = getattr(Fore, self.middle_rectangle_color) + '*'
                        elif i == self.height - 1 and j == 0:
                            rectangle[i][j] = getattr(Fore, self.middle_rectangle_color) + '*'
                middle_rectangles.append((rectangle, offset))
                offset += 1
        return middle_rectangles

    def generate_inner_rectangle(self):
        rectangle = [[Fore.WHITE + ' ' for _ in range(self.width)] for _ in range(self.height)]
        if self.width > 2 and self.height > 2:
            offset_right = (self.width // 2) + 3
            offset_down = self.height // 2
            for i in range(self.height):
                for j in range(self.width):
                    if i == 0 or i == self.height - 1 or j == 0 or j == self.width - 1:
                        rectangle[i][j] = getattr(Fore, self.inner_rectangle_color) + '*'
                    if i >= offset_down and i < self.height - offset_down and j >= offset_right and j < self.width - offset_right:
                        rectangle[i][j] = ' '
        return rectangle

    def resize_matrix(self, matrix):
        for row in matrix:
            row.extend([Fore.WHITE + ' '] * (self.width * 3 - 1))

    def combine_rectangles(self):
        combined_width = int((((self.width + self.height) / 2) + self.width) * 3)
        combined_height = int(((self.height + self.width) / 2) + self.height)

        combined_matrix = [[Fore.WHITE + ' ' for _ in range(combined_width)] for _ in range(combined_height)]

        for i in range(self.height):
            for j in range(self.width):
                combined_matrix[i][int(j * 3)] = self.outer_rectangle[i][j]

        middle_offset = 0
        for middle_rectangle, offset in self.middle_rectangles:
            for i in range(self.height):
                for j in range(self.width):
                    combined_matrix[i + offset][int(j * 3) + offset] = middle_rectangle[i][j]
                middle_offset = offset

        inner_offset = middle_offset + 1
        for i in range(self.height):
            for j in range(self.width):
                combined_matrix[i + inner_offset][int(j * 3) + inner_offset] = self.inner_rectangle[i][j]

        return combined_matrix

    def draw_combined_rectangles(self):
        combined_matrix = self.combine_rectangles()
        for row in combined_matrix:
            print(''.join(row))

    def draw_inner_rectangle(self):
        for row in self.inner_rectangle:
            print(''.join(row))

    def draw_middle_rectangles(self):
        for middle_rectangle, _ in self.middle_rectangles:
            for row in middle_rectangle:
                print(''.join(row))

    def draw_outer_rectangle(self):
        for row in self.outer_rectangle:
            print(''.join(row))

    def convert_to_2d(self):
        print("Converting 3D art to 2D...")
        for row in self.inner_rectangle:
            print('  '.join(row))

    def scale_figure(self, scale_factor):
        if scale_factor <= 0:
            print("Error: Scale factor should be a positive number.")
            return

        self.width = int(self.width * scale_factor)
        self.height = int(self.height * scale_factor)

        self.outer_rectangle = self.generate_outer_rectangle()
        self.middle_rectangles = self.generate_middle_rectangles()
        self.inner_rectangle = self.generate_inner_rectangle()

    def reverse_scale_figure(self, scale_factor):
        if scale_factor <= 0:
            print("Error: Scale factor should be a positive number.")
            return

        new_width = int(self.width / scale_factor)
        new_height = int(self.height / scale_factor)

        if new_width < 3 or new_height < 3:
            print("It is not possible to reduce the figure to dimensions smaller than 3x3.")
            return

        self.width = new_width
        self.height = new_height

        self.outer_rectangle = self.generate_outer_rectangle()
        self.middle_rectangles = self.generate_middle_rectangles()
        self.inner_rectangle = self.generate_inner_rectangle()

    def align_art(self, alignment, console_length):
        combined_matrix = self.combine_rectangles()
        max_length = max(len("".join(row)) for row in combined_matrix)

        if alignment == 'center':
            for row in combined_matrix:
                print(f"{(''.join(row)).center(console_length)}")
        elif alignment == 'right':
            for row in combined_matrix:
                print(f"{(''.join(row)).rjust(console_length)}")
        elif alignment == 'left':
            for row in combined_matrix:
                print(f"{(''.join(row)).ljust(console_length)}")

    def save_to_file(self, file_name):
        combined_matrix = self.combine_rectangles()
        with open(file_name, 'w') as f:
            for row in combined_matrix:
                row = ''.join(
                    map(lambda x: x.replace(Fore.WHITE, '').replace(Fore.RED, '').replace(Fore.BLUE, '').replace(
                        Fore.YELLOW, '').replace(Fore.GREEN, '').replace(Fore.MAGENTA, ''), row))
                f.write(row + '\n')
        print(f"ASCII art is saved to a file {file_name}.")


