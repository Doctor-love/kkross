from .conf_parser import conf_parser
from .modules import Modules

class Instance(object):
    '''Main Kkross object - returns instance'''

    def __init__(self, conf_file):
        self.conf_file = conf_file
        self.conf = conf_parser(conf_file)

        self.templates = Modules(self.conf.template_dirs)
        self.payloads = Modules(self.conf.payload_dirs)
        self.exploits = Modules(self.conf.exploit_dirs)

        #self.crusades = crusades.Crusades(self.conf.crusades_dir)
