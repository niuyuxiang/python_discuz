import unittest
from pageobjects.discuz_homepage import HomePage
from testsuits.base_testcase import BaseTestCase
import time
import HTMLTestRunner
class Discuz4(BaseTestCase):
    def test_discuz_log(self):
        home_page=HomePage(self.driver)
        home_page.search("nyx","123456")
        time.sleep(5)
        home_page.publish_post("1","12","123","1234","发表投票")
        time.sleep(5)
        home_page.cast_vote()
        home_page.vote_frame()
        time.sleep(5)
if __name__=="__main__":
    unittest.main()