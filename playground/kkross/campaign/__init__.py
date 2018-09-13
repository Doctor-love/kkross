from kkross.exceptions import CampaignError
from kkross.campaign.parse_structure import parse_structure
from kkross.campaign.parse_data import parse_data


# -------------------------------------------------------------------------------------------------
class Campaign(object):
    '''Main campaign object'''

    def __restore_module(self, instance_modules, module_raw):
        module = instance_modules.get(module_raw['name'])
        module.set_options(**module_raw['options'])

        return module

    # ---------------------------------------------------------------------------------------------
    def __restore_modules(self, instance_modules, modules_raw):
        modules = []

        for module_raw in modules_raw:
            modules.append(self.__restore_module(instance_modules, module_raw))

        return modules

    # ---------------------------------------------------------------------------------------------
    def __init__(self, instance_modules, campaign_structure):
        self.__campaign_structure = campaign_structure

        self.structure_version, self.__data_raw = parse_structure(campaign_structure)

        self.name, self.__templates_raw, self.__payloads_raw, self.__exploits_raw = parse_data(
            self.__data_raw)

        # -----------------------------------------------------------------------------------------
        instance_templates, instance_payloads, instance_exploits = instance_modules

        self.templates = self.__restore_modules(instance_templates, self.__templates_raw)
        self.payloads = self.__restore_modules(instance_payloads, self.__payloads_raw)
        self.exploits = self.__restore_modules(instance_exploits, self.__exploits_raw)

    # ---------------------------------------------------------------------------------------------
    def __extract_metadata(self, modules):
        results = []

        for module in modules:
            module = module.render()
            module.pop('data')
            results.append(module)

        return results

    # ---------------------------------------------------------------------------------------------
    @property
    def metadata(self):
        templates = self.__extract_metadata(self.templates)
        payloads = self.__extract_metadata(self.payloads)
        exploits = self.__extract_metadata(self.exploits)

        return {'templates': templates, 'payloads': payloads, 'exploits': exploits}

    # ---------------------------------------------------------------------------------------------
    def render(self):
        '''Renders all exploits in campaign with all templates - returns a list of strings'''

        if not self.templates or not self.exploits:
            raise CampaignError('Can not render campaign without configured templates/exploits')

        rendered_exploits = []

        for exploit in self.exploits:
            rendered_exploits.append(exploit.render())

        # -----------------------------------------------------------------------------------------
        rendered_templates = []

        for template in self.templates:
            rendered_templates.append(template.render(exploits=rendered_exploits))


        return rendered_templates
