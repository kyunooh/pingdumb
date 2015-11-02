import unittest

from main_module import get_status, url_type


class MainModuleTest(unittest.TestCase):

    def test_status(self):
        self.assertEqual(200, get_status("http://jellyms.kr"))

    def test_url_type(self):
        self.assertEqual("http://jellyms.kr", url_type("jellyms.kr"))
        self.assertEqual("http://jellyms.kr", url_type("http://jellyms.kr"))
