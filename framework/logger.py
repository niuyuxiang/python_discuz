import logging
import os .path
import time
class Logger(object):
    def __init__(self,logger):
        self.logger=logging.getLogger(logger)

        self.logger.setLevel(logging.DEBUG)
        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        log_path=os.path.dirname(os.path.abspath('.'))+'/logs/'
        log_name=log_path+rq+'.log'
        fh=logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)
        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formater=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formater)
        ch.setFormatter(formater)
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    def getlog(self):
        return  self.logger
