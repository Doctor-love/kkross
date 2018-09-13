basic_options = [
    {'name': 'PROTO', 'description': 'Protocol for target host ("http" or "https")',
    'option_type': 'string', 'default': '', 'required': True, 'constraints': [
        {'constraint_type': 'enum', 'options': ['http', 'https']}]
    },
    {'name': 'HOST', 'description': 'Host name or IP address of target host',
    'option_type': 'string', 'default': '', 'required': True, 'constraints': []
    },
    {'name': 'PORT', 'description': 'Port for service on target host',
    'option_type': 'string', 'default': '', 'required': True, 'constraints': []}]


# -------------------------------------------------------------------------------------------------
def get_inherited_options(module_type):
    '''Checks if module type has any inherited options and if so returns them'''

    if 'csrf_' in module_type or 'xss_' in module_type:
        return basic_options

    return []
