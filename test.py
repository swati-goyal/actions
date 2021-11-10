from seleniumbase import BaseCase
import time


class MyTestClass(BaseCase):
    
    def open_url(self, url, path):
        self.open(url + path)
        time.sleep(1)

    def test_demo_site(self):
        
        # Prod
        url = "https://madrid.quintype.io/"
        prod_paths = ["technology/drivezy-to-liquidate-its-fleet-as-demand-falls-amid-virus-outbreak", "culture/india/pursuitsbugatti-centodieci-revives-spirit-of-eb110-photos-specs-price", 
                 "tech/mobile/trai-chief-we-set-spectrum-price-industry-decides-tariff", "culture/this-is-a-title-9", "technology/youtube-now-available-for-jiophone"]
        
        for i in prod_paths:
            self.open_url(url, i)
        
        # Staging
        url_stg = "https://malibu-integration-web.qtstage.io/"
        stg_paths = ["whatever/imported-story-1-should-get-published-4", "whatever/headline-09837232647442259", "whatever/headline-09710416993351383", 
                     "whatever/headline-09369913954141263", "whatever/headline-07610392921128447"]
        
        for i in stg_paths:
            self.open_url(url_stg, i)
