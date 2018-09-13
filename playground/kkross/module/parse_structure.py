import logging

from kkross.exceptions import ModuleError

log = logging.getLogger('kkross;module')

# -------------------------------------------------------------------------------------------------
def parse_structure(module_structure):
    '''Checks if module structure looks resonable before further processing'''
    
    log.debug('Parsing module structure from raw data: "%s"' % str(module_structure))

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
    for req_property in [
        'module_type', 'name', 'description', 'metadata', 'options', 'template', 'instance_id']:

        if not req_property in data: 
            raise ModuleError('Module data is invalid: property "%s" not found' % req_property)
    
    for req_property in ['module_type', 'name', 'description', 'template', 'instance_id']:
        if not type(data[req_property]) is str: 
            raise ModuleError('Module data is invalid: property "%s" is not string' % req_property)
    
    if not type(data['module_type']) is str:
        raise ModuleError('Module data is invalid - "type" property must be a string')
    
    if not type(data['metadata']) is dict: 
        raise ModuleError('Module data is invalid - property "metadata" must be a dictionary')
    
    if not type(data['options']) is list: 
        raise ModuleError('Module data is invalid - property "options" must be a list')

    if not type(data['template']) is str:
        raise ModuleError('Module data is invalid - "template" property must be a string')

    # ---------------------------------------------------------------------------------------------
    return (
        structure_version, data['module_type'], data['name'], data['description'], 
        data['metadata'], data['options'], data['template'], data['instance_id'])
