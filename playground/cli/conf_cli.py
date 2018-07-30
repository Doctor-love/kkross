import cmd2

import conf_parser
from ext.tabulate import tabulate

from collections import namedtuple
Option = namedtuple('Option', 'name description value')
options = []

for option in ['HOST', 'PROTO', 'QUEL']:
    options.append(Option(name=option, description='Blalalblalba blalai ' + option, value='bla'))

# ------------------------------------------------------------------------------------------------
def generate_summary(metadata, options):
    '''Generate a nice summary table of module information'''

    return tabulate([['PROTO', 'Protcol scheme', 'https'], ['HOST', 'Host name or IP address', '']], headers=['Name', 'Description', 'Current value'], tablefmt='grid')


# ------------------------------------------------------------------------------------------------
class ConfCli(cmd2.Cmd):
    '''kkross interactive command line interface for exploit/payload configuration'''

    def __init__(self, module):
        super().__init__()

        #self.module = module
        #self.intro = generate_summary(module.metadata, module.options)
        self.intro = generate_summary('foo', 'bar')
        #self.prompt = self.colorize(module.metadata.name + ': ', 'yellow')
        self.prompt = self.colorize('xss_get/nagios_3-corewindow_uri: ', 'yellow')

    #@cmd2.with_argparser(conf_parser.set_parser(self.module.options))
    @cmd2.with_argparser(conf_parser.set_parser(options))
    def do_set(self, args):
        self.poutput('SET jao')
