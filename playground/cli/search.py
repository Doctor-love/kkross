from ext.tabulate import tabulate

def search(modules, **kwargs):
    results = modules.search(kwargs)

    return str(results)
