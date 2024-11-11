# 2.2 Аргументы и параметры функции

def example_args(*args):
    print('Positional argument tuple:', args)


example_args()
example_args(1, 2, 4, 'argument')