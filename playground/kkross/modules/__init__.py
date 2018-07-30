from .module_loader import module_loader

import logging

log = logging.getLogger('kkross;modules')

# -------------------------------------------------------------------------------------------------
class Modules(object):
    '''Loads modules (exploits, payloads, templates) and returns the common module interface'''

    def __init__(self, module_dirs):
        self.__module_dirs = module_dirs
        self.__modules = module_loader(self.__module_dirs)

    # ---------------------------------------------------------------------------------------------
    def extract_metadata(self):
        log.debug('Generating list of module metadata')

        results = []

        for module in self.__modules:
            results.append(module.metadata)

        return results

    # ---------------------------------------------------------------------------------------------
    def search(self, query='*', **kwargs):
        log.debug('Generating list of modules ')

        search_filters = kwargs
        modules = self.extract_metadata()

        if query == '*' and not search_filters:
            return modules

        # -----------------------------------------------------------------------------------------
        results = []

        for module in modules:
            attributes = dir(module)
            matches = []

            for key, value in search_filters.items():
                if key in attributes and value in getattr(module, key):
                    matches.append(key)

            if len(search_filters) == len(matches):
                if query == '*':
                    results.append(module)
                    continue
            else:
                continue

            # -------------------------------------------------------------------------------------
            for match in matches:
                if match in attributes:
                    attributes.pop(match)

            for key in attributes:
                if key.startswith('__'):
                    continue

                value = getattr(module, key)

                if query in value:
                    results.append(module)
                    break

        # -----------------------------------------------------------------------------------------
        log.debug('Found %i modules matching search filter and query' % len(results))

        return results
