from functions import *

if __name__ == '__main__':
    symbol_set = {
        'standart': "ascii_art.txt",
        '@': "ascii_art_dog.txt",
        '#': "ascii_art_lattice.txt",
        '*': "ascii_art_star.txt",
    }

    while True:
        selected_symbol = input("Select a symbol (standart, @, #, *): ")
        if selected_symbol not in symbol_set:
            print("Error! Invalid symbol.")
            continue

        file_path = symbol_set[selected_symbol]
        ascii_dict = load_ascii_art(file_path)

        while True:
            color = select_color()
            if color is None:
                print("Error! Invalid color choice.")
                continue

            while True:
                text = get_valid_text(ascii_dict)

                while True:
                    alignment = input("Select alignment (left, center, right): ").lower()
                    if alignment not in ['left', 'center', 'right']:
                        print("Error! Invalid alignment.")
                    else:
                        break

                while True:
                    try:
                        max_width = int(input("Enter maximum width: "))
                        if max_width <= 0:
                            print("Error. Maximum width must be a positive integer.")
                        else:
                            break
                    except ValueError as e:
                        print(e)

                while True:
                    try:
                        print("The result of ASCII art:")
                        output_lines = print_ascii_art(ascii_dict, text, alignment, max_width, selected_symbol, color)

                        save_choice = input("Do you want to save the ASCII art to a text file? (yes/no): ").lower()
                        if save_choice == "yes":
                            output_file_name = input("Enter the file name to save to: ")
                            save_to_text_file(output_lines, output_file_name)
                            print("ASCII art saved to", output_file_name)

                        continue_choice = input("Do you want to continue drawing ASCII art? (yes/no): ").lower()
                        if continue_choice != "yes":
                            exit()  # Exit the program

                        break
                    except ValueError as e:
                        print(e)
                        max_width = int(input("Enter maximum width: "))
