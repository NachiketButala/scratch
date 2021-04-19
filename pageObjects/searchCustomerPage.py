import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver

class searchCustomer:
    txtEmail_id="SearchEmail"
    txtFirstName_id="SearchFirstName"
    txtLastName_id="SearchLastName"
    btnSearch_id="search-customers"
    tbl_xpath="//table[@id='customers-grid']"
    tblRows_xpath="//table[@id='customers-grid']//tbody//tr"
    tblColumns_xpath="//table[@id='customers-grid']//tbody//tr//td"

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element_by_id(self.txtEmail_id).clear()
        self.driver.find_element_by_id(self.txtEmail_id).send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element_by_id(self.txtFirstName_id).clear()
        self.driver.find_element_by_id(self.txtFirstName_id).semd_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element_by_id(self.txtLastName_id).clear()
        self.driver.find_element_by_id(self.txtLastName_id).semd_keys(lname)

    def clickSearch(self):
        self.driver.find_element_by_id(self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.tblRows_xpath))

    def getNoOfCols(self):
        return len(self.driver.find_elements_by_xpath(self.tblColumns_xpath))

    def searchCustomByEmail(self,email):
        flag=False
        for i in range(1,self.getNoOfRows()+1):
            tbl=self.driver.find_element_by_xpath(self.tbl_xpath)
            emailid=tbl.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(i)+"]/td[2]").text
            if emailid==email:
                flag=True
                break
        return flag

    def searchCustomByNAme(self,name):
        flag=False
        for i in range(1,self.getNoOfRows()+1):
            tbl=self.driver.find_element_by_xpath(self.tbl_xpath)
            emailid=tbl.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(i)+"]/td[3]").text
            if name==name:
                flag=True
                break
        return flag