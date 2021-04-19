import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readproperties import readConfig
from utilities.customlogger import LogGen
from utilities import excelutils
import time
from pageObjects.searchCustomerPage import searchCustomer
from pageObjects.AddCustomerPage import AddCustomer

class Test_seatchCustomerByEmail_004():
    baseURL = readConfig.getApplicationURL()
    username = readConfig.getApplicationUsername()
    password = readConfig.getApplicationPassword()
    logger = LogGen.loggen()

    def test_searchCustmerByEmail(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.addcustomer=AddCustomer(self.driver)
        self.addcustomer.clickOnCustomerMenu()
        self.addcustomer.clickOnCustomerMenuItem()

        searchcust=searchCustomer(self.driver)

        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomByNAme("Victoria Terces")
        assert True==status
        self.driver.close()
