from kkross.exceptions import ModuleError, LoaderError
from kkross.module import Module

from glob import glob
import yaml
import os

def module_loader(module_dirs):
    '''Loads module YAML from ...'''

    module_paths = []

    for module_dir in module_dirs:
        module_paths.extend(glob(os.path.join(module_dir, '*.y*ml')))

    if not module_paths:
        raise LoaderError('Could not find any module files in %s' % ', '.join(module_dirs))

    modules = []

    for module_path in module_paths:
        try:
            module_raw = yaml.load(open(module_path, 'r'))

        except Exception as error_msg:
            raise LoaderError(
                'Failed to load module YAML data from "%s": "%s"' % (module_path, error_msg))

        try:
            modules.append(Module(module_raw))

        except Exception as error_msg:
            raise
            raise LoaderError('Failed to load module from "%s": %s' % (module_path, error_msg))

    return modules
