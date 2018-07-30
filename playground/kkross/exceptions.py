class KkrossError(Exception):
    '''kkross base exception'''

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class ModuleError(KkrossError):
    '''Issues related to modules'''


class MetadataError(ModuleError):
    '''Issues related to handling of module metadata'''


class OptionError(ModuleError):
    '''Issues related to handling of module options'''
