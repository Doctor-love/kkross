import logging

from kkross.exceptions import *

log = logging.getLogger('kkross;module.metadata')

# -------------------------------------------------------------------------------------------------
class Metadata(object):
    '''Module metadata object'''

    def __init__(self, properties):
        log.debug('Creating metadata object with properties "%s"' % str(properties))
        
        # -----------------------------------------------------------------------------------------
        for req_property in ['name', 'description']:
            if not req_property in properties.keys():
                raise MetadataError('Metadata is missing required property "%s"' % req_property)

            if not type(properties[req_property]) is str:
                raise MetadataError('Metadata property "%s" must be a string' % req_property)

        # -----------------------------------------------------------------------------------------
        try:
            self.__dict__.update(properties)

        except Exception as error_msg:
            raise MetadataError('Failed to load module metadata: "%s"' % error_msg)

