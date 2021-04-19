import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readproperties import readConfig
from utilities.customlogger import LogGen
from utilities import excelutils
import time

class Test_002_DDT_Login():
    baseURL = readConfig.getApplicationURL()
    path=".//testData/testdata.xlsx"

    logger = LogGen.loggen()


    def test_login_ddt(self, setup):
        self.logger.info("**********Test_002_DDT_Login**********")
        self.logger.info("**********Verifying Login functionality**********")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)

        self.rows=excelutils.getRowCount(self.path,'Sheet1')
        print("No of rows in an exel= ",self.rows)

        lst_stats=[]

        for r in range(2,self.rows+1):
            self.user=excelutils.readData(self.path,'Sheet1',r,1)
            self.password = excelutils.readData(self.path, 'Sheet1', r, 2)
            self.exp = excelutils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("Pass")
                    self.lp.clickLogout()
                    lst_stats.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("Fail")
                    self.lp.clickLogout()
                    lst_stats.append("Fail")

            if act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("Fail")
                    self.lp.clickLogout()
                    lst_stats.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("Pass")
                    lst_stats.append("Pass")



        if "Fail" not in lst_stats:
            self.logger.info("Login DDT test is passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT test is failed")
            self.driver.close()
            assert False
        # self.lp.setUserName(self.username)
        # self.lp.setPassword(self.password)
        # self.lp.clickLogin()
        # actual_title = self.driver.title
        # if actual_title == "Dashboard / nopCommerce administration":
        #     assert True
        #     self.logger.info("**********Login test is passed**********")
        # else:
        #     self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
        #     self.driver.close()
        #     assert False
        #     self.logger.info("**********Login Test is failed**********")
