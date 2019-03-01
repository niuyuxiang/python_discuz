#浏览器的引擎
import os.path
from configparser import ConfigParser  #有效读取配置文件数据
from selenium import webdriver
from framework.logger import Logger  #日志文件

logger=Logger(logger="BrowserEngine").getlog()

class BrowserEngline(object):
    dir=os.path.dirname(os.path.abspath("."))    #调用os.path模块  相对路径获取方法
    chrome_driver_path=dir+"/tools/chromedriver.exe"  #安装相应的驱动器
    firefox_driver_path=dir+"/tools/geckodriver.exe"
    ie_driver_path=dir+"/tools/IEDriverServer.exe"

    def open_browser(self):
        '''在配置文件下找到浏览器，选择浏览器，获得查找内容地址，设置窗口最大化，并且等待10秒，每一个过程都用logger记录'''
        config=ConfigParser()#有效读取配置文件数据
        file_path=os.path.dirname(os.path.abspath("."))+"/config/config.ini"  #用相对路径找到配置文件
        config.read(file_path)#读取配置文件内容
        browser=config.get("browserType","browserName")
        logger.info("You had select %s browser"%browser)   #你已经挑选了哪个浏览器
        url=config.get("testServer","url")   #地址
        logger.info("The test sever url is:%s"%url)  #用日志记录一下获得的地址

        if browser=="Firefox":
            self.driver=webdriver.Firefox(self.firefox_driver_path)  #利用webdriver打开火狐浏览器
            logger.info("Starting firefox browser.") #利用logger记录  “开启了火狐浏览器”
        elif browser=="Chrome":
            self.driver=webdriver.Chrome(self.chrome_driver_path)
            logger.info("Staring chrome browser.")
        elif browser=="IE":
            self.driver=webdriver.Ie(self.ie_driver_path)
            logger.info("Staring IE browser")

        self.driver.get(url)   #获得要查找内容的地址
        logger.info("Open url:%s"%url)

        self.driver.maximize_window()
        logger.info("Maximize the current window.")  #日志记录当前窗口最大化

        self.driver.implicitly_wait(10)
        logger.info("Set implicity wait 10 seconds. ")  #日志记录隐试等待10秒

        return self.driver
    def quit_browser(self):
        self.driver.quit()
        logger.info("日志记录退出并关闭浏览器")




