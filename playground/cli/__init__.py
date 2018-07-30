try:
    import sys
    import os.path
    import argparse
    import cmd2

    import exploit_parser
    import conf_cli
    from search import search

    from kkross import Instance

except Exception as error_msg:
    raise
    print('Failed to load required dependencies: "%s"' % error_msg)
    sys.exit(3)


# ------------------------------------------------------------------------------------------------
class BaseCli(cmd2.Cmd):
    '''kkross interactive command line interface'''

    def __init__(self, conf_file):
        super().__init__(
            persistent_history_file=os.path.expanduser('~/.kkross_history'),
            persistent_history_length=10000)

        self.intro = '.:: kkross - Cross-site attack framework for redteams (and skiddies) ::.\n'
        self.prompt = self.colorize('kk: ', 'red')

        self.instance = Instance(conf_file)

        return

    # ---------------------------------------------------------------------------------------------
    def exploit_search(self, args):
        self.poutput(search(self.instance.exploits, query=args.query, module_type=args.type))

        return


    # ---------------------------------------------------------------------------------------------
    def exploit_add(self, args):
        cli = conf_cli.ConfCli(args.name)
        cli.cmdloop()

        return

    # ---------------------------------------------------------------------------------------------
    @cmd2.with_argparser(exploit_parser.base_parser)
    def do_exploit(self, args):
        func = getattr(args, 'func', None)

        if not func:
            self.do_help('exploit')
            func(self, args)

        elif func == 'exploit_search':
            self.exploit_search(args)

        elif func == 'exploit_add':
            self.exploit_add(args)


# ------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='kkros', description='kkross - CLI')
    parser.add_argument(
        '-c', '--conf-file', type=str, required=True, help='Path to YAML configuration file')

    args = parser.parse_args()

    cli = BaseCli(args.conf_file)
    cli.cmdloop()
