import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readproperties import readConfig
from utilities.customlogger import LogGen


class Test_001_Login():
    baseURL = readConfig.getApplicationURL()
    username = readConfig.getApplicationUsername()
    password = readConfig.getApplicationPassword()

    logger = LogGen.loggen()

    def test_homepageTitle(self, setup):
        self.logger.info("**********Test_001_Login**********")
        self.logger.info("**********Verifying Home Page**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title

        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**********Home Page title test is passed**********")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "Test_001_Login.png")
            self.driver.close()
            self.logger.error("**********Home Page title test is failed**********")
            assert False

    def test_login(self, setup):
        self.logger.info("**********Test_001_Login**********")
        self.logger.info("**********Verifying Login functionality**********")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**********Login test is passed**********")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
            self.driver.close()
            assert False
            self.logger.info("**********Login Test is failed**********")
