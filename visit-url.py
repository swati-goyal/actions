import unittest
import requests

class TestStringMethods(unittest.TestCase):
    def visit_url(self):
        url = "https://madrid.quintype.io/"
        path = "ampstories/visual-stories/why-you-need-a-dog-in-your-life"
        requests.get(url+path)

if __name__ == '__main__':
    unittest.main()