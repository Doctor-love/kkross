from kkross.exceptions import CampaignError


# -------------------------------------------------------------------------------------------------
def parse_structure(campaign_structure):
    '''Parses campaign structure to validate that it is valid'''

    if not type(campaign_structure) is dict:
        raise CampaignError('Campaign structure is invalid - must be a dictionary')

    if not campaign_structure:
        raise CampaignError('Campaign structure is empty (populated dictionary required)')

    if not 'structure_version' in campaign_structure:
        raise CampaignError('Required property "structure_version" is missing in structure')

    if not 'data' in campaign_structure:
        raise CampaignError('Required property "data" is missing in structure')

    # ---------------------------------------------------------------------------------------------
    structure_version = campaign_structure['structure_version']
    data = campaign_structure['data']

    if not type(structure_version) is int:
        raise CampaignError('Required property "structure_version" must be a integer')

    if not type(data) is dict or not data:
        raise CampaignError('Required property "data" must be a populated dictionary')

    # ---------------------------------------------------------------------------------------------
    return structure_version, data
