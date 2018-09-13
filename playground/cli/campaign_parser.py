import argparse

# -------------------------------------------------------------------------------------------------
base_parser = argparse.ArgumentParser(prog='campaign')

base_subparser = base_parser.add_subparsers(
    title='Campaign subcommands', help='Commands for interacting with campaign(s)')

# -------------------------------------------------------------------------------------------------
list_parser = base_subparser.add_parser('list', help='List available campaigns') 
list_parser.set_defaults(func='campaign_list')

list_parser.add_argument(
    '-f', '--filter', metavar='SEARCH_STRING', type=str,
    help='Filter listed campaigns by string pattern')

# -------------------------------------------------------------------------------------------------
create_parser = base_subparser.add_parser('create', help='Create a campaign') 
create_parser.set_defaults(func='campaign_create')

create_parser.add_argument(
    'name', type=str, help='Specify name of campaign to create')

# -------------------------------------------------------------------------------------------------
load_parser = base_subparser.add_parser('load', help='Load a campaign') 
load_parser.set_defaults(func='campaign_load')

load_parser.add_argument(
    'name', type=str, help='Name of campaign to load')

# -------------------------------------------------------------------------------------------------
status_parser = base_subparser.add_parser(
    'status', help='Show crusade status and currently configured modules') 

status_parser.set_defaults(func='campaign_status')

status_parser.add_argument(
    '-t', '--type', dest='category_type', type=str, choices=['templates', 'payloads', 'exploits'],
    help='Only show modules in specic category')

# -------------------------------------------------------------------------------------------------
render_parser = base_subparser.add_parser('render', help='Render campaign to file') 
render_parser.set_defaults(func='campaign_render')

render_parser.add_argument(
    '-d', '--debug', type=bool, default=False,
    help='Include debugging information and exploit meta-data in rendered output')

render_parser.add_argument(
    'output_path', type=str, default='.',
    help='Target path of rendered output files (default: "%(default)s")')
