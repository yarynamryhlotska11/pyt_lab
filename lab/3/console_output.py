import functions

if __name__ == '__main__':
    while True:
        try:
            while True:
                initial_text = str(input("Enter a word or phrase you want to turn into ASCII-Art: "))
                if not initial_text.isascii():
                    print("Error! The text should only contain ASCII characters")
                    continue
                else:
                    break

            while True:
                functions.display_fonts()
                font_position = int(input("Enter the font number you want to use: "))
                if font_position not in functions.fonts:
                    print("Error! Invalid font number. Please enter again.")
                    continue
                else:
                    break

            while True:
                functions.display_colors()
                color_position = int(input("Enter the color number you want to use: "))
                if color_position not in functions.colors:
                    print("Error! Invalid color number. Please enter again.")
                    continue
                else:
                    break


        except ValueError as e:
            print("Error! Please enter a number.")
            continue

        try:
            while True:
                width = int(input("Enter width of the text you want to use: "))
                if width <= 0:
                    print("Width must be a positive value. Please enter a positive value.")
                else:
                    break
        except ValueError as e:
            print("Error! Please enter correct width (It must be number).")
            continue

        modified_text = functions.get_text(initial_text, functions.fonts[font_position], color_position, width)
        print("The result of ASCII art: ")
        print(modified_text)

        save_to_file = input("Save the text in the file? (yes/no): ")
        if save_to_file.lower() == "yes":
            filename = input("Enter the file name to save the text: ")
            functions.write_in_file(filename, modified_text)
            print(f"Text saved in the file {filename}")

        if input(
                "Continue to write? (yes/no): ").lower() == "yes":
            continue
        else:
            break
