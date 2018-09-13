from kkross.exceptions import CampaignError


# -------------------------------------------------------------------------------------------------
def parse_module(module_type, module):
    if not 'name' in module:
        raise CampaignError('Required %s item property "name" is missing' % module_type)

    if not 'options' in module:
        raise CampaignError('Required %s item property "options" is missing' % module_type)

    # -----------------------------------------------------------------------------------------
    name = module['name']
    options = module['options']

    if not type(name) is str or not name:
        raise CampaignError(
            'Required %s item property "name" must be a populated string' % module_type)

    if not type(options) is dict or not options:
            raise CampaignError(
                'Required %s item property "options" must be a populated dictionary' % module_type)

    return


# -------------------------------------------------------------------------------------------------
def parse_data(data_structure):
    '''Parses campaign data structure to validate that it is valid'''

    name = data_structure['name']
    modules = data_structure['modules']

    if not type(name) is str:
        raise CampaignError('Required data property "name" must be a string')

    if not type(modules) is dict or not modules:
        raise CampaignError('Required data property "modules" must be a populated dictionary')

    # ---------------------------------------------------------------------------------------------
    for req_property in ['templates', 'payloads', 'exploits']:
        if not req_property in modules:
            raise CampaignError('Required data property "%s" is missing' % req_property)

        if not type(modules[req_property]) is list:
            raise CampaignError('Required property "%s" must be a list' % req_property)

    # ---------------------------------------------------------------------------------------------
    for module_type in ['templates', 'payloads', 'exploits']:
        t_modules = modules[module_type]

        for t_module in t_modules:
            parse_module(module_type, t_module)

    # ---------------------------------------------------------------------------------------------
    return name, modules['templates'], modules['payloads'], modules['exploits']
