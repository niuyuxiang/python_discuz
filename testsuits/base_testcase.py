from selenium import webdriver
import unittest
from framework.browser_engine import BrowserEngline

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.browserEngline=BrowserEngline()
        self.driver=self.browserEngline.open_browser()
        # self.driver=webdriver.Chrome("./chromedriver.exe")
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(5)
    def TearDown(self):
        print("测试结束")
        self.driver=self.browserEngline.quit_browser()