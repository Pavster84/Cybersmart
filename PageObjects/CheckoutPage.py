from selenium.webdriver.common.by import By
from selenium import webdriver
from PageObjects.ConfirmationPage import ConfirmationPage


class CheckOutPage:

    # create constructor which accepts driver argument and performs connection to local driver
    def __init__(self, driver):
        self.driver = driver

    companyNameTxtBox = (By.CSS_SELECTOR, "#id_company_name")
    adminEmailTxtBox = (By.CSS_SELECTOR, "#id_admin_email")
    adminFirstNameTxtBox = (By.CSS_SELECTOR, "#id_admin_first_name")
    adminLastNameTxtBox = (By.CSS_SELECTOR, "#id_admin_last_name")
    productCERadioBtn = (By.CSS_SELECTOR, "#id_product_0")
    productCEPlusRadioBtn = (By.CSS_SELECTOR, "#id_product_1")
    productGDPRRadioBtn = (By.CSS_SELECTOR, "#id_product_2")
    productAllRadioBtn = (By.CSS_SELECTOR, "#id_product_3")
    submitBtn = (By.CSS_SELECTOR, "input[type='submit']")


    def set_company_name_txt_box(self, companyName):
        self.driver.find_element(*CheckOutPage.companyNameTxtBox).send_keys(companyName)

    def set_admin_email_txt_box(self, adminEmail):
        self.driver.find_element(*CheckOutPage.adminEmailTxtBox).send_keys(adminEmail)

    def set_admin_first_name_txt_box(self, adminFirstName):
        self.driver.find_element(*CheckOutPage.adminFirstNameTxtBox).send_keys(adminFirstName)

    def set_admin_last_name_txt_box(self, adminLastName):
        self.driver.find_element(*CheckOutPage.adminLastNameTxtBox).send_keys(adminLastName)

    def get_product_ce_radio_btn(self):
        return self.driver.find_element(*CheckOutPage.productCERadioBtn)

    def get_product_ceplus_radio_btn(self):
        return self.driver.find_element(*CheckOutPage.productCEPlusRadioBtn)

    def get_product_ce_radio_btn(self):
        return self.driver.find_element(*CheckOutPage.productCERadioBtn)

    def get_product_gdpr_radio_btn(self):
        return self.driver.find_element(*CheckOutPage.productGDPRRadioBtn)

    def get_dynamic_radio_btn(self, val):
        self.driver.find_element_by_xpath("//input[@id=" + "'" + val + "'" + "]").click()

    def submit_form(self):
        self.driver.find_element(*CheckOutPage.submitBtn).click()
        #confirmationPage = ConfirmationPage(self.driver)
       # return confirmationPage

