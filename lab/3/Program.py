import pyfiglet


def main():
    # Список доступних шрифтів
    available_fonts = pyfiglet.FigletFont.getFonts()

    print("Доступні шрифти:")
    for font in available_fonts:
        print(font)

    selected_font = input("Виберіть шрифт зі списку вище: ")

    if selected_font in available_fonts:
        # Отримуємо введення користувача
        user_input = input("Введіть слово або фразу для генерації ASCII-арту: ")

        # Ініціалізуємо об'єкт pyfiglet.Figlet з обраним шрифтом
        ascii_art_generator = pyfiglet.Figlet(font=selected_font)

        # Генеруємо ASCII-арт з введення користувача
        ascii_art = ascii_art_generator.renderText(user_input)

        # Виводимо ASCII-арт
        print(ascii_art)
    else:
        print("Ви вибрали недійсний шрифт. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
