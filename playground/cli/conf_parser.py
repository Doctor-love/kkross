import argparse

# ------------------------------------------------------------------------------------------------
def set_parser(options):
    option_names = []

    for option in options:
        option_names.append(option.name)

    parser = argparse.ArgumentParser(prog='set')

    parser.add_argument(
        'option', type=str, choices=option_names, help='Name of option to configure')

    parser.add_argument(
        'value', type=str, help='Value of option to configure')

    return parser
