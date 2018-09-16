import cmd2
from pprint import pformat
from ext.tabulate import tabulate

import conf_parser


# -------------------------------------------------------------------------------------------------
class ConfCli(cmd2.Cmd):
    '''kkross interactive command line interface for exploit/template/payload configuration'''

    def generate_options(self):
        '''Generate a nice summary table of module options'''

        options = []

        for option in self.module.options:
            options.append(
                [option.name, option.description, str(option.value), str(option.required)])

        return tabulate(
            options, headers=['Name', 'Description', 'Current value', 'Required'], tablefmt='grid')

    # ---------------------------------------------------------------------------------------------
    def generate_summary(self):
        '''Generate a nice summary table of module metadata and options'''

        metadatas = []

        for key, value in self.module.metadata.items():
            metadatas.append([key, str(value)])

        metadata_table = tabulate(
            metadatas, headers=['Property', 'Value'], tablefmt='grid')

        options_table = self.generate_options()

        # -----------------------------------------------------------------------------------------
        return (
            '%s/%s\n\n' % (self.module.module_type, self.module.name) +
            'Description: %s\n' % self.module.description + 
            'Metadata:\n' + metadata_table + '\n' +
            'Options:\n' + options_table + '\n' + '\n')

    # ---------------------------------------------------------------------------------------------
    def __init__(self, campaign, module_category, module):
        super().__init__()

        self.campaign = campaign
        self.module_category = module_category
        self.campaign_name = self.campaign.name
        self.module = module
        self.prompt = self.colorize(
            '%s: %s/%s: '
            % (self.campaign_name, self.module.module_type, self.module.name), 'yellow')

        self.poutput(self.generate_summary())

    # ---------------------------------------------------------------------------------------------
    @cmd2.with_argparser(conf_parser.set_parser())
    def do_set(self, args):
        self.module.set_option(args.name, args.value)
        self.poutput('%s = %s\n\n' % (args.name, args.value))

        return

    # ---------------------------------------------------------------------------------------------
    def do_summary(self, args):
        self.poutput(self.generate_summary())

        return

    # ---------------------------------------------------------------------------------------------
    def do_options(self, args):
        self.poutput(self.generate_options() + '\n\n')

        return

    # ---------------------------------------------------------------------------------------------
    def do_preview(self, args):
        self.poutput(self.module.render())

        return

    # ---------------------------------------------------------------------------------------------
    def do_preview(self, args):
        self.poutput(pformat(self.module.render()) + '\n\n')

        return

    # ---------------------------------------------------------------------------------------------
    def do_save(self, args):
        if not self.module.is_configured():
            self.poutput('Error: All required options are not configured\n\n')
            return

        if self.module_category == 'template':
            self.campaign.templates.append(self.module)

        elif self.module_category == 'payload':
            self.campaign.payloads.append(self.module)

        elif self.module_category == 'exploit':
            self.campaign.exploits.append(self.module)

        return self.do_quit('Done')
