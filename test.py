from seleniumbase import BaseCase
import time


class MyTestClass(BaseCase):

    def test_demo_site(self):

        url = "https://madrid.quintype.io/"
        path = "ampstories/visual-stories/why-you-need-a-dog-in-your-life"
        path1 = "culture/india/pursuitsbugatti-centodieci-revives-spirit-of-eb110-photos-specs-price"
        path2 = "tech/mobile/trai-chief-we-set-spectrum-price-industry-decides-tariff"
        path3 = "culture/this-is-a-title-9"
        path4 = "ampstories/technology/visual-story-demo1"

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
