from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time
class HomePage(BasePage):
    username=(By.ID,"ls_username")
    password=(By.ID,"ls_password")
    log_button=(By.CSS_SELECTOR,".pn em")

    moren=(By.CSS_SELECTOR,".fl_tb h2 a")
    title=(By.CSS_SELECTOR,".px")
    textarea=(By.ID,"fastpostmessage")
    button=(By.CSS_SELECTOR,".ptm .pn strong")

    more=(By.CSS_SELECTOR,".fl_tb h2 a")
    reply=(By.CSS_SELECTOR,".by a span")
    text=(By.ID,"fastpostmessage")
    button1=(By.ID,"fastpostsubmit")

    button2=(By.XPATH,"//*[@id='um']/p[1]/a[5]")



    mr=(By.CSS_SELECTOR,".fl_tb h2 a")
    delete=(By.NAME,"moderate[]")
    delete1=(By.XPATH,"//*[@id='mdly']/p[1]/strong[1]/a")
    delete2=(By.CSS_SELECTOR,".pn span")

    guanli=(By.XPATH,"//*[@id='um']/p[1]/a[6]")
    # pwd=(By.CLASS_NAME,"txt")
    # button4=(By.CLASS_NAME,"btn")
    luntan=(By.ID,"header_forum")

    add=(By.CSS_SELECTOR,".addtr")
    t=(By.NAME,"newforum[1][]")
    button3=(By.ID,"submit_editsubmit")

    guantui=(By.CSS_SELECTOR,".uinfo a")
    admin_quit=(By.LINK_TEXT,"退出")

    xinban=(By.CSS_SELECTOR,".fl_row td:nth-child(2) h2 a")




    post_search=(By.CSS_SELECTOR,".scbar_txt_td input")     #搜索haotest帖子
    haotest_button=(By.CSS_SELECTOR,".scbar_btn_td button")  #点击搜索帖子按钮

    enter_post=(By.CSS_SELECTOR,".xs3 strong font")  #点进搜帖找到的haotest
    title_loc=(By.CSS_SELECTOR,'.ts')
    # title_expect=(By.CSS_SELECTOR,".ts span")

    fatie1=(By.CSS_SELECTOR,".bm a img")
    start=(By.CSS_SELECTOR,".bm img")
    start_vote=(By.XPATH,"//*[@id='editorbox']/ul/li[2]/a")
    start_vote_text=(By.CSS_SELECTOR,".z .px ")
    start_vote_text1=(By.CSS_SELECTOR,".mbm .px")
    start_vote_text2=(By.CSS_SELECTOR,".mbm p:nth-child(2) input")
    start_vote_text3=(By.CSS_SELECTOR,".mbm p:nth-child(3) input")
    start_vote_text4=(By.XPATH,"/html/body")
    start_vote_button=(By.CSS_SELECTOR,".pn span")

    radio_option_1=(By.ID,"option_1")
    radio_option_2=(By.ID,"option_2")
    radio_option_3=(By.ID,"option_3")
    radio_submit=(By.CSS_SELECTOR,".pn span")

    radio_frame=(By.CSS_SELECTOR,".pcht tr")   #找到选票的整个文本框

    option_title=(By.CSS_SELECTOR,".ts span")    #发起投票的标题


    def search(self,text1,text2):
        self.sendkeys(text1,*self.username)
        self.sendkeys(text2,*self.password)
        self.click(*self.log_button)
        self.click(*self.moren)
    def fatie(self,text1,text2):
        self.click(*self.moren)
        self.sendkeys(text1,*self.title)
        self.sendkeys(text2,*self.textarea)
        self.click(*self.button)
    def huitie(self,text1):
        self.click(*self.more)
        self.click(*self.reply)
        self.sendkeys(text1,*self.text)
        self.click(*self.button1)
    def tuichu(self):
        self.click(*self.button2)



    def dele(self):
        time.sleep(3)
        self.click(*self.mr)
        self.click(*self.delete)
        self.click(*self.delete1)
        self.click(*self.delete2)
    def manage(self):
        self.click(*self.guanli)
        # self.sendkeys(p,*self.pwd)
        # self.click(*self.button4)
        self.window(1)
        self.click(*self.luntan)
    def tianjia(self,n):
        self.iframe(0)
        self.click(*self.add)
        time.sleep(10)
        self.sendkeys(n,*self.t)
        time.sleep(10)
        self.click(*self.button3)
        time.sleep(10)
    def tui(self):
        self.click(*self.guantui)
        self.window(0)
        time.sleep(3)
        self.click(*self.admin_quit)
    def xin(self,t1,t2):
        self.click(*self.xinban)
        self.sendkeys(t1,*self.title)
        self.sendkeys(t2,*self.textarea)
        self.click(*self.button)



    def haotest_post_search(self,h):
        self.clear(*self.post_search)
        self.sendkeys(h,*self.post_search)
        self.click(*self.haotest_button)
    def enter(self):
        time.sleep(2)
        self.window(1)  #切换到搜索haotest的点击窗口
        self.click(*self.enter_post)
        self.window(2)  #切换到haotest论坛里面
        title=self.find_element(*self.title_loc).text  #用title承接
        return title



    def publish_post(self,m,n,v,l,o):
        self.click(*self.moren)
        self.click(*self.start)
        self.click(*self.start_vote)
        self.sendkeys(m,*self.start_vote_text)
        self.sendkeys(n,*self.start_vote_text1)
        self.sendkeys(v,*self.start_vote_text2)
        self.sendkeys(l,*self.start_vote_text3)
        self.iframe(0)
        self.sendkeys(o,*self.start_vote_text4)
        self.window(0)
        self.click(*self.start_vote_button)
    def cast_vote(self):
        self.click(*self.radio_option_1)
        self.click(*self.radio_option_2)
        self.click(*self.radio_option_3)
        self.click(*self.radio_submit)
    def vote_frame(self):
        print(self.bianli(*self.radio_frame))


    # def vote_title(self):
    #     print("*self.option_title".text)