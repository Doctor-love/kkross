import logging

from kkross.exceptions import OptionsError

log = logging.getLogger('kkross;module')

# -------------------------------------------------------------------------------------------------
def parse_structure(module_structure):
    '''Checks if module structure looks resonable before further processing'''

    if not type(module_structure) is dict:
        raise ModuleError('Module data is invalid (dictionary required)')

    for req_property in ['structure_version', 'data']:
        if not req_property in module_structure:
            raise ModuleError('Module data is invalid - property "%s" not found' % req_property)

    # ---------------------------------------------------------------------------------------------
    structure_version = module_structure['structure_version']
    data = module_structure['data']

    if not type(structure_version) is int and structure_version > 1:
        raise ModuleError('Module version "%s" is not supported' % str(structure_version))

    if not type(module_structure['data']) is dict:
        raise ModuleError('Module data is invalid - "data" property must be a dictionary')

    # ---------------------------------------------------------------------------------------------
    for req_property in ['type', 'metadata', 'options', 'template']:
        if not req_property in data: 
            raise ModuleError('Module data is invalid: property "%s" not found' % req_property)
    
    if not type(data['type']) is str:
        raise ModuleError('Module data is invalid - "type" property must be a string')
    
    if not type(data['metadata']) is dict: 
        raise ModuleError('Module data is invalid - property "metadata" must be a dictionary')
    
    if not type(data['options']) is list: 
        raise ModuleError('Module data is invalid - property "options" must be a list')

    if not type(data['template']) is str:
        raise ModuleError('Module data is invalid - "template" property must be a string')

    return structure_version, data['type'], data['metadata'], data['options'], data['template']
