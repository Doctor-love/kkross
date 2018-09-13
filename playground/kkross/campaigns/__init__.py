from logging import getLogger

from kkross.exceptions import CampaignError
from kkross.campaigns.campaign_loader import campaign_loader

log = getLogger('kkross;campaigns')


# -------------------------------------------------------------------------------------------------
class Campaigns(object):
    '''Loads and handle campaign related data'''

    # ---------------------------------------------------------------------------------------------
    def __init__(self, instance, campaign_dirs):
        self.__campaign_dirs = campaign_dirs
        self.__campaigns = campaign_loader(instance, self.__campaign_dirs)
        # self.metadata = self.__extract_metadata()

    # ---------------------------------------------------------------------------------------------
    def get(self, name):
        log.debug('Reteriving campaign name "%s" from instance' % name)

        for campaign in self.__campaigns:
            if campaign.name == name:
                return campaign

        raise CampaignError('Could not find campaign name "%s" in instance' % name)
