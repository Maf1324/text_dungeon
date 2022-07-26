from types import FunctionType


def row_print(*args):
    print()
    print(*args, sep='\n')
    print()


def handle_choice(choice, choices) -> FunctionType:
    if choice not in choices:
        print('Invalid option')
        choice = input()
        return handle_choice(choice, choices)

    return choices[choice]


def get_int_input(frase=''):
    choice = input(f'{frase} --> ')
    try:
        choice = int(choice)
        return choice
    except ValueError as e:
        e = e
        row_print('Invalid point value, use only numbers and try again...')
        return get_int_input(frase)
