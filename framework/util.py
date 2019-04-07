import xlrd   #python中关于读表格的调用
from framework.logger import Logger    #日志记录
logger=Logger("logger=Util").getlog()
class Util(object):
    @classmethod
    def read_excel(self,excelPath,sheetName="Sheet1"):
        workbook=xlrd.open_workbook(excelPath)
        sheet=workbook.sheet_by_name(sheetName)
        keys=sheet.row_values(0)
        rowNum=sheet.nrows
        cloNum=sheet.ncols

        if rowNum<=1:
            logger.error("读取的表格中数据总行小于1")
        else:
            r=[]
            for i in range(1,rowNum):
                sheet_data={}
                values=sheet.row_values(i)
                for j in range(cloNum):
                    sheet_data[keys[j]]=values[j]
                r.append(sheet_data)
        return r
if __name__=="__main__":
    print(Util.read_excel("E:/工作簿1.xlsx", "Sheet1"))