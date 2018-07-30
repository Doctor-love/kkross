import logging

from kkross.module.parsers import parse_structure
from kkross.module.metadata import Metadata
from kkross.module.options import Options

log = logging.getLogger('kkross;module')

# -------------------------------------------------------------------------------------------------
class Module(object):
    '''Main module object'''

    # ---------------------------------------------------------------------------------------------
    def __init__(self, module_structure):
        self.__module_structure = module_structure
        
        self.structure_version, self.type, self.metadata_raw, self.options_raw, self.template = (
            parse_structure(self.__module_structure))

        self.metadata = Metadata(self.metadata_raw)
        self.options = Options(self.type, self.metadata_raw)
