from seleniumbase import BaseCase

class MyTestClass(BaseCase):

    def test_demo_site(self):
        url = "https://madrid.quintype.io/"
        path = "ampstories/visual-stories/why-you-need-a-dog-in-your-life"
        self.open(url+path)