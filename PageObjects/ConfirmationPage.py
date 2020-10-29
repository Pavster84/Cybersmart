from selenium.webdriver.common.by import By


class ConfirmationPage:

    def __init__(self, driver):
        self.driver = driver

    checkoutSubTxt = (By.XPATH, "//div[contains(text(),'Fake App Checkout Subscription')]")
    checkoutThankYouTxt = (By.XPATH, "//div[contains(text(),'Thank yoou')]")

    def get_checkout_subscription_success_txt(self):
        return self.driver.find_element(*ConfirmationPage.checkoutSubTxt)

    def get_success_thank_you_txt(self):
        return self.driver.find_element(*ConfirmationPage.checkoutThankYouTxt)


