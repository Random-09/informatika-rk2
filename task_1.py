"""Программа, принимающая строку и удаляющая дубликаты символов из неё."""


if __name__ == '__main__':
    string = input()
    edited_string = ''
    for symb in string:
        if symb not in edited_string:
            edited_string += symb
    print(edited_string)
