import argparse

# ------------------------------------------------------------------------------------------------
def set_parser():
    parser = argparse.ArgumentParser(prog='set')

    parser.add_argument(
        'name', type=str, help='Name of option to configure')

    parser.add_argument(
        'value', type=str, help='Value of option to configure')

    return parser
