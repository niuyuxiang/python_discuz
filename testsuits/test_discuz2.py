import unittest
from pageobjects.discuz_homepage import HomePage
from testsuits.base_testcase import BaseTestCase
import time
import HTMLTestRunner
class Discuz2(BaseTestCase):
    def test_discuz_log(self):
        home_page=HomePage(self.driver)
        home_page.search("admin","admin")
        home_page.dele()
        time.sleep(3)
        home_page.manage()
        home_page.tianjia("haotest")
        home_page.tui()
        home_page.search("nyx","123456")
        home_page.xin("haotest","xinbanmokuaihaotestceshi")
        home_page.huitie("sfhoieatuiisnvjzv")
        home_page.tuichu()
        time.sleep(5)
if __name__=="__main__":
    unittest.main()