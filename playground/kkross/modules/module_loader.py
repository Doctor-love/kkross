from collections import namedtuple

def module_loader(dirs):
    Metadata = namedtuple('Metadata', 'name module_type version')
    Module = namedtuple('Module', 'version metadata')

    return [Module(version=0, metadata=Metadata(name='nagios_3-corewindow_uri', module_type='xss_get', version=2))]
