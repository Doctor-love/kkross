class KkrossError(Exception):
    '''kkross base exception'''

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class ModuleError(KkrossError):
    '''Issues related to modules'''


class CampaignError(KkrossError):
    '''Issues related to campaigns'''


class LoaderError(ModuleError):
    '''Issues related to loading of modules'''


class OptionsError(ModuleError):
    '''Issues related to handling of module options'''


class OptionError(ModuleError):
    '''Issues related to handling of module option'''


class ConstraintError(OptionError):
    '''Issues related to handling of module option constraints'''
