from ext.tabulate import tabulate

def search(metadata, query='*'):
    '''Generates a table of module search results'''

    matches = []

    for module in metadata:
        if query == '*':
            matches.append([module['module_type'], module['name'], module['description']])

            continue

        for value in module.values():
            if query in str(value):
                matches.append([module['module_type'], module['name'], module['description']])

                break

    if not matches:
        return 'ERROR: No matches found for query "%s"!\n\n' % query

    headers = ['Type', 'Name', 'Description']

    return tabulate(matches, headers=headers, tablefmt='grid')

