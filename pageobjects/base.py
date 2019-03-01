from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
import time
import os.path
logger=Logger(logger='BasePage').getlog()
class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")
    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")
    def open_url(self,url):
        self.driver.get(url)
    def quite_browser(self):
        self.driver.quit()
    def close(self):
        try:
            self.driver.close()
            logger.info("Close and quit the browser.")
        except Exception as e:
            logger.error("Failed to quit the browser with %s"%e)
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print("")
    def find_elements(self,*loc):
        try:
            WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except:
            print("页面元素未找到")
    def clear(self,*loc):
        el=self.find_element(*loc)
        try:
            el.clear()
        except Exception as e:
            logger.error("clear fail%s"%e)
    def sendkeys(self, text, *loc):
        el=self.find_element(*loc)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("%s被输入" %text)
        except Exception as e:
            logger.error("Failed to type in input box with %s"%(el).text)
            self.get_windows_img()
    def bianli(self,*loc):
        list1=[]
        list2=[]
        list=self.find_elements(*loc)
        for i in (0,len(list)):
            if i%2==0:
                list1.append(i)
                return list1#偶数是比例
            else:
                list2.append(i)
                return list2
    def click(self,*loc):
        el = self.find_element(*loc)
        try:
            el.click()
            logger.info("%s is be clicked"%(el).text)
        except:
            logger.error("Failed to be clicked")
    def get_windows_img(self):
        file_path = os.path.dirname(os.path.abspath('.'))+'/screenshots/'
        rq = time.strftime('%Y%M%D%H%M',time.localtime(time.time()))
        screen_name = file_path + rq+'.png'
        try:
            self.driver.get_screenshots_as_file(screen_name)
            logger.info("Had take screenshort and save to folder: /screenshots")
        except Exception as e:
            self.get_windows_img()
            logger.error("Failed to take screenshort! %s"%e)
    def window(self,x):
        self.driver.switch_to.window(self.driver.window_handles[x])
    def iframe(self,y):
        self.driver.switch_to.frame(y)





