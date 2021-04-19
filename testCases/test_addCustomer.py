import pytest
import time

from pageObjects.LoginPage import Login
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readproperties import readConfig
from utilities.customlogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL=readConfig.getApplicationURL()
    username=readConfig.getApplicationUsername()
    password=readConfig.getApplicationPassword()
    logger=LogGen.loggen()

    def test_addCustomer(self,setup):
        self.logger.info("*****Test_003_AddCustomer*****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.clickOnAddNew()

        self.email= random_generator()+"@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setGender("Male")
        self.addcust.setMgrOfVendor("Vendor 2")
        self.addcust.setFirstName("Sunil")
        self.addcust.setLastName("Pawar")
        self.addcust.setDob("7/05/1996")
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("LeL")
        self.addcust.clickOnSave()

        self.msg=self.driver.find_element_by_tag_name("body").text

        print(self.msg)

        if 'customer has been added successfully.' in self.msg:
            assert True == True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "Test_003_AddCustomer.png")
            assert True == False
        self.driver.close()





def random_generator(size=8, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))
