import logging

from kkross.module.parse_structure import parse_structure
from kkross.module.parse_options import parse_options

log = logging.getLogger('kkross;module')

# -------------------------------------------------------------------------------------------------
class Module(object):
    '''Main module object'''

    # ---------------------------------------------------------------------------------------------
    def __init__(self, module_structure):
        self.__module_structure = module_structure

        module_attributes = (
            'structure_version', 'module_type', 'name', 'description', 'metadata',
            '__options_raw', 'template', 'instance_id')

        for key, value in zip(module_attributes, parse_structure(self.__module_structure)):
            setattr(self, key, value)

        self.options = parse_options(self.__options_raw)
