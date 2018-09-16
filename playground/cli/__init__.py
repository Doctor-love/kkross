try:
    import sys
    import os
    import argparse
    import cmd2

    import campaign_parser
    import exploit_parser
    import conf_cli
    from search import search
    from campaign_status import campaign_status

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

        self.instance = Instance(os.path.expanduser(conf_file))
        self.campaign = None

        return

    # ---------------------------------------------------------------------------------------------
    def campaign_load(self, args):
        self.campaign = self.instance.campaigns.get(args.name)
        self.prompt = self.colorize('%s: ' % self.campaign.name, 'green')

        return

    # ---------------------------------------------------------------------------------------------
    def campaign_status(self, args):
        if not self.campaign:
            self.poutput('Error: No campaign is loaded\n\n')
            return

        self.poutput(campaign_status(self.campaign.metadata))

        return


    # ---------------------------------------------------------------------------------------------
    def campaign_render(self, args):
        results = self.campaign.render()
        file_paths = []

        for index, result in enumerate(results):
            file_path = os.path.join(args.output_path, '%i.%s' % (index, result['module_type']))

            try:
                with open(file_path, 'w') as target_file:
                    target_file.write(result['data'])

                file_paths.append(file_path)

            except Exception as error_msg:
                self.poutput(
                    'Error: Failed to write results to "%s" ("%s")\n\n' % (file_path, error_msg))

                return
                
            self.poutput(
                'Saved rendered results to "%s" - happy hunting!\n\n' % ', '.join(file_paths))

        return

    # ---------------------------------------------------------------------------------------------
    def exploit_search(self, args):
        self.poutput(search(self.instance.exploits.metadata, args.query))

        return

    # ---------------------------------------------------------------------------------------------
    def exploit_add(self, args):
        module = self.instance.exploits.get(args.name)
        cli = conf_cli.ConfCli(self.campaign, 'exploit', module)
        cli.cmdloop()

        return

    # ---------------------------------------------------------------------------------------------
    @cmd2.with_argparser(campaign_parser.base_parser)
    def do_campaign(self, args):
        func = getattr(args, 'func', None)

        if not func:
            self.do_help('campaign')
            func(self, args)

        elif func == 'campaign_list':
            self.campaign_list(args)

        elif func == 'campaign_create':
            self.campaign_create(args)

        elif func == 'campaign_load':
            self.campaign_load(args)

        elif func == 'campaign_status':
            self.campaign_status(args)

        elif func == 'campaign_render':
            self.campaign_render(args)

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
    #@cmd2.with_argparser(payload_parser.base_parser)
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
    #@cmd2.with_argparser(template_parser.base_parser)
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
