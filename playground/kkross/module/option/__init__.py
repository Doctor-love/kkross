import logging

from kkross.exceptions import OptionError
from kkross.module.option.parse_constraints import parse_constraints

log = logging.getLogger('kkross;module')

# -------------------------------------------------------------------------------------------------
class Option(object):
    '''Main option object'''

    # ---------------------------------------------------------------------------------------------
    def __init__(self, option_raw):
        self.__option_raw  = option_raw
        
        self.name = option_raw['name']
        self.description = option_raw['description']
        self.required = option_raw['required']

        option_types = ['string', 'boolean']

        if not option_raw['option_type'] in option_types:
            raise OptionError(
                'Option type "%s" is not valid (supported types: %s)'
                % (option_raw['option_type'], ', '.join(option_types)))

        self.option_type = option_raw['option_type']
        
        # -----------------------------------------------------------------------------------------
        default = option_raw['default']

        if self.option_type == 'string' and not type(default) is str:
            raise OptionError(
                'Option default value "%s" does not match option type string' % str(default))

        elif self.option_type == 'boolean' and not type(default) is bool:
            raise OptionError(
                'Option default value "%s" does not match option type boolean' % str(default))
        
        self.default = default
        self.value = self.default

        # -----------------------------------------------------------------------------------------
        self.constraints = parse_constraints(option_raw['constraints'])

    # ---------------------------------------------------------------------------------------------
    def check(self, value):
        '''Checks if provided value is acceptable based on type and constraints'''

        pass

    # ---------------------------------------------------------------------------------------------
    def set(self, value):
        '''Sets provided value for option'''

        self.check(value)
        self.value = value

        return

    # ---------------------------------------------------------------------------------------------
    def is_configured(self):
        '''Checks if option is configured - returns True or False'''

        if type(self.value) is str and not self.value:
            return False

        return True

    # ---------------------------------------------------------------------------------------------
    def serialize(self):
        '''Returns the "serialized" version of the option'''

        return {self.name: self.value}
