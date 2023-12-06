# Зчитування текстового файлу, заміна символів та запис у новий файл
with open("ascii_art.txt", 'r') as input_file, open("ascii_art_do.txt", 'w') as output_file:
    for line in input_file:
        modified_line = ""
        for char in line:
            if char in '-\\|_' or char == '/':
                modified_line += '@'
            else:
                modified_line += char
        output_file.write(modified_line)
