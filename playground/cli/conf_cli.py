import cmd2
from ext.tabulate import tabulate


# -------------------------------------------------------------------------------------------------
class ConfCli(cmd2.Cmd):
    '''kkross interactive command line interface for exploit/payload configuration'''

    def generate_summary(self):
        '''Generate a nice summary table of module metadata and options'''

        return tabulate([['PROTO', 'Protcol scheme', 'https'], ['HOST', 'Host name or IP address', '']], headers=['Name', 'Description', 'Current value'], tablefmt='grid')

        summary = (
            '%s/%s\n\n' % (self.module.type, self.module.name) + metadata_table + options_table)

        return summary

    # ---------------------------------------------------------------------------------------------
    def __init__(self, crusade_name, module):
        super().__init__()

        self.crusade_name = crusade_name
        self.module = module
        self.prompt = self.colorize(
            '%s: %s/%s: ' % (self.crusade_name, self.module.type, self.module.name), 'orange')

        self.summary = self.generate_summary()
        #self.prompt = self.colorize(module.metadata.name + ': ', 'yellow')

    #@cmd2.with_argparser(conf_parser.set_parser(self.module.options))
    @cmd2.with_argparser(conf_parser.set_parser(options))
    def do_set(self, args):
        self.poutput('SET jao')
