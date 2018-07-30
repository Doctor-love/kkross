import logging

from kkross.exceptions import *

log = logging.getLogger('kkross;options')

# -------------------------------------------------------------------------------------------------
class Options(object):
    '''Module options object'''

    def __init__(self, options_raw):
        self.options_raw = options_raw

        if not type(self.options_raw) is list: 
            raise OptionError('Failed to load module options - "options" property must be a list')

        for option_raw in self.options_raw:



