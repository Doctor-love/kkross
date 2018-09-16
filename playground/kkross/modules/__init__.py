import logging
from copy import deepcopy

from kkross.exceptions import ModuleError
from .module_loader import module_loader

log = logging.getLogger('kkross;modules')

# -------------------------------------------------------------------------------------------------
class Modules(object):
    '''Loads modules (exploits, payloads, templates) and returns the common module interface'''

    # ---------------------------------------------------------------------------------------------
    def __extract_metadata(self):
        log.debug('Generating list of module metadata')

        results = []

        for module in self.__modules:
            log.debug('Extracting metadata for module "%s/%s"' % (module.module_type, module.name))

            basic_data = {
                'module_type': module.module_type, 'name': module.name,
                'description': module.description}

            results.append(dict(module.metadata, **basic_data))

        return results

    # ---------------------------------------------------------------------------------------------
    def __init__(self, module_dirs):
        self.__module_dirs = module_dirs
        self.__modules = module_loader(self.__module_dirs)
        self.metadata = self.__extract_metadata()

    # ---------------------------------------------------------------------------------------------
    def get(self, module_id):
        log.debug('Reteriving module ID "%s" from instance' % module_id)

        for module in self.__modules:
            if module.module_type + '/' + module.name == module_id:
                return deepcopy(module)

        raise ModuleError('Could not find module ID "%s" in instance' % module_id)

