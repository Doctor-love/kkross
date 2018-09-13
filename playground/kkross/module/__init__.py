from logging import getLogger
from jinja2.sandbox import SandboxedEnvironment

from kkross.exceptions import ModuleError
from kkross.module.parse_structure import parse_structure
from kkross.module.parse_options import parse_options

log = getLogger('kkross;module')

# -------------------------------------------------------------------------------------------------
class Module(object):
    '''Main module object'''

    # ---------------------------------------------------------------------------------------------
    def __init__(self, module_structure):
        self.__module_structure = module_structure

        module_attributes = (
            'structure_version', 'module_type', 'name', 'description', 'metadata',
            'options_raw', 'template', 'instance_id')

        for key, value in zip(module_attributes, parse_structure(module_structure)):
            setattr(self, key, value)

        self.options = parse_options(self.module_type, self.options_raw)

    # ---------------------------------------------------------------------------------------------
    def set_option(self, name, value):
        for option in self.options:
            if option.name == name:
                option.set(value)
                return

        raise ModuleError('Could not find option "%s" in module' % name) 

    # ---------------------------------------------------------------------------------------------
    def set_options(self, **options):
        for name, value in options.items():
            self.set_option(name, value)

        return

    # ---------------------------------------------------------------------------------------------
    def is_configured(self):
        '''Checks if all required are configured - returns True or False'''

        for option in self.options:
            if not option.is_configured():
                return False

        return True

    # ---------------------------------------------------------------------------------------------
    def render(self, **extra_vars):
        render_vars = {}

        if extra_vars:
            render_vars.update(extra_vars)

        for option in self.options:
            if not option.is_configured():
                raise ModuleError('Required option "%s" is not set' % option.name)

            render_vars[option.name] = option.value

        # -----------------------------------------------------------------------------------------
        renderer = SandboxedEnvironment()

        instance_id = renderer.from_string(self.instance_id).render(**render_vars)
        data = renderer.from_string(self.template).render(**render_vars)
            
        return {
            'module_type': self.module_type, 'name': self.name,
            'instance_id': instance_id, 'data': data}

    # ---------------------------------------------------------------------------------------------
    def serialize(self):
        '''Returns a dict with the "serialized" form of the module'''

        options = {}

        for option in self.options:
            options.update(option.serialize())

        return {'name': self.module_type + '/' + self.name, 'options': options}
