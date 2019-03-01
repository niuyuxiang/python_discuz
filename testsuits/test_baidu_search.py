import unittest
from pageobjects.baidu_homepage import HomePage
from testsuits.base_testcase import BaseTestCase
import time
import HTMLTestRunner
class BaiduSearch(BaseTestCase):
    def test_baidu_seach(self):   #一定要test开头，把测试逻辑代码封装到一个test开头的方法里
        home_page=HomePage(self.driver)  #声明HomePage类对象
        home_page.search('java')  #调用首页搜索功能
        time.sleep(10)
if __name__=="__main__":
    unittest.main()