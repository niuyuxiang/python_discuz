import unittest
from pageobjects.discuz_homepage import HomePage
from testsuits.base_testcase import BaseTestCase
import time
from ddt import ddt,data,unpack

@ddt
class Discuz3(BaseTestCase):

    @unpack
    def test_discuz_log(self):
        home_page=HomePage(self.driver)
        home_page.search("nyx","123456")
        time.sleep(2)
        home_page.haotest_post_search("haotest")
        title=home_page.enter()
        try:
            self.assertEqual(title,'haotest',msg=title)
            print('验证正确')
        except:
            print('验证错误')

        # home_page.tuichu()
        time.sleep(10)
if __name__=="__main__":
    unittest.main()