import logging

from kkross.exceptions import OptionsError, OptionError

log = logging.getLogger('kkross;option')

# -------------------------------------------------------------------------------------------------
def options_parser(options_raw):
    '''Does some basic parsing of options and returns option objects'''

    if not type(options_raw) is list:
        raise OptionsError('Options data is invalid (list required)')

    if not options_raw:
        raise OptionsError('Options data is empty (populated list required)')

    options = []

    for option_raw in options_raw:
        if not type(option_raw) is dict:
            raise OptionError('Option data is invalid (dictionary required)')

        for req_property in ['name', 'description', 'type', 'default', 'required', 'constraints']:
            if not req_property in option_raw:
                raise OptionError('Option data is invalid, property "%s" not found' % req_property)
        
        for req_property in ['name', 'description', 'type', 'default']:
            if not type(req_property) is str:
                raise OptionError('Option property "%s" must be a string' % req_property)

        if not type(option_raw['required']) is bool:
            raise OptionError('Option property "required" must be a boolean')
        
        if not type(option_raw['constraints']) is list:
            raise OptionError('Option property "constraints" must be a list')

        options.append(Option(options_raw))

    return options
