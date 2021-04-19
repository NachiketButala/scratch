import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver

class AddCustomer():
    lnk_customers_menu_css="li.has-treeview:nth-child(4) > a:nth-child(1)"
    lnk_customers_menu_items_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"   #"//span[@class='menu-item-title'][contains(text(),'Customers')]"
    btnAddnew_xpath="//a[@class='btn btn-primary']"
    txtEmail_xpath="//input[@id='Email']"
    txtPassword_xpath="//input[@id='Password']"
    txtfirstname_xpath = "//input[@id='FirstName']"
    txtlastname_xpath = "//input[@id='LastName']"
    txtcustomerRoles_xpath="//div[@class='k-widget k-multiselect k-multiselect-clearable']"
    lstitemAdministrators_xpath="//li[contains(text(),'Administrators')]"
    lstitemRegisters_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrofVendor_xpath = "//*[@id='VendorId']"
    rdMalegender_id="Gender_Male"
    rdFemalegender_id = "Gender_Female"
    txtCompanyname_id="Company"
    chkTax_id="IsTaxExempt"
    btnSave_xpath="//button[@name='save']"
    txtAdminComment_xpath="//textarea[@id='AdminComment']"
    txtDob_xpath="//input[@id='DateOfBirth']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomerMenu(self):
        self.driver.find_element_by_css_selector(self.lnk_customers_menu_css).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element_by_xpath(self.lnk_customers_menu_items_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()
        time.sleep(3)

        if(role=="Registered"):
            self.listitem=self.driver.find_element_by_xpath(self.lstitemRegisters_xpath)

        elif (role == "Administrators"):
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)

        elif (role=="Guests"):

            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem=self.driver.find_element_by_xpath(self.lstitemGuests_xpath)

        elif (role == "Registered"):
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegisters_xpath)

        elif(role=="Vendors"):
            self.listitem= self.driver.find_element_by_xpath(self.lstitemVendors_xpath)

        else:
            self.listitem= self.driver.find_element_by_xpath(self.lstitemGuests_xpath)

        time.sleep(3)
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def setGender(self,gender):
        if gender=="Male":
            self.driver.find_element_by_xpath(self.rdMalegender_id).click()
        elif gender=="Female":
            self.driver.find_element_by_xpath(self.rdFemalegender_id).click()
        else:
            self.driver.find_element_by_xpath(self.rdMalegender_id).click()

    def setFirstName(self,fname):
        self.driver.find_element_by_xpath(self.txtfirstname_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element_by_xpath(self.txtlastname_xpath).send_keys(lname)

    def setDob(self,dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self,cname):
        self.driver.find_element_by_id(self.txtCompanyname_id).send_keys(cname)

    def setAdminContent(self,content):
        self.driver.find_element_by_xpath(self.txtAdminComment_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()

    def setMgrOfVendor(self,vndr):
        drp=Select(self.driver.find_element_by_xpath(self.drpmgrofVendor_xpath))
        drp.select_by_visible_text(vndr)