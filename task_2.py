"""Программа, принимающая строку и удаляющая дубликаты символов из неё.
Ввод и вывод пользовательских значений организован с помощью файлов stdin.txt и stdout.txt"""


if __name__ == '__main__':
    with open('stdin.txt', 'r', encoding='utf-8') as input_file:
        string = input_file.read()

    edited_string = ''
    for symb in string:
        if symb not in edited_string:
            edited_string += symb

    with open('stdout.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(edited_string)
