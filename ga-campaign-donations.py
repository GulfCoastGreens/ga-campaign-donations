import json
import netifaces
import yaml
import sys

class GACampaignDonations:

  def __init__(self):
    with open('/usr/local/etc/ga-campaign-donations/ga-campaign-donations.yml', 'r') as f:
      self.gcd_config = yaml.load(f)

  def dummy(self):
    print("Hello")


 if __name__== "__main__":
  ca = GACampaignDonations()
  ca.dummy()
   