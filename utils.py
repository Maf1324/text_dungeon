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
