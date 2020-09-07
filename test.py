from seleniumbase import BaseCase
import time


class MyTestClass(BaseCase):

    def test_demo_site(self):
        
        # Prod
        url = "https://madrid.quintype.io/"
        path = "technology/drivezy-to-liquidate-its-fleet-as-demand-falls-amid-virus-outbreak"
        path1 = "culture/india/pursuitsbugatti-centodieci-revives-spirit-of-eb110-photos-specs-price"
        path2 = "tech/mobile/trai-chief-we-set-spectrum-price-industry-decides-tariff"
        path3 = "culture/this-is-a-title-9"
        path4 = "technology/youtube-now-available-for-jiophone"
        
        # Staging
        url_stg = "https://bloombergquint-web.qtstage.io/"
        path5 = "bq-blue-exclusive/new-story-check-for-add-social-card"

        self.open(url+path)
        time.sleep(5)

        self.open(url+path1)
        time.sleep(5)

        self.open(url+path2)
        time.sleep(5)

        self.open(url+path3)
        time.sleep(5)

        self.open(url+path4)
        time.sleep(5)
        
        self.open(url_stg+path5)
        time.sleep(5)
