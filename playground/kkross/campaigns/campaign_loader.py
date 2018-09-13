from kkross.exceptions import CampaignError
from kkross.campaign import Campaign

from glob import glob
from yaml import safe_load
import os

def campaign_loader(instance, campaign_dirs):
    '''Loads campaign YAML from ...'''

    campaign_paths = []

    for campaign_dir in campaign_dirs:
        campaign_paths.extend(glob(os.path.join(campaign_dir, '*.y*ml')))

    if not campaign_paths:
        return []

    campaigns = []

    for campaign_path in campaign_paths:
        try:
            campaign_raw = safe_load(open(campaign_path, 'r'))

        except Exception as error_msg:
            raise LoaderError(
                'Failed to load campaign YAML data from "%s": "%s"' % (campaign_path, error_msg))

        try:
            campaigns.append(Campaign(instance, campaign_raw))

        except Exception as error_msg:
            raise
            raise LoaderError('Failed to load campaign from "%s": %s' % (campaign_path, error_msg))

    return campaigns
