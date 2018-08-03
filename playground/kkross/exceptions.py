class KkrossError(Exception):
    '''kkross base exception'''

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class ModuleError(KkrossError):
    '''Issues related to modules'''


class LoaderError(ModuleError):
    '''Issues related to loading of modules'''


class MetadataError(ModuleError):
    '''Issues related to handling of module metadata'''


class OptionsError(ModuleError):
    '''Issues related to handling of module options'''


class OptionError(ModuleError):
    '''Issues related to handling of module option'''
