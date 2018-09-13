from ext.tabulate import tabulate


# -------------------------------------------------------------------------------------------------
def get_values(modules):
    results = []

    for module in modules:
        results.append([module['module_type'], module['name'], module['instance_id']])

    return results


# -------------------------------------------------------------------------------------------------
def campaign_status(metadata):

    templates = get_values(metadata['templates'])
    payloads = get_values(metadata['payloads'])
    exploits = get_values(metadata['exploits'])

    headers = ['Type', 'Name', 'Instance ID']

    templates_table = tabulate(
        templates, headers=headers, tablefmt='grid')

    payloads_table = tabulate(
        payloads, headers=headers, tablefmt='grid')

    exploits_table = tabulate(
        exploits, headers=headers, tablefmt='grid')

    # ---------------------------------------------------------------------------------------------
    return (
        'Templates:\n' +templates_table + '\n' +
        'Payloads:\n' + payloads_table + '\n' +
        'Exploits:\n' + exploits_table + '\n' + '\n')
