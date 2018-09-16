from kkross.conf_parser import conf_parser
from kkross.modules import Modules
from kkross.campaigns import Campaigns

class Instance(object):
    '''Main kkross object - returns instance'''

    def __init__(self, conf_file):
        self.conf_file = conf_file
        self.conf = conf_parser(conf_file)

        self.templates = Modules(self.conf.template_dirs)
        self.payloads = Modules(self.conf.payload_dirs)
        self.exploits = Modules(self.conf.exploit_dirs)
        self.__modules = (self.templates, self.payloads, self.exploits)

        self.campaigns = Campaigns(self.__modules, self.conf.campaign_dirs)
