import logging
import yaml
import os

from collections import namedtuple

log = logging.getLogger('kkross;conf_parser')

# -------------------------------------------------------------------------------------------------
def conf_parser(conf_file):
    log.debug('Reading data from configuration file "%s"' % conf_file)

    conf_data = yaml.load(open(os.path.expanduser(conf_file)))

    return namedtuple('Conf', conf_data.keys())(**conf_data)
