try:
    import sys
    import os
    import argparse
    import cmd2

    import crusade_parser
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

    def __init__(self):
        super().__init__(
            persistent_history_file=os.path.expanduser('~/.kkross_history'),
            persistent_history_length=10000)

        self.hidden_commands.extend(['py', 'pyscript', 'edit', 'alias', 'unalias', 'load'])

        self.intro = '\n.:: kkross - Cross-site attack tool for redteams (and skiddies) ::.\n'
        self.prompt = self.colorize('kk: ', 'red')

        # -----------------------------------------------------------------------------------------
        if 'KKROSS_CONF' in os.environ:
            conf_file = os.environ['KKROSS_CONF']

        else:
            conf_file = '~/.kkross_conf.yml'

        #self.instance = Instance(os.path.expanduser(conf_file))

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
    @cmd2.with_argparser(crusade_parser.base_parser)
    def do_crusade(self, args):
        func = getattr(args, 'func', None)

        if not func:
            self.do_help('crusade')
            func(self, args)

        elif func == 'crusade_list':
            self.crusade_list(args)

        elif func == 'crusade_create':
            self.crusade_create(args)

        elif func == 'crusade_load':
            self.crusade_load(args)

        elif func == 'crusade_render':
            self.crusade_render(args)

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

        elif func == 'exploit_remove':
            self.exploit_remove(args)

    # ---------------------------------------------------------------------------------------------
    @cmd2.with_argparser(payload_parser.base_parser)
    def do_payload(self, args):
        func = getattr(args, 'func', None)

        if not func:
            self.do_help('payload')
            func(self, args)

        elif func == 'payload_search':
            self.payload_search(args)

        elif func == 'payload_add':
            self.payload_add(args)
        
        elif func == 'payload_remove':
            self.payload_remove(args)

    # ---------------------------------------------------------------------------------------------
    @cmd2.with_argparser(template_parser.base_parser)
    def do_template(self, args):
        func = getattr(args, 'func', None)

        if not func:
            self.do_help('template')
            func(self, args)

        elif func == 'template_search':
            self.template_search(args)

        elif func == 'template_add':
            self.template_add(args)
        
        elif func == 'template_remove':
            self.template_remove(args)


# ------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    cli = BaseCli()
    cli.cmdloop()
