import unittest
from pageobjects.discuz_homepage import HomePage
from testsuits.base_testcase import BaseTestCase
import time
import HTMLTestRunner
class LuntanLog(BaseTestCase):
    def test_discuz_log(self):
        home_page=HomePage(self.driver)
        home_page.search("nyx","123456")
        home_page.fatie("我的第一个测试","这是论坛的第一个测试用户登录默认板块发帖默认板块回帖用户退出")
        home_page.huitie("huitie123456789")
        home_page.tuichu()
        time.sleep(10)
if __name__=="__main__":
    unittest.main()