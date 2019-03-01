import unittest
import HTMLTestRunner
import os
from testsuits.test_discuz_log import LuntanLog
from testsuits.test_discuz2 import Discuz2
from testsuits.test_discuz3 import Discuz3
from testsuits.test_discuz4 import Discuz4

file_path=os.path.dirname(os.path.abspath("."))+"/test_report"
# cur_path=os.path.dirname(os.path.realpath(__file__))
report_path=os.path.join(file_path,"report")
if not os.path.exists(report_path):os.mkdir(report_path)

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(LuntanLog))
suite.addTest(unittest.makeSuite(Discuz2))
suite.addTest(unittest.makeSuite(Discuz3))
suite.addTest(unittest.makeSuite(Discuz4))

if __name__=="__main__":
    html_report=report_path+r"\result.html"
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告",description="关于abs和sort的测试报告")
    runner.run(suite)
